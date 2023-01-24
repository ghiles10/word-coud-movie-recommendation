import dash
from dash import dcc, html , Output, Input
from dash import html
import plotly.express as px
import pandas as pd
import recuperation_sql_to_pandas
import word_cloud 
import base64

# read data
df = recuperation_sql_to_pandas.sql_to_pandas()

# Convertir le graphique en code HTML png
word_cloud.word_cloud()

# Import the data for the first graph
fig1 = px.histogram(df, x="duree", title="Durée film")

image_filename = r"./data/word_cloud.png" 
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

df_type = df.apply(nettoyage_type, axis = 1)
fig3 = px.histogram(df_type, x="type", title="Type de film")

# Initialize the app
app = dash.Dash()

title_options = list(df['titre'].unique())

app.layout = html.Div([
    html.H1('My Web App'),
    html.Div([
        dcc.Dropdown(
            id='title-dropdown',
            options=[{'label': title, 'value': title} for title in title_options],
            value=title_options[0]
        ),
        html.Img(id='img',src='data:image/png;base64,{}'.format(encoded_image.decode())),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3)
    ])
])

#Create callback function
@app.callback(Output('img', 'src'),
              [Input('title-dropdown', 'value')])
              
def update_image(title):
    word_cloud.word_cloud(title)
    image_filename = r"./data/word_cloud.png"
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded_image.decode())

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0')