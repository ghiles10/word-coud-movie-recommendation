import sys
sys.path.append(".")
import os
import pytest
import pyspark
from pyspark.sql import SparkSession
from scripts import preprocess_for_ML_pyspark 
import requests

def test_dash_app_returns_200_status_code():

    """Teste si l'application Dash retourne un code de statut 200"""

    response = requests.get("http://localhost:8050/")
    assert response.status_code == 200

def test_file_txt() : 

    """Teste si le fichier data_film.txt n'est pas vide"""

    # assert if the file in not empty 
    assert os.path.getsize(r'./data/data_film.txt') > 0 

def test_preproces_for_machine_learning():

    """Teste la fonction preproces_for_machine_learning"""

    # Appeler la fonction
    result = preprocess_for_ML_pyspark.preproces_for_machine_learning()

    # Vérifier que le résultat est bien un objet DataFrame de PySpark
    assert isinstance(result, pyspark.sql.dataframe.DataFrame) 

    # Vérifier que le résultat n'est pas vide
    assert result.count() > 0 

def test_word_cloud_png() :     

    """ Teste si le fichier word_cloud.png n'est pas vide"""

    # assert if the file in not empty 
    assert os.path.getsize(r'./data/word_cloud.png') > 0 

def test_ACP_KMEANS_png() : 

    """ Teste si le fichier acp_k_means.png n'est pas vide"""

    # assert if the file in not empty 
    assert os.path.getsize(r'./data/acp_k_means.png') > 0