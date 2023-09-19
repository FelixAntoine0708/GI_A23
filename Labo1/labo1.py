"""
*   Laboratoire 1 - apprentissage Python
*   bref:   Ce laboratoire nous fait apprendre le python de base. il consiste a
*           lancer des dés qu'un utilisteur a choisie. C'est valeur de dé seront
*           afficher dans le terminal. De plus, il y a une fonction qui sert a 
*           prendre le plus avantageux ou le plus désavantageux de deux lancé.
*   Fait par: Félix-Antoine Guimont
*   Date de remise : 12 septembre 2023
"""

from random import randint
import os
from time import sleep as s

"""
*   la fonction sert a roulé les dés.
*   Aussi elle renvoie le nombre total. 
"""
def randomDice(nbOfRoll, nbOfdiceFace):
    global number

    roll = 0
    number = 0
    
    while (nbOfRoll > roll):    # pour que le nombre de lancé dépasse pas le nombre choisie par l'utilisateur
        whatGet = randint(1, nbOfdiceFace)  #la fonction qui fait le lancé
        
        number += whatGet   #addition des nombre
        roll += 1   #pour pas que le nombre de lancé dépasse 

    return number   #retourne l'addition total 

"""
*   la fonction sert a afficher les règles.
"""
def rules():
    os.system('cls')    # efface tout sur le terminal
    print ("___________________________________________________________________________________________________________")
    print ("-------------------------------------------------Game Start------------------------------------------------") 
    print ("---------------You have the choice from 2,4,6,8,10,12,20 face on your dice and 1 to 20 rolls---------------")
    print ("------------------------------Write it like this 2d6 for 2 rolls on a 6 faces------------------------------")
    print ("----You can also put adv or dis in front of the number to get the higher or the lower dice from the two----")
    print ("___________________________________________________________________________________________________________")

"""
*   fonction qui permet au utilisateur d'utiliser
*   l'interface pour écrire le nombre de dé qu'il
*   veut lancer. Aussi elle vérifie si ce que 
*   l'utilisateur à écrit pour qu'il ne crée pas 
*   d'erreur.
"""
def ui():
    global rolls
    global face
    global phrase
    global start 
    faceDice = ["2","4","6","8","10","12","20"]
    phrase = "Please enter your wanted dice roll:"
    phrase2 = "Please enter your wanted dice face:"

    print(phrase)   # affiche la phrase du nombre de dé lancé
    rolls = input() # permet au utilisateur d'écrire

    if rolls == '': # si rien est écrit  
        os.system('cls')    # efface tout sur le terminal
        print ("You can't go higher than 20 or lower than 0")   # affiche l'erreur
        print ("Retry and follow the rules")
        s(2.5)  # attend 2.5 secondes
        rolls = 0 # remet a zéro
        face = 0
        return  # quitte la fonction

    list_face = [] # création d'une list

    for x in rolls:
        list_face.append(x) # mets tout ce qu'il y a dans rolls vers la list

    if list_face[0].isalpha():  #vérifie si l'utilisateur a mis une lettre
        if list_face[0] == 'a' or list_face[0] == 'd':  #vérifie si c'est un avantage ou un désavantage
            if len(list_face) == 5: #vérifie s'il a deux chiffre 
                if list_face[3].isnumeric() and list_face[4].isnumeric():   #vérifie si c'est bien des nombres
                    combination = list_face[3] + list_face[4]   #combine les deux pour faire un chiffres
                    for x in range(len(faceDice)):
                        if combination == faceDice[x]: #vérifie si le nombre est dans ceux valide
                            face = combination  # le met dans le nombre de face
                            start = list_face[0]    #por savoir si c'est un avantage ou un désavantage
                            return #quitte la fonction

                        elif x+1 == len(faceDice):  #si le chiffre est pas bon
                            os.system('cls')    #efface tout sur le terminal
                            print ("You don't have write it correctly or put a wrong number")   #affiche l'erreur
                            print ("Retry and follow the rules")
                            s(2.5)  #attend 2.5 secondes
                            rules() # affchies les règles
                            rolls = 0   #remets a zéro
                            face = 0
                            start = 0
                            list_face.clear()
                            return 
                        
            elif len(list_face) == 4:   #vérifie s'il a un chiffre
                if list_face[3].isnumeric(): #vérifie si c'est bien un nombre
                    for x in range(len(faceDice)):
                        if list_face[3] == faceDice[x]:
                            face = list_face[3]
                            start = list_face[0]
                            return

                        elif x+1 == len(faceDice):  #si le chiffre est pas bon
                            os.system('cls')    #efface tout sur le terminal
                            print ("You don't have write it correctly or put a wrong number")   #affiche l'erreur
                            print ("Retry and follow the rules")
                            s(2.5)  #attend 2.5 secondes
                            rules() # affchies les règles
                            rolls = 0   #remets a zéro
                            face = 0
                            start = 0
                            list_face.clear()
                            return

            else:  # si c'est plus haut que trois chiffres 
                os.system('cls')    #efface tout sur le terminal
                print ("You don't have write it correctly or put a wrong number")   #affiche l'erreur
                print ("Retry and follow the rules")
                s(2.5)  #attend 2.5 secondes
                rules() # affchies les règles
                rolls = 0   #remets a zéro
                face = 0
                start = 0
                list_face.clear()

        else:   # s'il met autre choses que adv ou dis
            os.system('cls')    #efface tout sur le terminal
            print ("You put the wrong Letter")  #affiche l'erreur
            print ("Retry and follow the rules")
            s(2.5)  #attend 2.5 secondes
            rules() # affchies les règles
            rolls = 0   #remets a zéro
            face = 0
            start = 0
            list_face.clear()

    elif len(list_face) > 1:    #s'il essaie de mettre la phrase tout en une étape
        os.system('cls')    #efface tout sur le terminal
        print ("can write only one phase at the time")  #affiche l'erreur
        print ("Retry and follow the rules")
        s(2.5)  #attend 2.5 secondes
        rules() # affchies les règles
        rolls = 0   #remets a zéro
        face = 0
        start = 0
        list_face.clear()


    elif int(list_face[0]) >= 1 and int(list_face[0]) < 21: #si le chiffre est entre 1 et 20
        os.system('cls')    #efface tout sur le terminal
        rules() # affchies les règles
        print (phrase2 + list_face[0] +'d') #affiche le chiffre
        face = input()  #demande le nombre de face
        for y in faceDice:  
            if face == y:   # vérifie si le nombre de face est valide
                os.system('cls')
                rules()
                print (phrase + list_face[0] +'d'+face) #affiche les nombres que l'utilisateur a choisie
                start = list_face[0]    # dit que c'est un roulement normal
                break   #quitte la boucle

        else: #si le nombre est incorrect
            os.system('cls')    #efface tout sur le terminal
            print ("You can only choose a dice with 2,4,6,8,10,12,20 faces")    #affiche l'erreur
            print ("Retry and follow the rules")
            s(2.5)  #attend 2.5 secondes
            rules() # affchies les règles
            rolls = 0   #remets a zéro
            face = 0
            start = 0
            list_face.clear()        

    else:   #si le nombre dépasse 20 ou est en bas de 1
        os.system('cls')    #efface tout sur le terminal
        print ("You can't go higher than 20 or lower than 1")   #affiche l'erreur
        print ("Retry and follow the rules")
        s(2.5)  #attend 2.5 secondes
        rules() # affchies les règles
        rolls = 0   #remets a zéro
        face = 0
        list_face.clear()

