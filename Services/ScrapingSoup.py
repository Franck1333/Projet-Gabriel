#AIDES: Conversation avec ChatGPT. 

#INFO : >> À retravailler en consequence !!!
#Ne fonctionne pas avec l'IDE iPhone. 

import requests
from bs4 import BeautifulSoup

print("\n ***PROTOTYPE*** \n")

# URL de la page d'actualités de Le Monde
url = 'https://www.lemonde.fr/'

# Envoi d'une requête GET pour récupérer le contenu de la page
response = requests.get(url)

print(response)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Analyse du HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver et extraire les titres des articles
    headlines = soup.find_all('h3', class_='teaser__title')

    # Afficher chaque titre
    for headline in headlines:
        print(headline.text.strip())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

print("\n ***PROTOTYPE*** \n")