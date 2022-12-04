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
    # avis_film = {}

    for film in url_films : 
        soup_film = BeautifulSoup(requests.get(str(film)).text, 'html.parser') 

        # recupération des titres 
        for titre_html in soup_film.find_all(class_ = 'titlebar-title titlebar-title-lg') : 
            donnees_film[titre_html.text] = []

        for info_film in soup_film.find_all(class_ = 'meta-body-item meta-body-info') :

            # recupération des dates 
            regex_date =  re.findall(r"[0-9]+ [a-zA-Z]+ [0-9]+", str(info_film))[0]
            donnees_film[titre_html.text].append(regex_date)

            # récupération de la durée 
            regex_duree = re.findall(r"[0-9]{1,3}h [0-9]+min", str(info_film))[0]
            donnees_film[titre_html.text].append(regex_duree)

            # récupération dy type de films 
            regex_type =  re.findall(r">([a-zA-Z éè]+)<", str(info_film)) 
            donnees_film[titre_html.text].append(regex_type)

    return donnees_film 

# pprint.pprint((get_donnees_film(get_url_films)))
    
####récupérer les avis et la note                               

def get_avis(func) : 

    url_films = func()     
    avis = []     # stocker la note moyenne et le nb d'avis                

    liens_avis = []  # afin de stocker les liens des films contenant les avis 
    for film in url_films :     
        soup_film = BeautifulSoup(requests.get(str(film)).content, 'html.parser')   

        # récupération des liens des avis dans la liste liens_avis
        for page_avis in soup_film.find_all(class_="end-section-link") : 
        
            # récupération du lien avis         
            regex_avis =  re.findall(r'href="(/.*/critiques/spectateurs/)', str(page_avis))  

            if len(regex_avis) > 0 :    
                lien_avis = "http://allocine.fr" + regex_avis[0]     
                liens_avis.append(lien_avis)  

    # entrer dans les liens des avis                    
    for url_avis in liens_avis : 
        soup_avis = BeautifulSoup(requests.get(str(url_avis)).content, 'html.parser')   

        # avoir la note
        for note in soup_avis.find_all(class_  = 'note' ) : 
            avis.append((note.text ,)) 
        
        # nb d'avis
        for nb_avis in soup_avis.find_all(class_ ="titlebar-title titlebar-title-md") :
            regex_nb_avis =  re.findall(r'([0-9]+) critiques spectateurs', str(nb_avis))
            if len(regex_nb_avis) > 0 :
                avis.append(regex_nb_avis)
    return avis 
    
print(get_avis(get_url_films))



