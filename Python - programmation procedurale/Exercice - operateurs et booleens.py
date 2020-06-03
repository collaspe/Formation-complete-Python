"""
Enoncé : 
Dans la première partie de cet exercice 'Le nombre mystère', nous allons vérifier l'égalité entre un nombre entré par l'utilisateur avec un nombre défini dans notre script de départ.

Demander à l'utilisateur d'entrer un nombre pour tenter de deviner le nombre mystère.

Afficher si le nombre entré par l'utilisateur est égal au nombre mystère (afficher un booléen True ou False).
"""

nombre_mystere = 7

nombre_utilisateur = input("Quel est le nombre mystère ? ")

resultat = int(nombre_utilisateur) == nombre_mystere
print(resultat)