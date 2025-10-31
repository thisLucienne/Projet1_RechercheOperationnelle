import csv
import networkx as nx

# ----- Étape 1 : Identifier les sommets à supprimer -----
top_5_degre = [0, 12, 34, 45, 78]          
top_5_proximite = [7, 19, 23, 45, 120]      

# Fusion des deux listes et supprimer les doublons
sommets_a_supprimer = set(top_5_degre + top_5_proximite)
print("Sommets à supprimer :", sommets_a_supprimer)

# ----- Étape 2 : Lire le graphe original -----
fichier_csv = "contacts.csv"
G = nx.Graph()

with open(fichier_csv, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        u = int(row['sommet_source'])
        v = int(row['sommet_cible'])
        w = float(row['distance'])
        G.add_edge(u, v, weight=w)

# ----- Étape 3 : Supprimer les sommets -----
G.remove_nodes_from(sommets_a_supprimer)
print(f"Nombre de sommets après suppression : {G.number_of_nodes()}")
print(f"Nombre d'arêtes après suppression : {G.number_of_edges()}")

# ----- Étape 4 : Écrire le nouveau graphe dans un fichier CSV -----
nouveau_fichier = "contacts_modifie.csv"
with open(nouveau_fichier, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["sommet_source", "sommet_cible", "distance"])
    for u, v, data in G.edges(data=True):
        writer.writerow([u, v, data['weight']])

print(f" Nouveau fichier '{nouveau_fichier}' créé avec succès !")
