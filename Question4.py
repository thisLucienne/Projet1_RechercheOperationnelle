import networkx as nx
import csv

def top_5_proximite(fichier_csv):
    """
    Lit un fichier CSV contenant les arêtes d'un graphe pondéré et retourne
    la liste des 5 sommets ayant les plus hautes valeurs de proximité.
    
    Le fichier CSV doit contenir : sommet_source, sommet_cible, distance
    """
    # --- Étape 1 : Création du graphe pondéré ---
    G = nx.Graph()

    with open(fichier_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            u = row['i']
            v = row['j']
            w = float(row['distance'])
            G.add_edge(u, v, weight=w)

    # --- Étape 2 : Calcul de la centralité de proximité ---
    closeness = nx.closeness_centrality(G, distance='weight')

    # --- Étape 3 : Trier les sommets par valeur décroissante ---
    top_5 = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]

    # --- Étape 4 : Afficher les résultats ---
    print("\nLes 5 sommets ayant les plus hautes valeurs de proximité :")
    for i, (sommet, prox) in enumerate(top_5, start=1):
        print(f"{i}. Sommet {sommet} -> proximite = {prox:.4f}")

    return top_5

# Suppose que ton fichier s’appelle "graphe_10_sommets.csv"
fichier = "contacts.csv"

resultats = top_5_proximite(fichier)
