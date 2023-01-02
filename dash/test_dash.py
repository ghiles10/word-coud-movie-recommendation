import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import recuperation_sql_to_pandas
import word_cloud 
import base64


# read data
df = recuperation_sql_to_pandas.sql_to_pandas()


# fig1 
fig1 = px.histogram(df, x="duree", title="duree")

# Convertir le graphique en code HTML png
word_cloud.word_cloud()

import os
# Vérifiez si le fichier "monfichier.txt" existe dans le répertoire courant
if os.path.exists(r"./data/word_cloud.png"):
    print("----------------------------------------------------------------------------------->")
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
else:
    print("NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN")

image_filename = r"./data/word_cloud.png" # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


# Import the data for the second graph
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
fig2 = px.histogram(df, x="month", title="Mois de sortie du film")

# Import the data for the third graph
def nettoyage_type(x) : 

    """nettoyage de la colonne type"""

    x['type'] = ' '.join( x['type'].split( )[:2]) 
    return x 

df = df.apply(nettoyage_type, axis = 1)
fig3 = px.histogram(df, x="type", title="Type de film")

# Initialize the app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([

    # Add a title
    html.H1('My Web App'),
    # Add a div to hold the graphs
    html.Div([
        
        #wordcloud
         html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
        # Add the first graph (countplot)
        dcc.Graph(figure=fig1),
        # Add the second graph (pie chart)
        dcc.Graph(figure=fig2),

        # Add the third graph (scatter plot)
        dcc.Graph(figure=fig3),

    ]),
])

    # Add some style to make the app look nice


#     html.Div(
#     children=[
#         # Your elements go here
#     ],
#     style={
#         'backgroundColor': 'blue',
#         'color': 'blue'
#     }
# )



# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug = True)
