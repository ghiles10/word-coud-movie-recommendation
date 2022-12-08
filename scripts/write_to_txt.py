import film

# écrire vers un fichier txt
raw_data = film.get_donnees_film()

# écrire les donnes vers le fichier texte 
def extract_data() : 
    
    for titre, info in raw_data.items() : 
        with open('data_film.txt', 'a') as f :

            f.write( str(titre)+ '\t' + str(info[0][0])+ '\t' + str(info[0][1]) + '\t' + str(info[0][2])\
             +'\t' + str(info[1][0]) + '\t' + str(info[1][1]) + '\t' +str(info[2])+ '\n' )
            

    f.close()
    print('ok')

extract_data() 