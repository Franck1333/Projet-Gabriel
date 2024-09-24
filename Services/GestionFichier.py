# AIDES: Conversation avec ChatGPT.
# AIDES: https://ioflood.com/blog/python-create-file/
# AIDES: https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python
# AIDES: https://www.freecodecamp.org/news/file-handling-in-python/
# AIDES: https://www.geeksforgeeks.org/get-file-size-in-bytes-kb-mb-and-gb-using-python/
# AIDES: https://www.geeksforgeeks.org/creating-pdf-documents-with-python/

########################################################################################################################
# Libs global.
import os  # Lib pour interagir avec le SE.
import time  # Lib pour obtenir date-heure.
import codecs  # Lib pour encoder les fichiers.
import datetime  # Lib pour obtenir date-heure.
import feedparser  # Lib pour télécharger les flux RSS.
#######################################################
# Lib "reportlab" et ses imports pour la création d'un rapport en format PDF.
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


########################################################################################################################

def temps_actuel():
    # OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE
    # -- DEBUT -- Jour, Mois, Année, Heure, Minute, Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime("%d-%m-%Y-%H_%M_%S")
    #print(("Voici l'horloge système:", system_time))
    return system_time
    # -- FIN -- Jour, Mois, Année, Heure, Minute, Seconde


def GenerationRapportTXT():
    # Expérimentation des méthodes permettant de générer un fichier.
    # Flux RSS de FranceBleu
    rss_url = "https://www.cnews.fr/rss.xml"
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)  # Décodage du flux RSS par la lib feedParser.
    ################################################

    # // Création du repertoire dédié aux rapports \\.
    base_dir = os.getcwd()  # Obtenir le répertoire de travail actuel.
    # Définir le chemin du dossier "Rapports" dans le repertoire actuel.
    rapport_dir = os.path.join(base_dir, "Rapports")
    # Créer le dossier "Rapports" s'il n'existe pas déjà.
    if not os.path.exists(rapport_dir):
        os.makedirs(rapport_dir)

    timeNAME = temps_actuel()  # Enregistrement de l'horloge système.
    # Définir le chemin complet du nouveau fichier
    chemin = os.path.join(rapport_dir, "RapportRSStexte_" + timeNAME + ".txt")
    # print(chemin + "\n")

    # Création d'un fichier ".txt" avec le mode écriture&modification et l'encodage UTF-8.
    file = codecs.open(chemin, "w+", "utf-8")
    ################################################
    for i in feed.entries:  # Pour chaque article, retrouvé les champs associés.
        print(i.title)
        print(i.description)
        print(i.link)
        print(i.updated)
        print(" \n ")
        ###########################################
        file.writelines(" \n ")  # Méthode permettant de créer une nouvelle ligne dans le fichier créé.
        file.write(i.title)  # Méthode permettant de créer une nouvelle ligne dans le fichier créé.
        ###########################################
        file.writelines(
            ' \n ')  # "This function inserts multiple strings at the same time", "A list of string elements is created".
        file.write(i.description)  # "This function inserts the string into the text file on a single line".
        ###########################################
        file.writelines(' \n ')
        file.write(i.link)
        ###########################################
        file.writelines(' \n ')
        file.write(i.updated)
        ###########################################
        file.writelines(' \n ')
        file.write(" \n ")
    file.close()  # Méthode permettant de fermer le fichier créé.
    size = os.path.getsize(chemin)  # Méthode permettant de connaitre la taille du fichier créé.
    size = size / 1024  # Division par 1024 pour obtenir le résultat en Kilo-octet.
    print(f' La taille du nouveau rapport texte est de {size} octets.')  # Affichage de la variable {}.
    ################################################
    return 0


