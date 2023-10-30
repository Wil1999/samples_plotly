import dash
from dash import dcc
from dash import html

    #
app = dash.Dash()
app.layout = html.Div([
    html.H1('Hello Dash!!'),
    html.Div('Creacion de un nuevo dash')
])

    #

if __name__ == '__main__':
    app.run_server(port=4050)

app = dash.Dash()