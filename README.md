# Projeto de Otimização de Rotas por Colônia de Formigas (ACO)

Este projeto implementa o **Algoritmo de Colônia de Formigas (ACO)** para otimização de rotas logísticas na região do Alto Paranaíba, Minas Gerais. Inspirado no comportamento coletivo das formigas em busca de caminhos eficientes, o sistema encontra as melhores rotas para uma transportadora de café, garantindo que passe por todas as cidades da região, saindo e retornando à sede em Patrocínio.

## 📋 Descrição do Projeto

O algoritmo utiliza uma estrutura de grafo para representar cidades e suas conexões. Cada aresta possui um nível de **feromônio** que guia as formigas virtuais na busca por caminhos ótimos. Ao longo das iterações, as rotas com menores custos são reforçadas através da atualização dos feromônios, permitindo a descoberta de soluções de alta qualidade baseadas em múltiplos critérios, como distância, tempo e custo.

As três melhores rotas identificadas são exibidas em um mapa interativo com cores distintas, utilizando a biblioteca **Folium** para visualização. A integração com a **Google Maps API** possibilita o acesso a dados reais de distância e tempo, aumentando a precisão da otimização.

## 🎯 Objetivos

- **Implementar o ACO** para encontrar rotas ótimas entre cidades do Alto Paranaíba.
- **Representar cidades e conexões** utilizando grafos com pesos que incorporam distância, custo e tempo.
- **Visualizar rotas otimizadas** em um mapa interativo, destacando as três melhores em cores diferentes.
- **Integrar com a Google Maps API** para obter dados reais de rotas, aumentando a fidelidade do sistema.
- **Simular restrições reais**, como a falta de conexões diretas entre cidades e a variabilidade nas condições das rodovias.

## 🗂️ Estrutura do Projeto

```
projeto_aco/
├── data/                     # Arquivos de dados (opcional)
├── src/
│   ├── __init__.py
│   ├── config.py             # Configurações e parâmetros do sistema
│   ├── graph_setup.py        # Criação do grafo com cidades e arestas
│   ├── aco.py                # Implementação do Algoritmo de Colônia de Formigas
│   ├── visualization.py      # Funções para visualização interativa das rotas
│   └── main.py               # Script principal para executar o sistema
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo de documentação
└── rotas_otimizadas.html     # Mapa interativo gerado com as rotas
```

## ⚙️ Dependências

- Python 3.x
- Bibliotecas Python:
  - networkx
  - folium
  - numpy
  - googlemaps

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto_aco.git
   cd projeto_aco
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure a chave da Google Maps API em `src/config.py`:
   ```python
   GOOGLE_API_KEY = "SUA_CHAVE_API_AQUI"
   ```

5. Certifique-se de que o grafo está configurado corretamente em `src/graph_setup.py` com cidades e arestas do Alto Paranaíba.

## ▶️ Uso

Para executar o programa e visualizar as três melhores rotas:

```bash
python -m src.main
```

O script irá:
- Criar o grafo de cidades e conexões.
- Executar o algoritmo ACO para encontrar rotas otimizadas.
- Exibir as três melhores rotas no terminal.
- Gerar e abrir automaticamente um mapa interativo (`rotas_otimizadas.html`) mostrando as rotas em cores diferentes.

## 📜 Funcionamento Interno

- **ACO:** As formigas simuladas exploram o grafo, depositando feromônios nas arestas com base na qualidade das rotas encontradas (distância, tempo, custo). A atualização contínua dos níveis de feromônio guia a busca por soluções ótimas.
- **Pheromone:** A variável `pheromone` armazena os níveis de feromônio em cada aresta, influenciando a escolha de caminhos pelas formigas em iterações subsequentes.
- **Visualização:** As melhores rotas são plotadas em um mapa interativo utilizando a biblioteca Folium, com cores distintas para cada rota e tooltips informativos.

## 🌈 Visualização das Três Melhores Rotas

O sistema apresenta as três melhores rotas em sessões distintas, destacando cada uma com uma cor diferente. Abaixo, veja uma visualização de cada rota:

### Rota 1
- **Imagem da Rota 1:**
  
  ![Rota 1](https://github.com/Micael-Resende/Algoritmo-ACO/blob/master/images/rota1.png)  

### Rota 2
- **Imagem da Rota 2:**
  
  ![Rota 2](https://github.com/Micael-Resende/Algoritmo-ACO/blob/master/images/rota2.png)  

### Rota 3
- **Imagem da Rota 3:**
  
  ![Rota 3](https://github.com/Micael-Resende/Algoritmo-ACO/blob/master/images/rota3.png)  


## 🛠️ Personalização e Expansões Futuras

- **Multiobjetivo:** Expandir a função de custo para considerar critérios adicionais, como pedágios, consumo de combustível ou condições de tráfego.
- **Interface Gráfica Avançada:** Desenvolver uma interface interativa mais robusta para configurar restrições dinâmicas e visualizar detalhes adicionais das rotas.
- **Expansão de Dados:** Adicionar mais cidades e conexões reais, ajustando as coordenadas e distâncias conforme necessário para maior precisão.

## 📄 Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---