def GenerationRapportPDF():
    # Ce code a été généré avec l'aide d'une IA, ChatGPT, pour créer un rapport PDF en utilisant le flux RSS.

    # Récupération du flux RSS à partir de l'URL de CNews
    rss_url = "https://www.cnews.fr/rss.xml"
    feed = feedparser.parse(rss_url)  # Décodage du flux RSS avec feedparser

    # Obtenir le répertoire de travail actuel et créer un dossier "Rapports"
    base_dir = os.getcwd()  # Obtient le chemin du répertoire actuel
    rapport_dir = os.path.join(base_dir, "Rapports")  # Crée le chemin pour le dossier "Rapports"
    if not os.path.exists(rapport_dir):  # Si le dossier n'existe pas, le créer
        os.makedirs(rapport_dir)

    # Génération d'un nom de fichier PDF basé sur l'horloge système
    timeNAME = temps_actuel()  # Fonction qui renvoie l'heure actuelle (non définie ici)
    cheminPDF = os.path.join(rapport_dir, "RapportRSSpdf_" + timeNAME + ".pdf")  # Définir le chemin du fichier PDF

    # Création d'un objet PDF avec une page A4
    pdf = canvas.Canvas(cheminPDF, pagesize=A4)
    document_title = 'Rapport RSS du ' + timeNAME  # Titre du document
    pdf.setTitle(document_title)  # Définir le titre du PDF

    # Enregistrement d'une police externe pour utilisation
    font_path = 'Gill_Sans_MT.TTF'  # Chemin de la police
    font_name = 'GillSans'  # Nom à utiliser pour la police
    pdfmetrics.registerFont(TTFont(font_name, font_path))  # Enregistrer la police dans le PDF

    # Initialisation de la position Y de départ pour les articles
    y_position = 800  # Position de départ en haut de la page

    # Largeur maximale pour le texte sur une ligne
    max_width = 450  # En points (une page A4 fait 595 points de large)

    # Fonction pour découper le texte en lignes de taille maximale
    # noinspection PyShadowingNames
    def wrap_text(text, font_name, font_size, max_width, pdf):
        wrapped_lines = []  # Liste pour stocker les lignes découpées
        words = text.split()  # Découpe le texte en mots
        line = ""  # Chaîne vide pour accumuler chaque ligne

        # Parcours de chaque mot pour tester s'il rentre dans la largeur maximale
        for word in words:
            test_line = f"{line} {word}".strip()  # Teste si on peut ajouter le mot à la ligne courante
            if pdf.stringWidth(test_line, font_name, font_size) <= max_width:  # Vérifie la largeur de la ligne
                line = test_line  # Si oui, on l'ajoute
            else:
                wrapped_lines.append(line)  # Sinon, on sauvegarde la ligne et commence une nouvelle
                line = word  # Le mot qui dépasse devient la première ligne suivante
        wrapped_lines.append(line)  # Ajouter la dernière ligne qui restait

        return wrapped_lines  # Retourne toutes les lignes découpées

    # Boucle pour parcourir chaque article du flux RSS
    for i in feed.entries:
        # Création d'un bloc de texte contenant les informations de chaque article
        article_text = f"Titre : {i.title}\nDescription : {i.description}\nDate : {i.updated}"

        # Création d'un objet texte pour gérer les retours à la ligne dans le PDF
        text_object = pdf.beginText(100, y_position)  # Commence à la position (100, y_position) sur la page
        text_object.setFont(font_name, 12)  # Définit la police et la taille pour ce texte

        # Découper le texte en lignes pour qu'il ne dépasse pas la largeur maximale
        wrapped_lines = wrap_text(article_text, font_name, 12, max_width, pdf)
        for wrapped_line in wrapped_lines:
            if y_position < 50:  # Si on atteint le bas de la page, créer une nouvelle page
                pdf.showPage()  # Crée une nouvelle page
                y_position = 800  # Réinitialiser la position Y en haut de la nouvelle page
                text_object = pdf.beginText(100, y_position)  # Recommence un nouveau bloc de texte
                text_object.setFont(font_name, 12)
            text_object.textLine(wrapped_line)  # Ajouter la ligne au texte
            y_position -= 20  # Baisse la position Y pour la ligne suivante

        # Dessiner le bloc de texte sur le PDF
        pdf.drawText(text_object)

        # Gestion de l'URL complète de l'article
        full_link = i.link  # Récupérer l'URL complète
        link_text = "Lien: " + full_link  # Ajouter "Lien:" suivi de l'URL

        # Si l'URL peut tenir sur une seule ligne, l'ajouter
        if pdf.stringWidth(link_text, font_name, 12) <= max_width:
            pdf.drawString(100, y_position, link_text)  # Affiche le lien
            # Créer une zone cliquable avec le lien complet
            pdf.linkURL(full_link, (100 + pdf.stringWidth("Lien: ", font_name, 12), y_position, 100 + pdf.stringWidth(link_text, font_name, 12), y_position + 15), relative=0)
            y_position -= 20  # Baisse la position Y après le lien
        else:
            # Si l'URL est trop longue, afficher "Lien:" d'abord
            pdf.drawString(100, y_position, "Lien: ")
            link_x_position = 100 + pdf.stringWidth("Lien: ", font_name, 12)  # Position après "Lien:"
            link_lines = wrap_text(full_link, font_name, 12, max_width - link_x_position, pdf)  # Découper l'URL sur plusieurs lignes

            # Afficher chaque ligne de l'URL découpée
            for link_line in link_lines:
                if y_position < 50:  # Si on atteint le bas de la page, créer une nouvelle page
                    pdf.showPage()  # Crée une nouvelle page
                    y_position = 800
                pdf.drawString(link_x_position, y_position, link_line)  # Affiche chaque partie du lien
                pdf.linkURL(full_link, (link_x_position, y_position, link_x_position + pdf.stringWidth(link_line, font_name, 12), y_position + 15), relative=0)  # Crée une zone cliquable pour chaque ligne
                link_x_position = 100  # Pour les lignes suivantes, revenir à 100
                y_position -= 20  # Baisse la position Y pour la ligne suivante

        # Ajoute un espace supplémentaire entre les articles
        y_position -= 40

    # Sauvegarder le fichier PDF
    pdf.save()

    # Affichage de la taille du fichier PDF créé
    size = os.path.getsize(cheminPDF)  # Obtenir la taille du fichier en octets
    size = size / 1024  # Convertir en kilo-octets
    print(f'La taille du nouveau rapport PDF est de {size} octets.')



if __name__ == "__main__":
    print("\n ***PROTOTYPE*** \n")
    #temps_actuel()
    GenerationRapportTXT()  # Expérimentation des méthodes permettant de générer un fichier texte.
    GenerationRapportPDF()  # Expérimentation des méthodes permettant de générer un fichier PDF.
    print("\n ***PROTOTYPE*** \n")
