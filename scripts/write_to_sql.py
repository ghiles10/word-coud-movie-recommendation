import pandas as pd
import film 
from sqlalchemy import create_engine

def extract_data() : 
    
    """permet de scrapper les données et écrire dans un fichier txt"""
    print('debut scrapping')
    raw_data = film.get_donnees_film()

    with open(r'data/data_film.txt', 'w') as f :
        
        for titre, info in raw_data.items() : 

            f.write( str(titre)+ '\t' + str(info[0][0])+ '\t' + str(info[0][1]) + '\t' + str(info[0][2])\
            +'\t' + str(info[1][0]) + '\t' + str(info[1][1]) + '\t' +str(info[2])+ '\n' )
    
        f.close()

    print('extracting data done')

extract_data()


# Créez un DataFrame Pandas à partir du fichier CSV
df = pd.read_csv(r'./data/data_film.txt', sep='\t', header = None,names= ['titre', 'date' , 'duree' , 'type' , 'note' , 'nb_avis' , 'avis'])

# Créez un objet engine
user = 'docker'
password = 'docker'
host = 'db'
database_name = 'mydatabase'

# Créez l'objet engine
engine = create_engine(f'postgresql://{user}:{password}@{host}/{database_name}')

# Écrivez le DataFrame dans la table
df.to_sql('film', engine, if_exists='replace')

print('Vous pouvez ouvrir')
