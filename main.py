import json

chemin = r"C:\Users\BINETOU_RASSOUL\Desktop\class_projet\monfichier\mfichier.json"

print("Mon chemin est\n:",chemin)

# lire ma liste de course from mfichier.json avec la fonction open
with open(chemin,"r") as f :
    liste_course = json.load(f)


print("La liste est ==>\n",liste_course)
menu = """ 
1-Afficher la liste de course 

2-Ajouter une course 

3-Suprrimer une course  

4-Modifier une course  

5-Supprimer Toute la liste de course 

6-Quitter:
"""
liste_choix = ['1','2','3','4' ,'5','6']

while True :
    choix = input(menu)
    if choix in liste_choix:

        if choix == '1':

          with open(chemin,"r") as f:
                liste_course = json.load(f)

          print("La liste est ==>\n:", liste_course)

        elif choix == '2':
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


        # Utlisation de la fonction open pour supprimer un element a l'interieur de mfichier.json

        elif choix == '3':

            with open(chemin, "r") as f:

                liste_course = json.load(f)

            sup_course = input("Veuillez saisir la course à supprimer :")

            while not sup_course in liste_course :

                sup_course = input("Veuillez saisir une course existante svp !!!")

            liste_course.remove(sup_course)

            with open(chemin,"w") as f:
                json.dump(liste_course , f , indent=3)

            print("Course supprimer avec success !!!")



        elif choix == '4' :
            with open(chemin, "r") as f:

                liste_course = json.load(f)

            replace_course = input("Veuillez saisir la course à modifier svp!!!\n :")

            replace_course_2 = input("Veuillez saisir la course a mettre svp!!! \n")

            while len(replace_course_2) < 10 :

                replace_course_2 = input("Veuillez saisir au moins 10 caraceteres  svp!!! \n :")

            for  i in liste_course:

                if i == replace_course:

                  x = liste_course.index(i)

                #  print(x)

            liste_course[x] = replace_course_2

            with open(chemin, "w") as f:

                json.dump(liste_course, f, indent=3)

            print("modification avec success !!!")


        elif choix == '5' :

            with open(chemin, "r") as f:

                liste_course = json.load(f)

            liste_course.clear()

            with open (chemin , "w") as f :

                json.dump(liste_course , f , indent=3)

            print('La liste a ete supprime avec succes ')


        elif choix == '6' :
            print('Au revoir Bye Bye ')
            break
        else :
            print('Choix non valide ')
            break










