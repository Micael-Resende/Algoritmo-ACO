import random
from config import W_DISTANCE, W_COST, W_TIME, EVITAR_PEDAGIOS

class AntColony:
    def __init__(self, graph, num_ants, num_iterations, alpha=1.0, beta=2.0, evaporation_rate=0.5):
        self.graph = graph
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.pheromone = self.initialize_pheromone()

    def initialize_pheromone(self):
        pheromone = {}
        for edge in self.graph.edges():
            pheromone[edge] = 1.0
            pheromone[(edge[1], edge[0])] = 1.0
        return pheromone

    def escolher_proximo(self, atual, visitados):
        vizinhos = [n for n in self.graph.neighbors(atual) if n not in visitados]
        if not vizinhos:
            return None
        probabilidades = []
        total = 0
        for viz in vizinhos:
            fer = self.pheromone.get((atual, viz), 1.0) ** self.alpha
            heur = (1.0 / self.calcular_custo(atual, viz)) ** self.beta
            prob = fer * heur
            probabilidades.append((viz, prob))
            total += prob
        rand = random.uniform(0, total)
        cumul = 0.0
        for viz, prob in probabilidades:
            cumul += prob
            if rand <= cumul:
                return viz
        return vizinhos[-1]

    def construir_rota(self, inicio):
        rota = [inicio]
        visitados = set(rota)
        atual = inicio
        while len(visitados) < len(self.graph.nodes()):
            prox_cidade = self.escolher_proximo(atual, visitados)
            if prox_cidade is None:
                break
            rota.append(prox_cidade)
            visitados.add(prox_cidade)
            atual = prox_cidade
        # Retorna à cidade inicial para fechar o ciclo
        if self.graph.has_edge(atual, inicio):
            rota.append(inicio)
        return rota


    def calcular_custo(self, u, v):
        edge = self.graph[u][v]
        distance = edge.get('distancia', 1)
        duration = edge.get('duracao', 1)
        simulated_cost = distance * 0.001  # Exemplo de custo simulado

        custo_total = (W_DISTANCE * distance + 
                       W_TIME * duration + 
                       W_COST * simulated_cost)

        if EVITAR_PEDAGIOS and edge.get('pedagio', False):
            custo_total *= 1.5
        
        return custo_total

    def custo_rota(self, rota):
        total_custo = 0
        for i in range(len(rota)-1):
            u, v = rota[i], rota[i+1]
            total_custo += self.calcular_custo(u, v)
        return total_custo

    def atualizar_feromonio(self, rotas):
        for edge in self.pheromone:
            self.pheromone[edge] *= (1 - self.evaporation_rate)
        for rota, custo in rotas:
            deposit = 1.0 / custo if custo > 0 else 0
            for i in range(len(rota)-1):
                u, v = rota[i], rota[i+1]
                self.pheromone[(u,v)] += deposit
                self.pheromone[(v,u)] += deposit

    def run(self, inicio):
        melhores_rotas = []
        for it in range(self.num_iterations):
            todas_rotas = []
            for _ in range(self.num_ants):
                rota = self.construir_rota(inicio)
                custo = self.custo_rota(rota)
                todas_rotas.append((rota, custo))
            self.atualizar_feromonio(todas_rotas)
            todas_rotas.sort(key=lambda x: x[1])
            # Adiciona as top 3 da iteração à lista geral
            melhores_rotas.extend(todas_rotas[:3])
        
        # Ordena todas as rotas coletadas pelo custo
        melhores_rotas.sort(key=lambda x: x[1])
        
        # Filtra rotas duplicadas para obter rotas distintas
        rotas_unicas = []
        for rota, custo in melhores_rotas:
            # Verifica se a rota já está na lista de rotas únicas
            if rota not in [r for r, _ in rotas_unicas]:
                rotas_unicas.append((rota, custo))
            if len(rotas_unicas) == 3:
                break
        
        return rotas_unicas
