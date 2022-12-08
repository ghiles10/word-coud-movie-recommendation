import film

# écrire vers un fichier txt
raw_data = film.get_donnees_film()

# écrire les donnes vers le fichier texte 
def extract_data() : 
    
    for titre, info in raw_data.items() : 
        with open('data_test.txt', 'a') as f :
            f.write( str(titre)+ ',' + str(info[0])+',' +str(info[1])+ ',' +str(info[2])+ '\n' )
            

    f.close()
    print('ok')

extract_data()

