from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
from flask.helpers import get_root_path



data = pd.read_excel('stats(2).xlsx')
data_US = pd.read_excel('users_USA.xlsx')
data_EU = pd.read_excel('users_EU.xlsx')


app = Dash(__name__)


labels = ["Men", "Women"]
values_US_2020 = [59, 41]
values_US_2021 = [55, 45]
values_US_2022 = [52, 48]

values_EU_2020 = [59, 41]
values_EU_2021 = [55, 45]
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


app.layout = html.Div([
    html.H2('The rise of cozy games'),
    html.P('All of these genres can be seen as cozy, choose which ones you want to include!'),
    dcc.Checklist(
        options= ['Cozy','Wholesome','Relaxing'],
        value=['Cozy'],
        id='checklist'),
        dcc.Graph(id='graph'),

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
        })
    ])
    
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