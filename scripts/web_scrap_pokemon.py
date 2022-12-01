from bs4 import BeautifulSoup
import requests 
import re 
import pandas as pd 
import pprint

def get_links_pokemons() : 

    """retourne une liste qui comporte des liens pour accéder a la page web qui contient les stats de chaque pokemon"""

    # recuperation du premier url parent qui contient la liste des pokemons
    url_parent = "https://pokemondb.net/pokedex/national"
    soup = BeautifulSoup(requests.get(url_parent).text, "html.parser") 

    #stocker les url's enfants qui contient les stats de chaque pokemon
    url_enfants  = [] 

    for i in soup.find( 'div' , {'class' : 'infocard-list infocard-list-pkmn-lg'}).findAll("a") : 
        if "ent-name" in str(i) :
            url_enfants.append( str("https://pokemondb.net")  + str( i.get("href") ) ) 

    return  url_enfants 

def get_stats_and_type_pokemons(func ) :  
    
    """permet de récuperer le nom, les stats et le type des pokemons et retourne un dictionnaire stockant ces données"""

    url = func()
    poke_data = {} #stocker les stats des pokemons

    #recuperation des données 
    
    for url_poke in url  :
        url_poke = BeautifulSoup( requests.get(url_poke).text , "html.parser" ) 

        #recuperation des stats + nom des pokemon
        liste_poke_stat = []
        for poke_stat in url_poke.find( class_ ='grid-col span-md-12 span-lg-8' ).findAll('td') : 

            try : 
                if isinstance(int(str(poke_stat.getText())), int) :        # ne recupérer que le statistiques en gérant les exceptions
                    liste_poke_stat.append(poke_stat.getText())

            except ValueError: 
                pass 

        liste_poke_stat =liste_poke_stat[::3 ][:-1]

    #recuperation des types de pokemon   
        try : 
            liste_type_pokemon = []
            for poke_type in url_poke.find( class_ ='infocard-lg-data text-muted' ).findAll('a') :
                if "itype" in str(poke_type)   : 
                    regex_type = re.search(r"itype ([a-zA-Z]+)", str(poke_type)).groups()[0]
                    liste_type_pokemon.append( regex_type )
                 
        except AttributeError:
            pass

    # pour recuperer nom du pockemon dans le dictionnaire poke stat 
        regex_poke = re.findall( r"pokedex\/([a-zA-z]+)" , str(url_poke) )[0]
        poke_data[ str(regex_poke) ] = (liste_poke_stat, liste_type_pokemon) 


    return poke_data

pprint.pprint((get_stats_and_type_pokemons(get_links_pokemons)))



