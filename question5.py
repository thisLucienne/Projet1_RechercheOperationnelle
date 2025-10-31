import networkx as nx
import csv
import random

def campagne_5_jours(fichier_csv="contacts.csv"):
    # --- 1. Charger le graphe depuis le CSV ---
    G = nx.Graph()
    with open(fichier_csv, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Ignorer l'en-tête
        for row in reader:
            u, v, weight = int(row[0]), int(row[1]), int(row[2])
            G.add_edge(u, v, weight=weight)

    # --- 2. Trouver le sommet de plus haut degré ---
    degres = dict(G.degree())
    sommet_depart = max(degres, key=degres.get)
    print(f"Sommet de départ (plus haut degré) : {sommet_depart} (degré = {degres[sommet_depart]})")

    # --- 3. Simuler 5 jours : parcourir 5 arêtes ---
    sommet_courant = sommet_depart
    sommets_touches = {sommet_depart}  # ensemble des sommets visités
    aretes_parcourues = set()          # arêtes déjà utilisées (u, v) avec u < v

    for jour in range(1, 6):
        # Récupérer les voisins non encore "explorés" via une arête non parcourue
        voisins_disponibles = []
        for voisin in G.neighbors(sommet_courant):
            arete = tuple(sorted([sommet_courant, voisin]))
            if arete not in aretes_parcourues:
                voisins_disponibles.append(voisin)

        if not voisins_disponibles:
            print(f"Jour {jour} : Aucun chemin disponible -> arrêt.")
            break

        # Choisir un voisin aléatoirement
        prochain_sommet = random.choice(voisins_disponibles)
        arete = tuple(sorted([sommet_courant, prochain_sommet]))
        aretes_parcourues.add(arete)
        sommets_touches.add(prochain_sommet)

        print(f"Jour {jour} : {sommet_courant} -> {prochain_sommet} (total touchés : {len(sommets_touches)})")

        sommet_courant = prochain_sommet

    # --- 4. Retourner le nombre de sommets touchés ---
    return len(sommets_touches)

# Ensuite, lance la campagne
nb_sommets_touches = campagne_5_jours("contacts.csv")
print(f"\n=== RÉSULTAT FINAL ===")
print(f"Nombre de sommets touchés après 5 jours : {nb_sommets_touches}")