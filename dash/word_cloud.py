from wordcloud import WordCloud
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
from scripts import preprocess_for_ML_pyspark 
import os

def word_cloud(title = 'Babylon') :

    """ fonction qui permet de créer un word cloud à partir des avis des films """

    # read data
    df = preprocess_for_ML_pyspark.preproces_for_machine_learning()

    # stop word 
    stop_words = set(stopwords.words('french'))
    
    # ajout des mots vides
    mots_vides = ["film", "\n","plus","a","sans","dans","sans","cette",'cet', "jour","encore","fait","comme","un","très", "tous","tout","cest","si",
    "cela", 'peut',  "être", "aussi", "mais","par","dont", "moi", "il", "toi", 'ils', "les",'quoi', "ca"] 
    stop_words.update(mots_vides) 

    # Filter the dataframe by title
    df = df.filter(df.titre == title)

    # Concatenate the 'avis' column values into a single string
    avis_string = ' '.join(df.select("avis").rdd.flatMap(lambda x: x).collect())

    # Définir le calque du nuage des mots
    wc = WordCloud(background_color="black", max_words=30, stopwords=stop_words, max_font_size=100, random_state=42)
    wc.generate(avis_string)  # "Calcul" du wordcloud

    # Obtenir un objet Image à partir de wc
    image = wc.to_image()
    # Enregistrer l'image en utilisant la méthode save de l'objet Image

    if not os.path.exists("./data"):
        os.mkdir("./data") 

    image.save(r'./data/word_cloud.png') 

    return wc.words_ 

if __name__ =='__main__' : 
    word_cloud() 

