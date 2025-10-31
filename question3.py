import random
import matplotlib.pyplot as plt
from collections import Counter

# ----- PARAMÈTRES -----
n = 250        # nombre de sommets
p = 0.3        # probabilité de création d’une arête
min_d = 1      # distance minimale
max_d = 6      # distance maximale
INF = float('inf')

# ----- CRÉATION DU GRAPHE SOUS FORME DE MATRICE D'ADJACENCE -----
graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if random.random() < p:
            w = random.randint(min_d, max_d)
            graph[i][j] = w
            graph[j][i] = w  # graphe non orienté

# ----- FONCTION D'IMPLEMENTATION DE DIJKSTRA -----
def dijkstra(graph, src):
    n = len(graph)
    dist = [INF]*n
    visited = [False]*n
    dist[src] = 0

    for _ in range(n):
        # trouver le sommet non visité avec la distance minimale
        u = min((d, idx) for idx, d in enumerate(dist) if not visited[idx])[1]
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    return dist

# ----- CALCUL DE LA PROXIMITÉ POUR TOUS LES SOMMETS -----
proximite = []
for node in range(n):
    dist = dijkstra(graph, node)
    proximite.append(sum(d for d in dist if d < INF))  # somme des distances atteignables

# ----- DISTRIBUTION DE PROXIMITÉ -----
distribution = Counter(proximite)

# Affichage texte
print("--- Distribution de proximité ---")
for k, v in sorted(distribution.items()):
    print(f"Proximité {k} : {v} sommets")

# ----- HISTOGRAMME -----
plt.figure(figsize=(10,5))
plt.bar(distribution.keys(), distribution.values(), color='lightcoral', edgecolor='black')
plt.title("Distribution de proximité des sommets")
plt.xlabel("Somme des distances vers tous les autres sommets")
plt.ylabel("Nombre de sommets")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
