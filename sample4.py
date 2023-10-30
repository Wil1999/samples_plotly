import dash
from dash import dcc
import plotly.graph_objs as go
from dash import html
import pandas as pd
import numpy as np

#
app = dash.Dash()
#

#
x_rand= np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

app.layout = html.Div([
    dcc.Graph(
        id='scatter_chart',
        figure={
            'data': [
                go.Scatter(
                    x = x_rand,
                    y = y_rand,
                    mode = 'markers'
                )
            ],
            'layout': go.Layout(
                title= 'Scatterplot of Random 60 points',
                xaxis={'title':'Random X values'},
                yaxis={'title':'Random Y values'},
                hovermode='closest'
            )
        }
    )
])

#
if __name__ == '__main__':
    app.run_server(port=4050)

app = dash.Dash()