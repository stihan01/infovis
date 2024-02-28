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

fig = px.bar(
        data, x='år',
        y=['Cozy', 'Wholesome', 'Relaxing'], 
        text_auto=True, 
        title='Number of cozy games on steam over time',
        labels={'år':'Year','value':'Number of games in this category','variable':'Category'},
        color_discrete_sequence=px.colors.qualitative.Pastel
        )
fig.update_layout(
    font_family="Poppins"
)

#dcc.Checklist(
            #options= ['Cozy','Wholesome','Relaxing'],
            #value=['Cozy'],
            #id='checklist'),



app.layout = html.Div([
    html.Div(className='cosmo', children = [
        html.Img(src=r'assets/cosmopolitan.png', alt='image')]),
    html.Div(className='main-site', children= [
        html.H1('The rise of cozy games', className='big-title'),
        html.P('All of these genres can be seen as cozy, choose which ones you want to include!'),
        dcc.Graph(id='graph', figure=fig),
        html.Div(className='row', children =[
        dcc.Graph(id = 'PSM', figure = figPSM, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'Heart', figure = figHeartRate, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'systolic', figure = figSystolic, style = {'display': 'inline-block'}),
        dcc.Graph(id = 'diastolic', figure = figDiastolic, style = {'display': 'inline-block'})
    ])
        ])
])



# @app.callback(
#     Output("graph", "figure"), 
#     Input("checklist", "value"))
# def display_color(selected_genres):
    
    
        

#     return fig




if __name__ == '__main__':
    app.run(debug=True)




app.run_server(debug=True)