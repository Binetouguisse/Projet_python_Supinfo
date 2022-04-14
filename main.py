import json

chemin = r"C:\Users\BINETOU_RASSOUL\Desktop\class_projet\monfichier\mfichier.json"

print("Mon chemin est\n:",chemin)

# lire ma liste de course from mfichier.json avec la fonction open
with open(chemin,"r") as f :
    liste_course = json.load(f)


print("La liste est ==>\n",liste_course)
menu = """ 
1-Ajouter une course 

2-Suprrimer une course  

3-Modifier une course  

4-Supprimer Toute la liste de course 

5-Quitter:
"""
liste_choix = ['1','2','3','4' ,'5']

while True :
    choix = input(menu)
    if choix in liste_choix :
        if choix == '1':
            ajout_course = input("Veuillez saisir la liste à ajouter :")

            while len(ajout_course) < 10 :

                ajout_course = input("Veuillez saisir au moins 10 caracteres ")

            #Recuperation de mes datas from mfichier.json
            # La fonction dump() nous permet d'ecrire a linterieur d'un fichier json
            with open(chemin , "r") as f :

                liste_course = json.load(f)

            liste_course.append(ajout_course)

            with open(chemin , "w") as f :

                json.dump(liste_course,f,indent=3)

            print("Ajout de course reussi")
            break

        # Utlisation de la fonction open pour supprimer un element a l'interieur de mfichier.json

        elif choix == '2':

            with open(chemin, "r") as f:

                liste_course = json.load(f)

            sup_course = input("Veuillez saisir la course à supprimer :")

            while not sup_course in liste_course :

                sup_course = input("Veuillez saisir une course existante svp !!!")

            liste_course.remove(sup_course)

            with open(chemin,"w") as f:
                json.dump(liste_course , f , indent=3)

            print("Course supprimer avec success !!!")

            break

        elif choix == '3' :

            replace_course = input("Veuillez saisir la course à modifier svp!!!\n :")

            replace_course_2 = input("Veuillez saisir la course a mettre svp!!! \n")

            while len(replace_course_2) < 10 :

                replace_course_2 = input("Veuillez saisir au moins 10 caraceteres  svp!!! \n :")

            for  i in liste_course:

                if i == replace_course:

                  x = liste_course.index(i)

                #  print(x)

            liste_course[x] = replace_course_2

            print("modification avec success !!!")

            break
        elif choix == '4' :
            with open(chemin, "r") as f:
                liste_course = json.load(f)
                liste_course.clear()
                print('La liste a ete supprime avec succes ')
                break
        elif choix == '5' :
            print('Au revoir Bye Bye ')
            break
        else :
            print('Choix non valide ')
            break
print("La liste est ==>\n:",liste_course)









