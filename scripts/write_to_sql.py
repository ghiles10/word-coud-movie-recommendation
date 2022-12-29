import mysql.connector
import pandas as pd
import film 

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

######################

# Read the CSV file into a DataFrame
df = pd.read_csv(r'../data/data_film.txt', sep = '\t')

# Connect to the database
cnx = mysql.connector.connect(user='root',
                              password='root',
                              host='mysql',
                              database='mydatabase')

# Write the DataFrame to a table in the database
df.to_sql(name='table_name', con=cnx, if_exists='replace', index=False)

# Close the connection
cnx.close()





