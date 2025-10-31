import csv
from collections import defaultdict

def top_5_sommets_par_degre(nom_fichier):
    

    degres = defaultdict(int)

    # Lecture du fichier CSV
    with open(nom_fichier, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            # Normaliser les clés pour accepter plusieurs en-têtes possibles
            row = { (k.strip().lower() if k is not None else k): v for k, v in ligne.items() }

            source_candidates = ["sommet_source", "source", "i", "from"]
            target_candidates = ["sommet_cible", "cible", "j", "to", "target"]

            src_key = next((k for k in source_candidates if k in row), None)
            tgt_key = next((k for k in target_candidates if k in row), None)

            if src_key is None or tgt_key is None:
                # Ligne non conforme, on ignore
                continue

            try:
                i = int(row[src_key])
                j = int(row[tgt_key])
            except (TypeError, ValueError):
                # Valeurs non numériques, on ignore la ligne
                continue

            degres[i] += 1
            degres[j] += 1

    # Tri des sommets par degré décroissant
    top_5 = sorted(degres.items(), key=lambda x: x[1], reverse=True)[:5]

    # Affichage
    print("Les 5 sommets ayant les plus hauts degres :")
    for sommet, degre in top_5:
        print(f"Sommet {sommet} -> degre {degre}")

    return top_5

# Exemple d’exécution
top_5_sommets_par_degre("contacts.csv")
