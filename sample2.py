import dash
from dash import dcc
from dash import html

#
colors = {
    'text':'#ff0000',
    'plot_color':'#D3D3D3',
    'paper_color':'#00FFFF'
}
#
app = dash.Dash()
app.layout = html.Div([
    html.H1(children = 'Hello Dash!!',
            style={
                'textAlign':'center',
                'color':colors["text"]
            }),
    html.Div(children='Creacion de un nuevo dash',
             style={
                 'textAlign':'center',
                'color':colors["text"]
             }),
    dcc.Graph(
        id = 'samplechart',
        figure = {
            'data':[
                {'x':[4,6,8],'y':[12,16,18],'type':'bar','name':'First Chart'},
                {'x':[5,6,8],'y':[12,16,18],'type':'bar','name':'Second Chart'}
            ],
            'layout':{
                'title':'Simple Bar Chart',
                'plot_bgcolor': colors["plot_color"],
                'paper_bgcolor':colors["paper_color"],
                'font':{
                    'color': colors["text"]
                }
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(port=4050)

app = dash.Dash()