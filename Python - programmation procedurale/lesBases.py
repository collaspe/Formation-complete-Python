"""
Les commandes de base
"""

print("Hello world") #Afficher du texte
nombre = input("Entrez un nombre : ") #faire saisir une valeur à l'utilisateur
prenom = input("Quel est votre prenom : ") # variable = valeur d'entrée par l'utilisateur
print("Hello world " + nombre + " vous vous appelez " + prenom)


"""
Convertir string en int
"""

a = 5
b = "10"
b = int(b) """ Il faut s'assurer de bien mettre la fonction de conversion dans la variable (ici la variable est b) """
print (a + b)


"""
Afficher le type d'une variable
"""

a = "10"
print(type(a)) """ fonction type pour savoir le type de variable """


"""
La concaténation
"""

""" On ne peut pas concatener du texte avec des nombres, donc il faut convertir le nombre en texte pour de l'affichage """
print ("Vous avez le nombre " + str(5))

""" f-string (a partir de la version 3.6 de python) -> permet d'afficher les variables sans les convertir, donc f-string à utiliser tout le temps !On peut effectuer les calculs dans un f-string """
prenom = "Paul"
f"bonjour {prenom} !"

a = 5
b = 10
f"La multiplication de {a} par {b} est égale à {a * b}"

""" concatenation avant la version 3.6 de python """
nombre = 5
"Le nombre est égal à {}".format(nombre) """ resultat -> Le nombre est égal à 5 """
"Les nombres sont égaux à {} et {}".format(5, 10)


""" Commenter du code """
#On peut faire un commentaire d'une ligne avec un dièse

"""
3 guillemets au début et a la fin pour faire un commentaire de plusieurs lignes
"""