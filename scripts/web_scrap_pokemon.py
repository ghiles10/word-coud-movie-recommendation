from bs4 import BeautifulSoup
import requests 
import re 
import pandas as pd 

def scrapping_pokemon() : 
    # recuperation du premier url parent qui contient la liste des pokemon 
    url = "https://pokemondb.net/pokedex/national"

    code_source = requests.get(url)
    soup = BeautifulSoup(code_source.text, "html.parser") 

    #stocker les url's enfants qui contient les stats des pokemon
    url_2  = [] 
    for i in soup.find( 'div' , {'class' : 'infocard-list infocard-list-pkmn-lg'}).findAll("a") : 
        if "ent-name" in str(i) :
            url_2.append( str("https://pokemondb.net")  + str( i.get("href") ) ) 


    dico_pole_stat = {} # stocker pokemon + statistiques du pokemon

    #recuperation des stats + nom des pokemon
    for url_poke in url_2  :
        url_poke = BeautifulSoup( requests.get(url_poke).text , "html.parser" ) 

        liste_poke_stat = []

        for poke_stat in url_poke.find( class_ ='grid-col span-md-12 span-lg-8' ).findAll('td') : 
            try : 
                if isinstance(int(str(poke_stat.getText())), int) :
                    liste_poke_stat.append(poke_stat.getText())

            except ValueError: 
                pass 
        liste_poke_stat =liste_poke_stat[::3 ][:-1]
    
    # pour recuperer nom du pockemon 
        regex_poke = re.findall( r"pokedex\/([a-zA-z]+)" , str(url_poke) )[0]  
        dico_pole_stat[ str(regex_poke) ] = liste_poke_stat

    return dico_pole_stat
