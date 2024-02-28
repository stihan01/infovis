from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from flask.helpers import get_root_path



data = pd.read_excel('stats(2).xlsx')

inpactData = pd.read_excel('inpact.xlsx')

figPSM = px.bar(inpactData, x=" ", y="PSM-9", width =400,
                 color="Category", barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)
figHeartRate = px.bar(inpactData, x=" ", y="Heart rate", width =400,
                 color="Category", barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)
figSystolic= px.bar(inpactData, x=" ", y="Systolic BP", width =400,
                 color="Category", barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)
figDiastolic = px.bar(inpactData, x=" ", y="Diastolic BP", width =400,
                 color="Category", barmode="group", color_discrete_sequence=px.colors.qualitative.Pastel)

figHeartRate.update_layout(showlegend=False)
figSystolic.update_layout(showlegend=False)
figDiastolic.update_layout(showlegend=False)
figPSM.update_layout(legend=dict(
    orientation="h",
    entrywidth=100,
    yanchor="bottom",
    y=1.02,
    xanchor="left",
    x=0
))

app = Dash(__name__)



app.layout = html.Div([
    html.H2('The rise of cozy games'),
    html.P('All of these genres can be seen as cozy, choose which ones you want to include!'),
    dcc.Checklist(
        options= ['Cozy','Wholesome','Relaxing'],
        value=['Cozy'],
        id='checklist'),
    dcc.Graph(id='graph'),
    html.Div(className='row', children =[
        dcc.Graph(id = 'PSM', figure = figPSM, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'Heart', figure = figHeartRate, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'systolic', figure = figSystolic, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'diastolic', figure = figDiastolic, style = {'display': 'inline-block'})
    ]),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def display_color(selected_genres):
    fig = px.bar(
        data, x='år',
        y=selected_genres, 
        text_auto=True, 
        title='Number of cozy games on steam over time',
        labels={'år':'Year','value':'Number of games in this category','variable':'Category'},
        color_discrete_sequence=px.colors.qualitative.Pastel
        )
    fig.update_layout(
        font_family="Poppins"
    )
    
        

    return fig



if __name__ == '__main__':
    app.run(debug=True)




app.run_server(debug=True)