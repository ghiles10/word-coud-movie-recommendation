from scripts import film

# écrire vers un fichier txt
raw_data = film.get_donnees_film()


print(raw_data)
# écrire les donnes vers le fichier en format csv (sep = ;)
# with open('data_film.txt', 'w') as f : 

#     f.write('titre,date,duree,note moyenne,nombre avis')
#     f.close()


