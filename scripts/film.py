from bs4 import BeautifulSoup
import requests 
import re


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

    return url_enfants


# recuprere les données sur chaque films 

url_films = get_url_films()
date = []

for film in url_films : 

    soup_film = BeautifulSoup(requests.get(str(film)).text, 'html.parser')   

    for date_html in soup_film.find_all(class_ = 'meta-body-item meta-body-info') : # pour les dates 
        regex_date =  re.findall(r"[0-9]+ [a-zA-Z]+ [0-9]+", str(date_html))
        date.append(regex_date)

print(date)
