#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ROCHAT_FRANCK
#---------------------------------------Importante LIB---------------------------------------
import datetime  #Bibliotheque permettant d'obtenir la date
import time  #Bibliotheque permettant d'obtenir la date
from tkinter import *  #Bibliotheque permettant d'obtenir Tkinter(G.U.I)
from tkinter import Tk, Label  #Bibliotheque permettant d'obtenir Tkinter(G.U.I
import psutil  #Bibliotheque permettant d'obtenir des infos systèmes
#---------------------------------------Importante LIB---------------------------------------
#-----------------------------------------------------Localisation de l'emplacement des fichiers nécessaires-----------------------------------------------------
print(
    "\n Bonjour/Bonsoir, ne pas faire fonctionner ce programme en utilisant les droits/commandes administrateur si l'utilisateur n'est pas l'Admin au quel cas le programme ne fonctionnera pas correctement. \n")  #Information à lire dans la console
#...
#-----------------------------------------------------Localisation de l'emplacement des fichiers nécessaires-----------------------------------------------------
#-------------Fenetre Maitre-------------
fenetre: Tk = Tk()  #Creation d'une fenêtre Maîtresse TK appelé "fenêtre"
fenetre.title('Projet GABRIEL')
#-------------Fenetre Maitre-------------
#-------------------------------------------------------------------Contenue Fenetre Principale-------------------------------------------------------------------
#------------------------------------------------------------------------------     #Affichage du Temps HEURES/MINUTES/SECONDES
def temps_actuel():
    #OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print(("Voici l'heure:", system_time))
    return system_time
    #-- FIN -- Heure,Minute,Seconde
#---------------------------------------------

status_temps_actuel = Label(fenetre, text=temps_actuel())  #Affichage du Temps (Label)
status_temps_actuel.pack()  #Pour obtenir un affichage dynamique, il faut utiliser pack/grid de cette façon

#---------------------------------------------
def update_temps_actuel():  #Fonctionnalité permettant de mettre à jour l'Heure en fonction du Temps Réel
    # On met à jour le temps actuel dans le champ text du Widget LABEL pour afficher l'heure
    status_temps_actuel["text"] = temps_actuel()
    # Après une seconde, on met à jour le contenu text du LABEL
    fenetre.after(1000, update_temps_actuel)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# noinspection PyGlobalUndefined
def information_Materiel():
    #Obtention des Informations Materiel de l'Ordinateur
    global tk_UtilisationCPU
    global tk_tk_diskUsage
    global tk_MemoireUtilise
    #--        
    UtilisationCPU = "0%"  #Obtention du Niveau d'utilisation du Processeur.
    MemoireUtilise = "0%"  #Obtention d'information par rapport à la Memoire Vive.
    tk_diskUsage = "0%"  #Obtention de la Temperature du Package Processeur/GPU.
    #--
    #--Affichage--
    EnveloppeInfoMateriel = LabelFrame(fenetre, text="Informations Relatives aux Matériels", padx=5,
                                       pady=5)  #Création d'une "Zone Frame" à Label
    EnveloppeInfoMateriel.pack(fill="both", expand=0)  #Position de la "Zone Frame" à Label dans la fenêtre
    tk_UtilisationCPU = Label(EnveloppeInfoMateriel, text=UtilisationCPU)
    tk_MemoireUtilise = Label(EnveloppeInfoMateriel, text=MemoireUtilise)
    tk_tk_diskUsage = Label(EnveloppeInfoMateriel, text=tk_diskUsage)
    tk_UtilisationCPU.pack()
    tk_MemoireUtilise.pack()
    tk_tk_diskUsage.pack()
    #--Affichage--
def update_information_Materiel():
    UtilisationCPU = psutil.cpu_percent(interval=None)
    MemoireUtilise = psutil.virtual_memory()[2]
    diskUsage = psutil.disk_usage('/').percent

    #Mise à Jour des Informations à propos du Materiel
    tk_UtilisationCPU["text"] = "Utilisation du Processeur: " + str(UtilisationCPU) + " %"
    tk_MemoireUtilise["text"] = "Memoire Vive Utilise: " + str(MemoireUtilise) + " %"
    tk_tk_diskUsage["text"] = "Utilisation du disque: " + str(diskUsage) + " %"

    #Après une seconde, on met à jour le contenu text du LABEL
    fenetre.after(1000, update_information_Materiel)
