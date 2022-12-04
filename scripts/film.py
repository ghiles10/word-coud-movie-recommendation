from bs4 import BeautifulSoup
import requests 
import re
import pprint

# récuperer les liens des pages des films 
def get_url_films() : 

    # pour stocker les url des pages web des films 
    url_enfants = []

    for page in range(1,2): 

        url_page = f"https://www.allocine.fr/films/?page={page}"
        soup = BeautifulSoup(requests.get(url_page).text, 'html.parser')

        for titre in soup.find_all(class_ = "meta-title-link") : # avoir les liens
            if "href" in str(titre) : 
                regex_url = re.search(r'href="(.*)"', str(titre)).groups()[0]
                url_enfants.append('http://allocine.fr'+regex_url)

    return set(url_enfants) 


# recuperer les données sur chaque films 
def get_donnees_film(func) : 

    url_films = func()
    donnees_film = {} 

    for film in url_films : 
        soup_film = BeautifulSoup(requests.get(str(film)).text, 'html.parser') 

        # recupération des titres 
        for titre_html in soup_film.find_all(class_ = 'titlebar-title titlebar-title-lg') : 
            donnees_film[titre_html.text] = []

        for date_html in soup_film.find_all(class_ = 'meta-body-item meta-body-info') :

            # recupération des dates 
            regex_date =  re.findall(r"[0-9]+ [a-zA-Z]+ [0-9]+", str(date_html))[0]
            donnees_film[titre_html.text].append(regex_date)

            # récupération de la durée 
            regex_duree = re.findall(r"[0-9]{1,3}h [0-9]+min", str(date_html))[0]
            donnees_film[titre_html.text].append(regex_duree)

            # récupération dy type de films 
            regex_type =  re.findall(r">([a-zA-Z éè]+)<", str(date_html)) 
            donnees_film[titre_html.text].append(regex_type)

    return donnees_film 



pprint.pprint((get_donnees_film(get_url_films)))


