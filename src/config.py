# config.py
NUM_ANTS = 50
NUM_ITERATIONS = 200
CIDADE_INICIAL = "Patrocínio"
ALPHA = 1.0 # Peso dado à trilha de feromônio ao escolher o próximo nó (cidade).
BETA = 2.0 # Peso dado à heurística (inversa da distância ou custo) ao escolher o próximo nó.
EVAPORATION_RATE = 0.3

# Pesos para critérios multiobjetivo
W_DISTANCE = 0.5
W_COST = 0.3
W_TIME = 0.2

# Parâmetros de restrição (exemplo)
EVITAR_PEDAGIOS = False       # Usado em cálculos de custo
AVOID_TOLLS = True            # Para a Google Directions API: evitar pedágios
AVOID_HIGHWAYS = False        # Para a Google Directions API: evitar rodovias

GOOGLE_API_KEY = "secret"
