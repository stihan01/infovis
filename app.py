from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



data = pd.read_excel('stats(1).xlsx')


app = Dash(__name__)



app.layout = html.Div([
    html.H4('The rise of cozy games'),
    html.P('All of these genres can be seen as cozy, choose which ones you want to include!'),
    dcc.Checklist(
        options= [{'label':'Cozy','value':'cozy'},
                  {'label':'Wholesome','value':'wholesome'},
                  {'label':'Relaxing','value':'relaxing'}],
        value=['cozy'],
        id='checklist'),
        dcc.Graph(id='graph')
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def display_color(selected_genres):
    fig = px.bar(data, x='år',y=selected_genres, text_auto=True)

    return fig






app.run_server(debug=True)