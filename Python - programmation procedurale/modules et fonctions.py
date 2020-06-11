"""
Appeler un module : 

import random

utiliser ce module : 

random.fonctionDemandée

"""

import random

r = random.randint(0, 1) #genere un nombre entier aléatoire entre 0 et 1 (donc soit 0 ou 1 du coup)
print(r)

u = random.uniform(0, 1) #genere un nombre float aléatoire entre 0 & 1
print(r)

randrange = random.randrange(999) #Genere aléatoirement un nombre entier entre 0 & 999 (donc pas 999)
print(randrange)

randrange2 = random.randrange(0, 101, 10) #Genera aléatoirement un nombre entier entre 0 & 101 (mais pas 101) avec un pas de 10
print(randrange2)


"""
Module os

sert à manipuler des dossiers

"""

import os

#Creer un dossier
chemin = "/media/collaspe/HDD 1Tb/Work/Development/Soft Development/Python/Formation complete Python/"
dossier = os.path.join(chemin, "dossier", "sous dossier")
print(dossier)

if not os.path.exists(dossier): #Si le dossier n'existe pas, alors il faut le creer
    os.makedirs(dossier) #Permet de creer les dossiers & sous dossiers (ne pas utiliser la fonction mkdir)
else:
    print("Dossier déjà existant")

os.makedirs(dossier, exist_ok=True) #Alternative à la condition du if, on peut faire comme ça aussi, si le dossier existe alors ça nous affiche pas de message d'erreur

#Supprimer un dossier
os.removedirs(dossier)

#Si le dossier n'existe pas, il renvoit une erreur. L'argument exist_ok=True n'existe pas

if os.path.exists(dossier): #Si le dossier existe
    os.removedirs(dossier)    
else:
    print("Dossier déjà supprimé, il n'existe plus")


"""
Fonction dir & help

afficher les fonctions qu'on peut utiliser dans chaque module
"""

import random
from pprint import pprint #On importe la fonction pprint du module pprint, juste une seule fonction

print(dir(random)) #Affiche toutes les fonctions utilisables
#help(random.randint) #Afficher l'aide de la fonction utilisée, pas besoin de mettre les () a la fin de la fonction
pprint(dir(random)) #affiche le dir mais mieux classé


"""
Les objets callable
"""

import pprint

print(callable(pprint)) #Retourne false car pprint n'est pas appelable car c'est un module et non une fonction


from pprint import pprint

print(callable(pprint)) #Retourne true car pprint est appelable, c'est une fonction

import os
print(callable(os.name)) #Return false car name est pas une fonction mais une valeur (chaine de caractere)