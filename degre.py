import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def calculer_distribution_degres(nom_fichier):
    """
    Calcule le degré de chaque sommet à partir d’un fichier CSV
    et affiche la distribution des degrés sous forme d’histogramme.
    
    Format attendu du fichier :
    i,j,distance
    0,1,3
    0,4,2
    ...
    """
    # Dictionnaire pour stocker le degré de chaque sommet
    degres = defaultdict(int)

    # Lecture du fichier CSV
    with open(nom_fichier, "r") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            i = int(ligne["i"])
            j = int(ligne["j"])
            # Comme le graphe est non orienté, chaque lien compte pour les deux sommets
            degres[i] += 1
            degres[j] += 1

    # Construction de la distribution des degrés
    distribution = defaultdict(int)
    for degre in degres.values():
        distribution[degre] += 1

    # Affichage texte
    print(" Distribution des degrés :")
    for k in sorted(distribution.keys()):
        print(f"Degré {k} : {distribution[k]} sommets")

    # --- Création de l’histogramme ---
    plt.bar(distribution.keys(), distribution.values(), color="skyblue", edgecolor="black")
    plt.xlabel("Degré (nombre de contacts)")
    plt.ylabel("Nombre de sommets")
    plt.title("Distribution des degrés du graphe")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


# Exemple d’exécution

calculer_distribution_degres("contacts.csv")