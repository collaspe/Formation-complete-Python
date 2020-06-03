"""
Test d'une condition avec if
"""

age = 20
if age >= 18:
    print("Vous êtes majeur !")


"""
Les blocs d'instructions
"""
langage = "Python"
if age >= 18:
    print("Vous êtes majeur !")
    if langage == "Python": #Ce if s'executer si age est >= 18 car ce if est dans le premier if
        print("Vous pouvez rentrer")

print ("Le script est terminé")

"""
Tester plusieurs conditions :
if, elif
elif est l'équivalant de sinon si donc on doit rajouter une condition apres le elif, a ne pas confondre avec else
"""

age = 20
if age >= 18:
    print("Vous êtes majeur !")
elif age <18:
    print("Vous êtes mineur !")


"""
Tester plusieurs conditions :
if, elif, else

else est la condition qui va s'éxecuter si if et elif sont faux
"""

utilisateur = "admin"
if utilisateur == "admin":
    print("accès autorisé")
else:
    print ("accès refusé")

    
utilisateur = "root"
if utilisateur == "admin":
    print("accès autorisé")
elif utilisateur == "root":
    print("accès autorisé")
else:
    print ("accès refusé")


"""
Les opérateurs logiques
and,or,not
"""
mot_de_passe = "root"
if utilisateur == "admin":
    if mot_de_passe == "admin":
        print("Accès autorisé")

#Ici on nous retourne rien car on a pas spécifier la variable mot_de_passe
#Grace aux opérateurs logiques, on va pouvoir racourcir ces indentations

if utilisateur == "admin" and mot_de_passe == "admin":
    print("Accès autorisé")

#and est plus fort que or 

#not True -> False
#not False -> True

if not utilisateur == "admin":
    print("Accès refusé")

"""
Erreurs à eviter
"""
#ne pas enchainer les if mais bien faire if puis elif puis elif puis else