from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
from flask.helpers import get_root_path



data = pd.read_excel('stats(2).xlsx')
data_US = pd.read_excel('users_USA.xlsx')
data_EU = pd.read_excel('users_EU.xlsx')
data_genre = pd.read_excel('female in game genre.xlsx')

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


labels = ["Men", "Women"]
values_US_2020 = [59, 41]
values_US_2021 = [55, 45]
values_US_2022 = [52, 48]

values_EU_2020 = [54, 46]
values_EU_2021 = [53, 47]
values_EU_2022 = [52, 48]

fig_US_20 = px.pie(data_US, values=values_US_2020, names=labels, title="2020", width = 300)
fig_US_21 = px.pie(data_US, values=values_US_2021, names=labels, title="2021", width = 300)
fig_US_22 = px.pie(data_US, values=values_US_2022, names=labels, title="2022", width = 325)

fig_US_20.update_layout(showlegend=False)
fig_US_21.update_layout(showlegend=False)

fig_EU_20 = px.pie(data_US, values=values_EU_2020, names=labels, title="2020", width = 300)
fig_EU_21 = px.pie(data_US, values=values_EU_2021, names=labels, title="2021", width = 300)
fig_EU_22 = px.pie(data_US, values=values_EU_2022, names=labels, title="2022", width = 300)

fig_EU_20.update_layout(showlegend=False)
fig_EU_21.update_layout(showlegend=False)
fig_EU_22.update_layout(showlegend=False)



genres = ["Match 3", "Family/Farm sim", "Casual Puzzel", "Atmpospheric Exploration",
      "Interactive Drama", "MMOs (High Fantasy)", "Japanese RPG", "Western RPG",
      "Survival Roguelike", "Platformer", "City Building", "Action RPG", "Sandbox",
      "Action Adventure", "MMOs (Sci-Fi)", "Open World", "Turn-Based Strategy", "MOBA",
      "Grand Strategy", "First-Person shooter", "Racing", "Tactical Shooter", "Sports"

]

fig_genre = go.Figure()
fig_genre.add_bar(x=[69,69,42,41,37,36,33,26,25,25,22,20,18,18,16,14,11,10,7,7,6,4,2],y=genres, name="Women",orientation='h')
fig_genre.add_bar(x=[31,31,58,59,63,64,67,74,75,75,78,80,82,82,84,86,89,90,93,93,94,96,98],y=genres, name= "Men",orientation='h')
fig_genre.update_layout(barmode="relative")


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
        ]),
        html.H3("USA Players:"),
        html.Div(id="pieCharts", className="row", children=[

            dcc.Graph(id='US20',figure=fig_US_20, style={
                "display": "inline-block"
            }),
            dcc.Graph(id='US21',figure=fig_US_21, style={
                "display": "inline-block"
            }),
            dcc.Graph(id='US22',figure=fig_US_22, style={
                "display": "inline-block"
            }),
            html.H3("Europe Players:"),
            dcc.Graph(id='EU20',figure=fig_EU_20, style={
                "display": "inline-block"
            }),
            dcc.Graph(id='EU21',figure=fig_EU_21, style={
                "display": "inline-block"
            }),
            dcc.Graph(id='EU22',figure=fig_EU_22, style={
                "display": "inline-block"
            }),
            dcc.Graph(id="genre", figure=fig_genre, style={
                "display": "inline-block"
            })
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