import csv
from collections import defaultdict

def top_5_sommets_par_degre(nom_fichier):
    

    degres = defaultdict(int)

    # Lecture du fichier CSV
    with open(nom_fichier, "r", encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            i = int(ligne["sommet_source"])
            j = int(ligne["sommet_cible"])
            degres[i] += 1
            degres[j] += 1

    # Tri des sommets par degré décroissant
    top_5 = sorted(degres.items(), key=lambda x: x[1], reverse=True)[:5]

    # Affichage
    print("Les 5 sommets ayant les plus hauts degrés :")
    for sommet, degre in top_5:
        print(f"Sommet {sommet} → degré {degre}")

    return top_5

# Exemple d’exécution
top_5_sommets_par_degre("contacts.csv")
