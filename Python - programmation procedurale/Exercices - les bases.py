"""
Exercice 1 :
Demander à l'utilisateur d'entrer un premier nombre

Demander à l'utilisateur d'entrer un deuxième nombre

Afficher à l'écran le résultat de l'addition (exemple : 'Le résultat de l'addition de 5 avec 10 est égal à 15')
"""

a = int(input("Entrez un premier nombre : "))
b = int(input("Entrez un deuxième nombre : "))
resultat = f"Le résultat de l'addition de {a} avec {b} est égal à {a + b}"
print(resultat)


"""
Exercice 2 :
Script de départ : 
a = "J'ai une classe de " + 30 + " élèves"
b = 10 + " + " + "5" + " est égal à " + 15
c = 10 + "5"
d = "L'addition de 10 + 5 est égal à " + 10 + 5

Phrases à afficher :

J'ai une classe de 30 élèves

10 + 5 est égal à 15

15

L'addition de 10 + 5 est égal à 15
"""

a = "J'ai une classe de " + str(30) + " élèves"
b = str(10) + " + " + "5" + " est égal à " + str(15)
c = 10 + int("5")
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)