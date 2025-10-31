import csv
import networkx as nx
import random

# ===== TON CODE DE MODIFICATION DU GRAPHE =====
top_5_degre = [0, 12, 34, 45, 78]
top_5_proximite = [7, 19, 23, 45, 120]
sommets_a_supprimer = set(top_5_degre + top_5_proximite)
print("Sommets a supprimer :", sommets_a_supprimer)

fichier_csv = "contacts.csv"
G = nx.Graph()

with open(fichier_csv, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # normaliser les cles pour accepter differents en-tetes
        r = { (k.strip().lower() if k is not None else k): v for k, v in row.items() }

        source_candidates = ["sommet_source", "source", "i", "from"]
        target_candidates = ["sommet_cible", "cible", "j", "to", "target"]
        weight_candidates = ["distance", "weight", "w"]

        src_key = next((k for k in source_candidates if k in r), None)
        tgt_key = next((k for k in target_candidates if k in r), None)
        w_key = next((k for k in weight_candidates if k in r), None)

        if src_key is None or tgt_key is None:
            continue

        try:
            u = int(r[src_key])
            v = int(r[tgt_key])
            w = float(r[w_key]) if w_key in r and r[w_key] not in (None, "") else 1.0
        except (TypeError, ValueError):
            continue

        G.add_edge(u, v, weight=w)

G.remove_nodes_from(sommets_a_supprimer)
print(f"Nombre de sommets apres suppression : {G.number_of_nodes()}")
print(f"Nombre d'aretes apres suppression : {G.number_of_edges()}")

nouveau_fichier = "contacts_modifie.csv"
with open(nouveau_fichier, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["sommet_source", "sommet_cible", "distance"])
    for u, v, data in G.edges(data=True):
        writer.writerow([u, v, data['weight']])

print(f" Nouveau fichier '{nouveau_fichier}' cree avec succes !")

# ===== FONCTION : CAMPAGNE 3 JOURS =====
def campagne_3_jours_faible_proximite(fichier="contacts_modifie.csv"):
    G = nx.Graph()
    with open(fichier, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            u, v, w = int(row[0]), int(row[1]), float(row[2])
            G.add_edge(u, v, weight=w)

    if G.number_of_nodes() == 0:
        return 0

    closeness = nx.closeness_centrality(G)
    depart = min(closeness, key=closeness.get)
    print(f"\nSommet de depart : {depart} (proximite = {closeness[depart]:.5f})")

    courant = depart
    touches = {courant}
    aretes_utilisees = set()

    for jour in range(1, 4):
        voisins = [v for v in G.neighbors(courant) if tuple(sorted([courant, v])) not in aretes_utilisees]
        if not voisins:
            print(f"  Jour {jour} : aucun voisin disponible -> arret")
            break
        prochain = random.choice(voisins)
        arete = tuple(sorted([courant, prochain]))
        aretes_utilisees.add(arete)
        touches.add(prochain)
        print(f"  Jour {jour} : {courant} -> {prochain} -> total touches = {len(touches)}")
        courant = prochain

    return len(touches)

# ===== EXECUTION =====
resultat = campagne_3_jours_faible_proximite()
print(f"\n{'='*50}")
print(f"RESULTAT : {resultat} sommets touches apres 3 jours")
print(f"{'='*50}")