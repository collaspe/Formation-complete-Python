"""
Listes :

Creer une liste : 
- liste = [1,2,3,4,5]
- liste = []


On peut y mettre n'importe quelle variable
liste est un objet mutable (modifiable)

list est le mot reservé, donc à ne pas utiliser comme variable


Les tuples : 
Les tuples, c'est quasiment la même chose que les listes. La différence principale, c'est qu'on ne peut ni ajouter ni enlever d'éléments à un tuple.
Pourquoi utiliser un tuple plutôt qu'une liste alors ?
Pour des questions de rapidité, principalement !

mon_tuple = (1, 2, 3)

mon_tuple = (250, "Python", True)

Convertir tuple en list :

mon_tuple = (1, 2, 3)
liste = list(mon_tuple)
#Resultat : [1, 2, 3]
mon_tuple = tuple(liste)
#Resultat : (1, 2, 3)



Ajouter et suprimer des elements à une liste : 
Ajouter :
laListe.append(5) -> cette methode ne permet d'ajouter qu'une seule valeur à la fois
laListe.extend([10, 25, 30]) -> permet d'ajouter plusieurs elements

Supprimer : 
liste.remove(5) cette methode ne permet de supprimer que le premier 5 trouver dans la liste, si il y en a plusieurs


Recuperer un element d'une liste :
Utilisation des indices : 

laListe[0] -> premier element de la liste récupéré

ATTENTION :
On peut utiliser des indices négatifs comme -1, -2, -3 etc... et si on tape laListe[-1] on récupere le dernier element de la liste, -2 l'avant dernier et ainsi de suite

Il ne faut pas dépaser les limites de la liste -> affichage d'une erreur de python
"""

#Exercice

# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0]
nombre_dernier = nombres[-1]
 
# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = langages[1]
 
# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")

"""
Les slices : 
Permet de récuperer certains éléments de notre liste
"""

liste = ["Utilisateur_01",
         "Utilisateur_02",
         "Utilisateur_03",
         "Utilisateur_04",
         "Utilisateur_05",
         "Utilisateur_06"]

print(liste[0:1]) #Slice -> liste[0:1] : on recupere qu'un seul element car on commence de 0 et on s'arrete à 1 (le 1 n'est pas prit en compte donc on récupere pas Utilisateur_02) -> on recupere une liste
print(liste[0:2])
print(liste[1:2]) #On récupere qu'un seul element dans une liste, Utilisateur_02 donc on commence de 1 etr on termine a 2
print(liste[:]) #On récupere tout
print(liste[:-1]) #On recupere tous les utilisateurs sauf le dernier
print(liste[2:]) #On recupere l'utilisateur_03 et on recupere le reste
print(liste[:-2])
print(liste[::2]) #On va du début à la fin de la liste, et on utilise un pas, ici de 2
print(liste[1::2])  #2, 4 et 6
print(liste[1:-2:2]) #on commence a 1, on s'arrête à l'avant dernier, et on prend un pas de 2. 2 & 4
print(liste[::-1]) #Inverser l'ordre d'une liste


#Exercice
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[3:]
milieu = liste[1:-1]
premier_dernier = liste[::5]
"""
Le dernier cas de figure était un peu plus compliqué.

On voulait récupérer uniquement le premier et le dernier élément avec un slice. Je n'utilise donc aucun indice pour le début ni pour la fin, ce qui me permet de récupérer la liste au complet.

MAIS, je mets un pas de 5, qui est le nombre d'éléments dans la liste, -1. Je vais donc ainsi récupérer uniquement le premier et le dernier élément de la liste.

Pour rendre le code encore plus robuste, on pourrait utiliser la fonction len pour récupérer automatiquement la longueur de la liste et pouvoir ainsi obtenir un résultat constant peu importe la longueur de la liste :

premier_dernier = liste[::len(liste)-1]
"""
