import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import requests
import restapi


app=dash.Dash(__name__,external_stylesheets=[dbc.themes.CYBORG],
        meta_tags=[{'name':'viewport',
        'content':'width=device-width,initial-scale=1.0'}])

app.title="Cowin Dashboard"


app.layout=html.Div(id="page-content",children=[
    html.Div([
       html.Div([
           html.H6(children="States"),
           dcc.Dropdown(id="linedropdown1",
           options=restapi.allstate(),
           value="India",
           multi=False,
           clearable=False
           ),
       ], style={'width':'35%','padding-left':'3%','textAlign':'center',
       'padding-right':'1%','fontSize':15},className='col-4'),

       html.Div([
            html.H6(children='District'),
            dcc.Dropdown(id='linedropdown2',
                options=[{"label":"ALL","value":"ALL"}],
                #value='All',
                multi=False,
                clearable=False
            ),
        ],style={'width': '35%', 'textAlign': 'center','padding-right':'1%','fontSize':15},className='col-4'),   
    ],style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'},className='row'),
          
],)


if __name__ =="__main__":
    app.run_server(host="0.0.0.0",port=8080)