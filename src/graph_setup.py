# graph_setup.py
import json
import networkx as nx
import numpy as np
import itertools

# Definições de cidades com coordenadas aproximadas
cidades_coordenadas = {
    "Abadia dos Dourados": (-18.7200, -46.8500),
    "Águas Formosas": (-18.8500, -47.0000),
    "Arapuá": (-19.0000, -48.5000),
    "Araxá": (-19.5917, -46.9739),
    "Belo Horizonte": (-19.9167, -43.9345),
    "Campina Verde": (-16.7589, -50.5850),
    "Campos Altos": (-19.8934, -46.6831),
    "Carmo do Paranaíba": (-19.9770, -46.8830),
    "Coromandel": (-19.2019, -45.5141),
    "Cruzeiro da Fortaleza": (-18.1964, -49.3644),
    "Frutal": (-19.2427, -47.9400),
    "Guimarânia": (-19.1234, -50.0000),
    "Iraí de Minas": (-19.5030, -48.1690),
    "Itapagipe": (-20.5903, -45.9298),
    "João Pinheiro": (-18.8360, -49.1946),
    "Lagoa Formosa": (-19.4753, -44.8017),
    "Luz": (-19.5312, -45.5111),
    "Patos de Minas": (-18.5817, -46.5183),
    "Patrocínio": (-18.9440, -46.9928),
    "Presidente Olegário": (-18.9706, -50.0105),
    "Rio Paranaíba": (-19.8890, -47.1000),
    "Romaria": (-19.4590, -46.8920),
    "Santa Vitória": (-19.2950, -48.2430),
    "São Gotardo": (-19.9130, -46.8320),
    "São João do Paraíso": (-19.6620, -46.9220),
    "São Pedro do Paranaíba": (-19.5699, -47.1551),
    "Tiros": (-19.9813, -48.1917),
    "Uberaba": (-19.7479, -47.9354)
}


def distancia_euclidiana(cidade1, cidade2, coords=cidades_coordenadas):
    lat1, lon1 = coords[cidade1]
    lat2, lon2 = coords[cidade2]
    return np.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def criar_grafo():
    G = nx.Graph()
    # Adiciona todos os nós (cidades) no grafo
    for cidade in cidades_coordenadas:
        G.add_node(cidade)
        
    # Tenta carregar dados pré-calculados de arestas
    try:
        with open("dados_arestas.json", "r") as f:
            dados_arestas = json.load(f)
    except FileNotFoundError:
        print("Arquivo dados_arestas.json não encontrado. Execute precalculo_arestas.py primeiro.")
        return G

    # Adiciona arestas ao grafo com base nos dados carregados
    for key, dados in dados_arestas.items():
        try:
            u, v = key.split('-')
        except ValueError:
            continue

        if dados and dados["distancia"] is not None and dados["duracao"] is not None:
            G.add_edge(u, v, distancia=dados["distancia"], duracao=dados["duracao"])
        else:
            # Se não houver dados válidos, utiliza a distância euclidiana como fallback
            dist = distancia_euclidiana(u, v)
            G.add_edge(u, v, distancia=dist, duracao=1)
    return G

def get_cidades_coordenadas():
    return cidades_coordenadas