"""
*   fonction qui roule deux dés. Puis elle va
*   mettre vérifier si c'est un désavantage 
*   ou un avantage que nous voulons afficher.
"""
def adv_dis(nbOfDiceFace):
    global number1
    global number2

    number1 = randint(1, nbOfDiceFace) 
    number2 = randint(1, nbOfDiceFace) 

    if start == 'a':    # si c'est l'avantage qui est choisi
            if number1 > number2:   # si le dé numero1 est le plus grand affiche le numéro
                print("--- " + str(number1) + " --- ( " + str(number1) + " , " + str(number2) + " )")
                s(4)    # attend 4 secondes
            
            else:   # si le dé numero2 est le plus grand affiche le numéro
                print("--- " + str(number2) + " --- ( " + str(number1) + " , " + str(number2) + " )")
                s(4)

    else:   # si c'est le désavantage qui est choisi
            if number1 > number2:   # si le dé numero2 est le plus petit affiche le numéro
                print("--- " + str(number2) + " --- ( " + str(number1) + " , " + str(number2) + " )")
                s(4)
            
            else:   # si le dé numero1 est le plus petit affiche le numéro
                print("--- " + str(number1) + " --- ( " + str(number1) + " , " + str(number2) + " )")
                s(4)
      

while(1):    
    rules() # fonction qui affiche les règles
    ui()    # fonction pour l'utilisateur

    if str(start).isalpha():    # savoir si c'est un roulement normal ou pour connaitre l'avantage
        adv_dis(int(face))  # fonction du avantage, désavantage
        rolls = 0   # remet à zéro les variables 
        face = 0

    elif rolls == 0 and face == 0:  # si il y a une erreur continue 
        continue

    else:   # si c'est pour le roulement de dé normal affiche le résultat
        result = randomDice(int(rolls), int(face))
        high = int(rolls)*int(face)
        half = high / 2
        gap = result - int(half)
        print ("R:" + str(result) + "(min: " + rolls + " , max: " + str(high) + " , ecart: " + str(gap) + " )")
        s(4)
        rolls = 0
        face = 0