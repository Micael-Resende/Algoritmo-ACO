# precalculo_arestas.py
import json
import itertools
import googlemaps
from config import GOOGLE_API_KEY
from graph_setup import cidades_coordenadas

# Inicializa o cliente da Google Maps API
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

dados_arestas = {}

# Gera todas as combinações possíveis de duas cidades
edges = itertools.combinations(cidades_coordenadas.keys(), 2)

for (tmp_city1, tmp_city2) in edges:
    try:
        result = gmaps.distance_matrix(f"{tmp_city1}, MG", f"{tmp_city2}, MG", mode="driving")
        element = result["rows"][0]["elements"][0]
        if element["status"] == "OK":
            distance = element["distance"]["value"]
            duration = element["duration"]["value"]
            dados_arestas[f"{tmp_city1}-{tmp_city2}"] = {
                "distancia": distance,
                "duracao": duration
            }
        else:
            dados_arestas[f"{tmp_city1}-{tmp_city2}"] = {
                "distancia": None,
                "duracao": None
            }
    except Exception as e:
        print(f"Erro ao obter dados para {tmp_city1}-{tmp_city2}: {e}")
        dados_arestas[f"{tmp_city1}-{tmp_city2}"] = {
            "distancia": None,
            "duracao": None
        }

# Salva os dados pré-calculados em um arquivo JSON
with open("dados_arestas.json", "w") as f:
    json.dump(dados_arestas, f, indent=4)

print("Pré-cálculo concluído e dados salvos em dados_arestas.json.")
