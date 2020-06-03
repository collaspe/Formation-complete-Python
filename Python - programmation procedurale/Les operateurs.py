"""
Les opérateurs mathématiques : 
+ addition
- soustraction
* multiplication
/ division (nous retourne un nombre décimal)
% modulo (recuperer le reste d'une division)
// division entière -> nous permet de faire une division & de récuperer un nombre entier
** puissance

"""

print("Hello" + "World")
#résulat : "HelloWorld"
print("Python" * 3)
#résultat : PythonPythonPython
print(10 % 2)
#résultat : 0
print(6 % 2)
#résulat : 2
print (10 // 2)
#résultat : 5
print(10 / 3)
#résulat : 3.333333333335
print(10 // 3)
#résultat : 3
print (2 ** 4) #2⁴
#résultat : 16

#Pour utiliser d'autres fonctions de calculs plus complexes, il faut importer un module : le module math, comme ceci
import math

racine = math.sqrt(16)
print(racine)
#résulat : 4.0
"""
Ci-dessous, vous trouverez une liste non-exhaustive des fonctions les plus utilisés et disponibles dans le module math :

- math.ceil(-4.7) : entier immédiatement supérieur, donne ici -4.

- math.exp(2) : exponentielle.

- math.factorial(5) : factorielle 5, donc 120 ici (fonctionne uniquement pour les entiers positifs).

- math.floor(-4.7) : partie entière, donne ici -5.

- math.isinf(x) : teste si x est infini (inf) et renvoie True si c'est le cas.

- math.log(2) : logarithme en base naturelle.

- math.log(8, 2) : log de 8 en base 2.

- math.log10(2) : logarithme en base 10.

- math.pow(2, 3) : 2 puissance 3 (peut aussi s'écrire 2 ** 3).

- math.sqrt(16) : racine carrée, donne ici 4.

- fonctions trigonométriques : math.sin, math.cos, math.tan, math.asin, math.acos, math.atan (argument en radians).

- fonctions hyperboliques : math.sinh, math.cosh, math.tanh, math.asinh, math.acosh, math.atanh.

- math.degrees(x) : convertit de radians en degrés.

- math.radians(x) : convertit de degrés en radians.

Les constantes :

- math.pi (3.14159...)

- math.e (2.71828...)
"""


"""
Opérateur d'assignation
= -> ajouter une valeur à une variable
"""

i = 0
i = i + 1 #incrémanter de 1 i
i += 1 #incrémanter de 1 i

i += 1
i -= 1
i /= 1
i %= 1
i //= 1
i **= 1

i = 5
i += 10
print(i)
#résultat : 15

"""
Opérateurs de comparaison
<
>
<=
>=
== Egal à
!= Différent de
"""

"""
Différence entre is & ==
is -> permet de verifier si on a les mêmes objets en mémoire
== permet de verifier une égalité
"""
a = [1,2,3]
b = [1,2,3]

a == b
#résulat : true

a is b
#résultat : false (car a n'est pas un objet égal à b en mémoire)

id(a)
#résultat : une adresse mémoire (du type : 445684048)
id(b)
#résultat : une adresse mémoire (du type : 445660032)


"""
-5 et 256
Les chiffres entre -5 & 256 seront plaçés dans la même zone mémoire
"""

a = 10
b = 10
a is b
#résultat : true car a et b sont placer à la même place mémoire pour des questions d'optimisation fait par les développeurs de Python

id(a) #résulat : 445684049
id(b) #résulat : 445684049