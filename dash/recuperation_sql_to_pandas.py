import sys
sys.path.append(r'.')

from scripts import preprocess_for_ML_pyspark 

def spark_to_pandas() : 

    """ cette fonction permet de transformer les données spark en pandas afin de pouvoir faire des stats desc et des modeles ML"""

    data = preprocess_for_ML_pyspark.preproces_for_machine_learning()
    data_pandas = data.toPandas()

    return data_pandas 


if __name__ == '__main__' :
    spark_to_pandas() 