import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import plotly.io as pio
import matplotlib.pyplot as plt
import recuperation_sql_to_pandas
import word_cloud 

# read data
df = recuperation_sql_to_pandas.sql_to_pandas()


# fig1 
fig = px.histogram(df, x="duree", title="duree")

# Convertir le graphique en code HTML png
word_cloud.word_cloud()

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
          html.Img(src='word_cloud.png'),
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
    app.run_server(host='0.0.0.0')
