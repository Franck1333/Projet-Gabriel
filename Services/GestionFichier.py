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
    rss_url = "https://www.francebleu.fr/rss/a-la-une.xml"
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
    # Most of this function is made by ChatGPT.
    # Flux RSS de FranceBleu
    rss_url = "https://www.francebleu.fr/rss/a-la-une.xml"
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)  # Décodage du flux RSS par la lib feedParser.

    ################################################
    # // Création du repertoire dédié aux rapports \\.
    base_dir = os.getcwd()  # Obtenir le répertoire de travail actuel
    rapport_dir = os.path.join(base_dir, "Rapports")  # Définir le chemin du dossier "Rapports"
    # Créer le dossier "Rapports" s'il n'existe pas déjà
    if not os.path.exists(rapport_dir):
        os.makedirs(rapport_dir)

    timeNAME = temps_actuel()  # Enregistrement de l'horloge système.
    cheminPDF = os.path.join(rapport_dir, "RapportRSSpdf_" + timeNAME + ".pdf")  # Définir le chemin complet du fichier
    # print(cheminPDF + "\n")

    # Création de l'objet PDF avec une page A4
    pdf = canvas.Canvas(cheminPDF, pagesize=A4)
    document_title = 'Rapport RSS du ' + timeNAME
    pdf.setTitle(document_title)
    # Enregistrement de la police externe
    font_path = 'Gill_Sans_MT.TTF'
    font_name = 'GillSans'
    pdfmetrics.registerFont(TTFont(font_name, font_path))

    # Initialisation de la position Y de départ pour le premier article
    y_position = 800  # Position de départ en haut de la page

    # Largeur maximale pour le texte
    max_width = 450  # En points (A4 a une largeur de 595 points)

    # Boucle principale pour parcourir les articles du flux RSS
    for i in feed.entries:
        # Regroupement des champs de l'article dans une liste
        text_lines = [
            i.title,
            i.description,
            i.link,
            i.updated,
            " "  # Ajouter un espace vide pour séparer les articles
        ]

        # Utilisation d'un TextObject pour gérer les retours à la ligne
        text_object = pdf.beginText(100, y_position)  # Commence à la position (x, y)
        text_object.setFont(font_name, 12)

        # Fonction pour découper le texte en lignes de taille maximale
        def wrap_text(text, font_name, font_size, max_width, pdf):
            wrapped_lines = []
            words = text.split()
            line = ""

            for word in words:
                test_line = f"{line} {word}".strip()
                if pdf.stringWidth(test_line, font_name, font_size) <= max_width:
                    line = test_line
                else:
                    wrapped_lines.append(line)
                    line = word
            wrapped_lines.append(line)

            return wrapped_lines
        # Ajouter chaque ligne de texte au TextObject
        for line in text_lines:
            wrapped_lines = wrap_text(line, font_name, 12, max_width, pdf)  # Découper les lignes qui sont trop longues
            for wrapped_line in wrapped_lines:
                if y_position < 50:  # Si la position y est trop basse, passer à une nouvelle page
                    pdf.showPage()  # Créer une nouvelle page
                    y_position = 800  # Réinitialiser la position y en haut de la nouvelle page
                    text_object = pdf.beginText(100, y_position)
                    text_object.setFont(font_name, 12)
                text_object.textLine(wrapped_line)  # Ajoute la ligne au TextObject
                y_position -= 20  # Déplacer la position y vers le bas pour la ligne suivante

        # Dessine le TextObject sur le PDF
        pdf.drawText(text_object)

    # Sauvegarde du PDF
    pdf.save()
    size = os.path.getsize(cheminPDF)  # Méthode permettant de connaitre la taille du fichier créé.
    size = size / 1024  # Division par 1024 pour obtenir le résultat en Kilo-octet.
    print(f' La taille du nouveau rapport PDF est de {size} octets.')  # Affichage de la variable {}.


if __name__ == "__main__":
    print("\n ***PROTOTYPE*** \n")
    #temps_actuel()
    GenerationRapportTXT()  # Expérimentation des méthodes permettant de générer un fichier texte.
    GenerationRapportPDF()  # Expérimentation des méthodes permettant de générer un fichier PDF.
    print("\n ***PROTOTYPE*** \n")
