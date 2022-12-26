from bs4 import BeautifulSoup
import requests 
import re
# import pprint


def get_url_films(nb_page = 2) : 
    """permet de récupérer les liens de chaque film de la page du site web inital"""

    # pour stocker les url des pages web des films 
    url_enfants = []

    for page in range(1,nb_page ):  # nombre de page 
        url_page = f"https://www.allocine.fr/films/?page={page}"
        soup = BeautifulSoup(requests.get(url_page).text, 'html.parser')

        for lien_film in soup.find_all(class_ = "meta-title-link") : # avoir les liens
            if "href" in str(lien_film) : 
                regex_url = re.search(r'href="(.*)"', str(lien_film)).groups()[0]
                url_enfants.append('http://allocine.fr'+regex_url)

    return set(url_enfants) 


def get_note_et_nb_avis(lien_avis) : 

    """ prends un lien et retourne un tuple stockant le nb d'avis et de la note moyenne pour chaque film"""

    soup_avis = BeautifulSoup(requests.get(str(lien_avis)).content, 'html.parser')   

    # avoir la note et nb_avis 
    for note_nombre in soup_avis.find_all(class_  = "gd gd-gap-15 gd-xs-1 reviews-note-holder") : 
        try : 
            regex_note = re.findall(r'"note">([0-9,]+)<', str(note_nombre))[0].replace(',', '.')
            regex_nb_avis = re.findall(r'([0-9]+) critiques spectateurs', str(note_nombre))[0]

            if isinstance(float(regex_note), float) and isinstance(float(regex_nb_avis), float) :      
                return regex_note, regex_nb_avis

        except IndexError: 
            return 'vide' , 'vide'


def get_commentaire(lien_avis) : 

    
    try :
        commentaire =[] # afin de stocker tous les commentaire  
        soup_commentaire = BeautifulSoup(requests.get(str(lien_avis)).content, 'html.parser')   
        
        for com in soup_commentaire.find_all(class_ = "content-txt review-card-content") : 
            commentaire.append( com.text) 
        
        return commentaire

    except TypeError: 
        return "vide"


def get_info_de_base(soup_film_base) : 
    
    try : 
        for info_film in soup_film_base.find_all(class_ = 'meta-body-item meta-body-info') :

            # recupération des dates 
            regex_date =  re.findall(r"[0-9]+ [a-zA-Zéèû]+ [0-9]+", str(info_film))[0]

            # récupération de la durée 
            regex_duree = re.findall(r"[0-9]{1,3}h [0-9]+min", str(info_film))[0]

            # récupération dy type de films 
            regex_type =  re.findall(r">([a-zA-Z éè]+)<", str(info_film))

    except IndexError:  # eviter erreur  manque de data sur le site web
        regex_date = 'vide'
        regex_duree = 'vide'
        regex_type = 'vide'
    
    return regex_date, regex_duree, regex_type


def ajout_nombre_avis_et_note(soup_film_base ) : 
    """ retourne le lien de page de chaque films ou se trouve les avis et appel chaque lien sur la fonction get_note_et_nb_avis"""
    
    # récupération des liens des avis dans la liste liens_avis
    for page_avis in soup_film_base.find_all(class_="end-section-link") : 

        # récupération du lien avis         
        regex_lien_avis =  re.findall(r'href="(/.*/critiques/spectateurs/)', str(page_avis)) 
        if len(regex_lien_avis) > 0 :    
            lien_avis = "http://allocine.fr" + regex_lien_avis[0]  

            return get_note_et_nb_avis(lien_avis), get_commentaire(lien_avis) 
            

def get_donnees_film() : 

    """retourne un dictionnaire qui permet d'avoir toutes les info sur les films"""

    url_films = get_url_films()
    donnees_film = {} # stocker les données

    # recup html de chaque page film 
    for film in url_films : 
        soup_film = BeautifulSoup(requests.get(str(film)).text, 'html.parser') 

        # recupération des titres 
        for titre_html in soup_film.find_all(class_ = 'titlebar-title titlebar-title-lg') : 
            donnees_film[titre_html.text] = []

        # recupération des info
        donnees_film[titre_html.text].append(get_info_de_base(soup_film))
            
        #récupération du nb_avis et note 
        try : 
            donnees_film[titre_html.text].append( ajout_nombre_avis_et_note(soup_film )[0] ) 
        except TypeError:
            donnees_film[titre_html.text].append(('vide','vide'))

        # récupération commentaire 
        try :
            donnees_film[titre_html.text].append(ajout_nombre_avis_et_note(soup_film )[1])
        except TypeError: 
            donnees_film[titre_html.text].append('vide')

    return donnees_film 


if __name__ == "__main__" : 
    get_donnees_film()
    