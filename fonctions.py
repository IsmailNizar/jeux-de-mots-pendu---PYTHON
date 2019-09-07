# -*-coding:Latin-1 -*
"""Ce fichier définit des fonctions utiles pour le programme pendu."""

import os
import pickle
import random

from donnees import list_des_mots as list_des_mots
 
def recupereScores ():
    """fonction qui recupére tous les scores disponnibles"""

    if os.path.exists("score"): # Le fichier existe
        with open("score",'rb') as scoreFile :
            monpickler = pickle.Unpickler(scoreFile)
            Allscore = monpickler.load()
    else: #le fichier n'exite pas
        Allscore = {}
    return Allscore

def enregisterNouveauxScores (score):
    """fonction qui enregsitre les nouveaux scores"""

    with open("score",'wb') as scoreFile :  # On écrase les anciens scores
        monpickler = pickle.Pickler(scoreFile)
        monpickler.dump(score)
 
def recupNom ():
    """fonction qui recupére le nom d'utilisateur du joueur"""
    nom = input("Veuillez saisir votre nom:")
    nom = nom.capitalize()
    if not nom.isalnum() or len(nom)<4:
        print('Ce nom est invalide !')
        return recupNom()
    else:
        return nom       

def recupLettre ():
    """fonction qui recupére la lettre saisie du joueur"""
    lettre = input("Veuillez choisir une lettre:")
    lettre = lettre.lower()
    if len(lettre)!=1 or  not lettre.isalpha():
        print('Veuillez saisir une seul lettre !')
        return recupLettre()
    else:
        return lettre       

def choisirMot ():
    """fonction qui renvoit un mot aléatoire du liste disponnible"""

    return random.choice(list_des_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué """
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque