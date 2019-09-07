# -*-coding:Latin-1 -*

import os
import fonctions
import donnees
#on récupére tous les scores
AllScores = fonctions.recupereScores()

#on récupére le nom du joueur
nom = fonctions.recupNom()

#si le joueur n'a pas de score alors on ajoute 
if nom not in AllScores.keys():
    AllScores[nom]=0

continue_partie = True
while continue_partie:
    print("Le joueur {} : {} point(s)".format(nom,AllScores[nom]))
    mot_choisi = fonctions.choisirMot() #on choisie une mot aléatoire du liste disponnible
    lettres_trouvees = []
    lettres_essayees = []
    mot_trouve = fonctions.recup_mot_masque(mot_choisi,lettres_trouvees) #on récupére le mot masqué
    nb_coups = donnees.nb_coups
    while mot_choisi != mot_trouve and nb_coups > 0:
        print("Le mot trouvee : {} et il vous reste encore {} chance(s)".format(mot_trouve,nb_coups))
        lettre = fonctions.recupLettre()
        if  lettre in lettres_trouvees :
            print("Vous avez deja trouvee cette lettre !") #la lettre a déja été choisie
        elif lettre in lettres_essayees :
            print("Vous avez deja essayee cette lettre ! essaye à nouveau ...") #la lettre à déja été essayé
        elif lettre in mot_choisi :
            lettres_trouvees.append(lettre) #on ajoute la lettre trouvée au liste des lettres trouvées
            print('Bien jouee vous avez choisi la bonne lettre')
        else:
            nb_coups -= 1 #On decrimente le nb de coups 
            print('Ohh non ! Cette lettre ne se trouve pas dans cette mot ....')
        lettres_essayees.append(lettre)
        mot_trouve = fonctions.recup_mot_masque(mot_choisi,lettres_trouvees) #on récupére le mot masqué
    if mot_trouve == mot_choisi :
        print("Felicitations, vous venez de trouve le mot {}".format(mot_trouve)) # le mot a été trouvée avec success
    else:
        print("Dzl, vous avez perdu.") # le mot n'as pas été trouvée échoue
        print("le mot ete {}".format(mot_choisi))

    AllScores[nom] +=nb_coups # le nb de coups restant seront ajoutée au score du joueur

    continue_p = input("vous voulez continuer la partie (o/n) ?")
    if continue_p.lower() !="o": # Si la reponse est diff de Oui
        fonctions.enregisterNouveauxScores(AllScores)  # on enregistre le nouveau score
        print("Vous quittez la parti avec un score :", AllScores[nom])
        continue_partie = False

os.system("pause")