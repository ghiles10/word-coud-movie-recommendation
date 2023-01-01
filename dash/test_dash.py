import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import recuperation_sql_to_pandas


# read data
# df = pd.read_csv(r"data\data_film.txt", sep = "\t", header = None, names = ['titre', 'date', 'duree', 'type', 'note', 'nombre avis', 'avis'] )
df = recuperation_sql_to_pandas.sql_to_pandas()

# Import the data for the first graph

x1 = df['duree'].value_counts()[0]
y1 = df['duree']

# Import the data for the second graph
x2 = df['duree'].value_counts()[0]
y2 = df['duree']

# Import the data for the third graph
x3 = df['duree'].value_counts()[0]
y3 = df['duree']

# Initialize the app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div([
    # Add a title
    html.H1('My Web App'),
    # Add a div to hold the graphs
    html.Div([
        # Add the first graph (countplot)
        dcc.Graph(
            id='graph-1',
            figure={
                'data': [{'x': x1, 'y': y1, 'type': 'bar'}],
                'layout': {'title': 'First Graph (Countplot)'}
            }
        ),
        # Add the second graph (pie chart)
        dcc.Graph(
            id='graph-2',
            figure={
                'data': [{'labels': x2, 'values': y2, 'type': 'pie'}],
                'layout': {'title': 'Second Graph (Pie Chart)'}
            }
        ),
        # Add the third graph (scatter plot)
        dcc.Graph(
            id='graph-3',
            figure={
                'data': [{'x': x3, 'y': y3, 'type': 'scatter'}],
                'layout': {'title': 'Third Graph (Scatter Plot)'}
            }
        )
    ]),
    # Add some style to make the app look nice


    html.Div(
    children=[
        # Your elements go here
    ],
    style={
        'backgroundColor': 'blue',
        'color': 'blue'
    }
)

])

# Run the app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