#---
information_Materiel()  #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def information_Complementaire():
    #Recuperation des Informations
    INFOS_SUPP = "Aucune Informations Supp. à afficher pour le moment."

    #--Affichage--
    EnveloppeInfoComplementaire = LabelFrame(fenetre, text="Informations Complémentaires", padx=5,
                                             pady=5)  #Création d'une "Zone Frame" à Label
    EnveloppeInfoComplementaire.pack(fill="both", expand=0)
    #---Affichage Infos---
    tk_info_supp = Label(EnveloppeInfoComplementaire, text=INFOS_SUPP)
    tk_info_supp.pack()

    #---Affichage Infos---    
    #--Affichage--
    def update_information_Complementaire():
        #Mise à Jour des Informations reçues
        tk_info_supp["text"] = INFOS_SUPP
        #Après 2,16 minutes, on met à jour le contenu text du LABEL
        fenetre.after(13000, update_information_Complementaire)
    #---
information_Complementaire()  #Lancement de la Fonctionnalitée.
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# noinspection PyTypeChecker
def Fonctionnalitee_1():
    print("Fonctionnalitée 1")

    #Etape-1 On Declare la fenêtre
    #global fonct_1
    fonct_1 = Toplevel()

    #Etape-2 On récupère les informations à afficher
    Informations = "Voici la fonctionnalitee numéro #1"
    print(Informations)
    #Etape-3 On fait la mise en page des Informations réceptionner
    #Zone d'affichage
    EnveloppeFonction1 = LabelFrame(fonct_1, text="Emplacement dédié a l'information", padx=5,
                                    pady=5)  #Création d'une "Zone Frame" à Label
    EnveloppeFonction1.pack(fill="both", expand=0)  #Position de la "Zone Frame" à Label dans la fenêtre

    Chocolat = Label(EnveloppeFonction1, text="Chocolat")
    Noisette = Label(EnveloppeFonction1, text="Noisette")
    Lait = Label(EnveloppeFonction1, text="Lait")
    Vitamine = Label(EnveloppeFonction1, text="Vitamine")

    #Etape-4 Indication de l'Emplacement des Informations dans l'Interface
    Chocolat.pack()
    Noisette.pack()
    Lait.pack()
    Vitamine.pack()

    #Etape-5 Bouton(s)
    Button(fonct_1, text="Fermer", command=fonct_1.destroy).pack()  #Bouton de Fermeture de la fenêtre actuelle
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Fonctionnalitee_2():
    print("Fonctionnalitée 2")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def Fonctionnalitee_3():
    print("Fonctionnalitée 3")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
Button(fenetre, text="Fonctionnalitée 1", command=Fonctionnalitee_1).pack()  #Bouton
Button(fenetre, text="Fonctionnalitée 2", command=Fonctionnalitee_2).pack()  #Bouton
Button(fenetre, text="Fonctionnalitée 3", command=Fonctionnalitee_3).pack()  #Bouton
Button(fenetre, text="Fermer", command=fenetre.destroy).pack()  #Bouton de Fermeture de la fenêtre Principale
#-------------------------------------------------------------------Contenue fenêtre Secondaires-------------------------------------------------------------------
if __name__ == "__main__":
    # noinspection PyBroadException
    try:
        #clear_cache()
        #-------------------------------------------------------------------Démarrage des fonctions operant sur la fenêtre Principale-------------------------------------------------------------------
        #Récupération des informations pour la Mise à jour du LABEL toute les 1 milliseconde quand la fenêtre Maitre est lancée
        fenetre.after(1, update_temps_actuel)  #update_temps_actuel()
        fenetre.after(1, update_information_Materiel)  #update_information_Materiel()
        #fenetre.after(1, update_information_Complementaire) #update_information_Complementaire()
        fenetre.mainloop()  #Boucle de Lancement de la Fenêtre PRINCIPAL
        #-------------------------------------------------------------------Démarrage des fonctions operant sur la fenêtre Principale---------------------------------------------------------------
        pass

    #---!!!GESTION DES ERREURS!!!---
    #Utiliser uniquement quand le produit est finalisé et/ou commenter les lignes durant le development pour determiner les bugs.
    #except TypeError:
    # print("Code Erreur: TypeError")
    #except KeyError:
    # print("Code Erreur: KeyError")
    #except ValueError:
    # print("Code Erreur: ValueError")
    #except AssertionError:
    # print("Code Erreur: AssertionError")
    #except NameError:
    # print("Il est nécessaire de redémarrer le programme !") #On affiche ce message dans la console
    # print("Code Erreur: NameError")
    except:
        print("Il est nécessaire de redémarrer le Logiciel!")  #On affiche ce message dans la console
        print("Code Erreur: Aucun")
        #---!!!GESTION DES ERREURS!!!---