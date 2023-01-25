import pandas as pd
import write_to_txt 
import preprocess_for_ML_pyspark
from sqlalchemy import create_engine

def main() : 

    write_to_txt.extract_data()

    # création d'une base de données avec pyspark/ nettoyage de la base 
    data_spark = preprocess_for_ML_pyspark.preproces_for_machine_learning()

    # Conversion du DataFrame PySpark en DataFrame pandas
    df = data_spark.toPandas()

    # Créer un objet engine
    USER = 'docker'
    PASSWORD = 'docker'
    HOST = 'db'
    DATABASE_NAME = 'mydatabase'

    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}')

    # Écriture du DataFrame dans la table
    df.to_sql('film', engine, if_exists='replace')

    print('Vous pouvez ouvrir')

if __name__ =='__main__':
    main()
