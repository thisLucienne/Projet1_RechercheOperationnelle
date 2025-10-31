import networkx as nx
import random
import csv
import matplotlib.pyplot as plt

# ----- PARAMÈTRES -----
n = 250      # nombre de sommets
p = 0.3     # probabilité de création d’une arête
min_d = 1   # distance minimale
max_d = 6   # distance maximale

# ----- CRÉATION DU GRAPHE -----
G = nx.erdos_renyi_graph(n, p)

# ----- AJOUT DE DISTANCES ALÉATOIRES -----
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(min_d, max_d)

# ----- ÉCRITURE DANS UN FICHIER CSV -----
fichier_csv = "contacts.csv"

with open(fichier_csv, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["sommet_source", "sommet_cible", "distance"])
    for (u, v, data) in G.edges(data=True):
        writer.writerow([u, v, data['weight']])

print(f"Fichier '{fichier_csv}' généré avec succès !")
print(f"Nombre de sommets : {G.number_of_nodes()}")
print(f"Nombre d'arêtes : {G.number_of_edges()}")

# ----- VISUALISATION DU GRAPHE -----
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Positionnement automatique

# Dessin du graphe
nx.draw(
    G, pos,
    with_labels=True,
    node_color="skyblue",
    node_size=800,
    font_size=10,
    font_weight="bold",
    edge_color="gray"
)

# Afficher les poids (distances) sur les arêtes
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

plt.title("Graphe aléatoire à 10 sommets avec distances (1 à 6)")
plt.show()
