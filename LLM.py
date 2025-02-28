import networkx as nx
import matplotlib.pyplot as plt
import random

# Número de nós
eNe = 50
# Probabilidade fixa de conexão entre nós
Pe = 0.1

# Criar um grafo baseado em probabilidade fixa de conexão
def gerar_grafo_aleatorio(n, p):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G.add_edge(i, j)
    return G

G = gerar_grafo_aleatorio(eNe, Pe)

# Desenhar o grafo
plt.figure(figsize=(6,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=12)
plt.title(f'Grafo Aleatório com {eNe} Nós (Pe={Pe})')
plt.show()

# Criar histograma do grau dos nós
graus = [d for n, d in G.degree()]
plt.figure(figsize=(6,4))
plt.hist(graus, bins=range(min(graus), max(graus) + 2), color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Grau')
plt.ylabel('Frequência')
plt.title('Histograma do Grau dos Nós')
plt.xticks(range(min(graus), max(graus) + 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
