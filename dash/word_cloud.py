
def word_cloud() : 

    import pandas as pd
    import recuperation_sql_to_pandas
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords 
    import matplotlib.pyplot as plt
    import plotly.express as px
    import plotly.io as pio
    import plotly.tools as tls
    from PIL import Image


    # read data
    df = recuperation_sql_to_pandas.sql_to_pandas()

    # stop word 
    stop_words = set(stopwords.words('french'))
    # ajout des mots vides
    mots_vides = ["film", "\n"]
    stop_words.update(mots_vides) 

    # Définir le calque du nuage des mots
    wc = WordCloud(background_color="black", max_words=50, stopwords=stop_words, max_font_size=50, random_state=42)
    plt.figure(figsize= (10,6)) # Initialisation d'une figure
    wc.generate(df['avis'][0])  # "Calcul" du wordcloud
    # Obtenir un objet Image à partir de wc
    image = wc.to_image()

    # Enregistrer l'image en utilisant la méthode save de l'objet Image
    image.save('word_cloud.png')


if __name__ =='__main__' : 
    word_cloud() 
