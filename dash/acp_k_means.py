from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import recuperation_sql_to_pandas
import os

def recommandation():

    """ this function is used to make a recommandation of film to the user """

    # read df 
    df = recuperation_sql_to_pandas.sql_to_pandas()
    df1= df[['titre']]
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df = df[['note', 'nombre avis', 'duree', 'month']]

    # Standrad scaler for ACP 
    sc = StandardScaler()

    # normalistion du jeu de donnée
    X_normalise = sc.fit_transform(df)

    # réalisation de l'ACP
    acp = PCA() 
    acp.fit(X_normalise)
    new_columns = acp.transform(X_normalise) # Calculer les nouvelles colonnes obtenues par l'acp

    # Création d'un dataframe contenant 3 colonnes ( variable / correlation axe1 / correlation ax2)
    n,p = X_normalise.shape # nb individus  # nb variables
    eigval = ((n-1) / n) * acp.explained_variance_ # valeurs propres
    sqrt_eigval = np.sqrt(eigval) # racine carrée des valeurs propres
    corvar = np.zeros((p,p)) # matrice vide pour avoir les coordonnées
    for k in range(p):
        corvar[:,k] = acp.components_[k,:] * sqrt_eigval[k]

    #kmeans afin d'afficher les films similaires
    km = KMeans(n_clusters=3).fit(X_normalise)
    preds = km.predict(X_normalise) # predictions pour chaque observation son cluster d'appartenance
    df['cluster'] = preds 

    # Representer graphiquement les departements sur les deux premieres composante de l'acp
    plt.scatter(new_columns[:, 0], new_columns[:, 1])
    colors = ['yellow','red','green']
    for label, x, y,c in zip(df1['titre'].str.strip().values, new_columns[:, 0], new_columns[:, 1],df['cluster']):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-5, 5),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc=colors[c], alpha=0.5),
            arrowprops = dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    if not os.path.exists("./data"):
        os.mkdir("./data") 

    # save image matplotlib 
    plt.savefig(r'./data/acp_k_means.png')


if __name__ == '__main__' : 
    recommandation() 
    