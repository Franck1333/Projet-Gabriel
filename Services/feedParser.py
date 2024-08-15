#AIDES: Conversation avec ChatGPT.
#DOC: https://feedparser.readthedocs.io/en/latest/common-atom-elements.html
#AIDES: http://atlasflux.saynete.net/

import feedparser


def Choix_Unique():
    # URL of the RSS feed
    #OUEST-FRANCE
    #rss_url = "https://www.ouest-france.fr/rss/une"

    #BFMTV
    #Plusieurs autres flux RSS disponible sur le site
    #rss_url = "https://rmc.bfmtv.com/rss/fil-info/"

    #LE Figaro
    #Plusieurs autres flux RSS disponible sur le site
    #rss_url = "https://www.lefigaro.fr/rss/figaro_flash-actu.xml"

    #Le Parisien
    #Il n'y a que le titre et lien de disponible !
    #rss_url = "https://feeds.leparisien.fr/leparisien/rss"

    #20 Minutes
    #rss_url = "https://partner-feeds.20min.ch/rss/20minutes"

    #La Depeche
    #rss_url = "https://www.ladepeche.fr/rss.xml"

    #FranceBleu
    #rss_url = "https://www.francebleu.fr/rss/a-la-une.xml"

    #SudOuest
    #rss_url = "https://www.sudouest.fr/rss.xml"

    #CNEWS
    #Plusieurs autres flux RSS disponible sur le site
    #rss_url = "https://www.cnews.fr/rss.xml"

    #LeMonde
    #Plusieurs autres flux RSS disponible sur le site
    rss_url = "https://www.lemonde.fr/international/rss_full.xml"

    #Parse the RSS feed
    feed = feedparser.parse(rss_url)
    for i in feed.entries:
        print(i.title)
        print(i.description)
        print(i.link)
        print(i.updated)
        print(" \n ")

########################################################################################################################

def Choix_MultipleStatic():
    # Variables contenant les URLs des flux RSS
    rss_lemonde_st = "https://www.lemonde.fr/international/rss_full.xml"
    rss_cnews_st = "https://www.cnews.fr/rss.xml"
    rss_francebleu_st = "https://www.francebleu.fr/rss/a-la-une.xml"

    # Liste des URLs des flux RSS
    rss_urls = [rss_lemonde_st, rss_cnews_st, rss_francebleu_st]

    # Parcourir chaque flux RSS dans la liste
    for y in rss_urls:
        # Parser le flux RSS
        feed = feedparser.parse(y)

        print(f"Articles from: {y}")

        # Parcourir chaque entrée (article) dans le flux
        for i in feed.entries:
            print(i.title)
            print(i.description)
            print(i.link)
            print(i.updated)
            print(" \n ")

        print("##############FIN################\n")

def Choix_MultipleDynamique():
    #***SOURCES FLUX RSS***
    # Variables des flux RSS intégré
    rss_lemonde_dyn = "https://www.lemonde.fr/international/rss_full.xml"
    rss_cnews_dyn = "https://www.cnews.fr/rss.xml"
    rss_francebleu_dyn = "https://www.francebleu.fr/rss/a-la-une.xml"

    # Dictionnaire pour lier les noms des sources aux flux RSS via des clés
    rss_sources = {
        '1': rss_lemonde_dyn,
        '2': rss_cnews_dyn,
        '3': rss_francebleu_dyn
    }
    # ***SOURCES FLUX RSS***

    #***Interaction avec l'utilisateur***
    # Demander à l'utilisateur de choisir une ou plusieurs sources
    print("Choisissez une ou plusieurs sources d'actualités (séparez les choix par des virgules) :")
    print("1: Le Monde")
    print("2: CNEWS")
    print("3: France Bleu")

    # Récupérer le choix de l'utilisateur
    user_input = input("Entrez vos choix (ex: 1,2): ")

    # Convertir l'entrée en une liste de choix
    choices = user_input.split(',')
    #***Interaction avec l'utilisateur***

    # Créer une liste pour les URLs sélectionnées
    selected_rss_urls = []

    # Ajouter les URLs sélectionnées à la liste
    for choice in choices:
        choice = choice.strip()  # Enlever les espaces autour des choix
        if choice in rss_sources:
            selected_rss_urls.append(rss_sources[choice])
            # Ajout des flux choisis dans une nouvelle liste, en concordant le dictionnaire et la liste des choix de l'user à chaque itération FOR/in.
        else:
            print(f"Choix invalide: {choice}")

    # Afficher les URLs sélectionnées
    print("\nVous avez sélectionné les sources suivantes :")
    for url in selected_rss_urls:
        print(url + "\n")

    # Parcourir chaque flux RSS sélectionné par l'utilisateur
    for rss_url in selected_rss_urls:
        # Parser le flux RSS
        feed = feedparser.parse(rss_url)

        #print(f"\nArticles from: {rss_url}")

        # Initialiser le compteur
        compteurArticle = 0

        # Parcourir chaque entrée (article) dans le flux
        for i in feed.entries:
            compteurArticle += 1

            print("Article N° " + str(compteurArticle))
            print(i.title)
            print(i.description)
            print(i.link)
            print(i.updated)
            # Vérifier s'il y a un lien d'image dans le flux
            if 'media_content' in i:
                for media in i.media_content:
                    print("Image :", media['url'])
            elif 'media_thumbnail' in i:
                for thumbnail in i.media_thumbnail:
                    print("Image :", thumbnail['url'])
            elif 'enclosures' in i:
                for enclosure in i.enclosures:
                    print("Image :", enclosure['url'])
            else:
                print("Pas d'image trouvée.")
            print(" \n ")
        print("##############FIN################\n")

if __name__ == "__main__":
    print("\n ***PROTOTYPE*** \n")

    #Choix_Unique()
    #Choix_MultipleStatic()
    Choix_MultipleDynamique()

    print("\n ***PROTOTYPE*** \n")