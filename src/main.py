# src/main.py
import random
random.seed()  # Reinicializa o gerador de números aleatórios com base no tempo do sistema

from config import NUM_ANTS, NUM_ITERATIONS, CIDADE_INICIAL, ALPHA, BETA, EVAPORATION_RATE
from graph_setup import criar_grafo
from aco import AntColony
from visualization import gerar_mapa, gerar_mapas_separados

def main():
    # 1. Criar o grafo de cidades
    G = criar_grafo()

    # 2. Executar o ACO
    aco = AntColony(G, num_ants=NUM_ANTS, num_iterations=NUM_ITERATIONS,
                    alpha=ALPHA, beta=BETA, evaporation_rate=EVAPORATION_RATE)
    melhores_rotas = aco.run(CIDADE_INICIAL)

    print("Top 3 rotas encontradas: \n")
    for i, (rota, custo) in enumerate(melhores_rotas):
        print(f"Rota {i+1}: {' -> '.join(rota)} | Custo total: {custo:.2f}\n")


    # 3. Visualizar as rotas no mapa
    # gerar_mapa(melhores_rotas)
    gerar_mapas_separados(melhores_rotas)

if __name__ == "__main__":
    main()
