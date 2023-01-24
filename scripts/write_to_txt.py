import film 

def extract_data() : 
    
    """permet de scrapper les données et écrire dans un fichier txt"""
    print('debut scrapping')
    raw_data = film.get_donnees_film()

    with open(r'./data/data_film.txt', 'w') as f :
        
        for titre, info in raw_data.items() : 

            f.write( str(titre)+ '\t' + str(info[0][0])+ '\t' + str(info[0][1]) + '\t' + str(info[0][2])\
            +'\t' + str(info[1][0]) + '\t' + str(info[1][1]) + '\t' +str(info[2])+ '\n' )
    
        f.close()

    print('extracting data done')

if __name__ == '__main__' :
    extract_data()


