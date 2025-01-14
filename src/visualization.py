# visualization.py
import folium
import webbrowser
import polyline
import googlemaps
from config import GOOGLE_API_KEY
from graph_setup import get_cidades_coordenadas

# Inicializa o cliente da Google Maps API usando a chave já definida
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

def obter_caminho_real(origem, destino):
    try:
        directions_result = gmaps.directions(origin=f"{origem}, MG",
                                             destination=f"{destino}, MG",
                                             mode="driving",
                                             alternatives=False)
        if directions_result:
            polyline_str = directions_result[0]['overview_polyline']['points']
            return polyline.decode(polyline_str)
    except Exception as e:
        print(f"Erro ao obter rota de {origem} para {destino}: {e}")
    return None

def gerar_mapa(melhores_rotas, nome_arquivo="rotas_otimizadas.html"):
    # Centraliza o mapa na sede, Patrocinio
    cidades_coordenadas = get_cidades_coordenadas()
    lat_inicial, lon_inicial = cidades_coordenadas["Patrocínio"]
    mapa = folium.Map(location=[lat_inicial, lon_inicial], zoom_start=7)

    cores = ['red', 'blue', 'green']  # Cores para as 3 rotas

    # Limita a 3 rotas caso a lista contenha mais
    melhores_rotas = melhores_rotas[:3] 

    for (rota, custo), cor in zip(melhores_rotas, cores):
        caminho_completo = []
        # Obtém o percurso real para cada par consecutivo na rota
        for i in range(len(rota) - 1):
            origem = rota[i]
            destino = rota[i+1]
            caminho_segmento = obter_caminho_real(origem, destino)
            if caminho_segmento:
                # Adiciona o segmento ao caminho completo
                # Note: para evitar sobreposição de pontos duplicados,
                # podemos omitir o primeiro ponto de cada segmento, exceto o primeiro segmento.
                if caminho_completo:
                    caminho_completo.extend(caminho_segmento[1:])
                else:
                    caminho_completo.extend(caminho_segmento)

        tooltip_text = f"Rota: {' -> '.join(rota)}\nCusto: {custo:.2f}"
        if caminho_completo:
            folium.PolyLine(caminho_completo, color=cor, weight=5, opacity=0.8,
                            tooltip=tooltip_text).add_to(mapa)

    mapa.save(nome_arquivo)
    print(f"Mapa salvo como '{nome_arquivo}'.")
    webbrowser.open(nome_arquivo)
    
def gerar_mapas_separados(melhores_rotas, cores=None):
    from graph_setup import get_cidades_coordenadas
    cidades_coordenadas = get_cidades_coordenadas()
    lat_inicial, lon_inicial = cidades_coordenadas["Patrocínio"]
    
    if cores is None:
        cores = ['red', 'blue', 'green']

    for idx, ((rota, custo), cor) in enumerate(zip(melhores_rotas, cores), start=1):
        # Força a cor vermelha para o primeiro mapa
        if idx == 1:
            cor = 'red'
        
        mapa = folium.Map(location=[lat_inicial, lon_inicial], zoom_start=7)
        caminho_completo = []
        
        for i in range(len(rota) - 1):
            origem = rota[i]
            destino = rota[i+1]
            caminho_segmento = obter_caminho_real(origem, destino)
            if caminho_segmento:
                if caminho_completo:
                    caminho_completo.extend(caminho_segmento[1:])
                else:
                    caminho_completo.extend(caminho_segmento)
        
        tooltip_text = f"Rota: {' -> '.join(rota)}\nCusto: {custo:.2f}"
        if caminho_completo:
            folium.PolyLine(caminho_completo, color=cor, weight=5, opacity=0.8,
                            tooltip=tooltip_text).add_to(mapa)
        else:
            # Fallback: desenha linha reta entre as cidades se nenhum caminho real foi encontrado
            coords_rota = [cidades_coordenadas[c] for c in rota if c in cidades_coordenadas]
            folium.PolyLine(coords_rota, color=cor, weight=5, opacity=0.8,
                            tooltip=tooltip_text + " (linha reta)")\
                            .add_to(mapa)
        
        file_name = f"rota_{idx}.html"
        mapa.save(file_name)
        print(f"Mapa da Rota {idx} salvo como '{file_name}' com cor {cor}.")

