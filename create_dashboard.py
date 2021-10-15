from dash_core_components.Dropdown import Dropdown
from dash_html_components.Br import Br
from dash_html_components.Hr import Hr
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import requests
import restapi

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.title="Cowin Dashboard"

xx=[{"Type":"NA","Count":0}]

label=restapi.allstate()
df_total=pd.DataFrame(xx)
fig1=px.bar(df_total.head(20),x="Type",y="Count",color="Count",barmode="group")
fig1.update_xaxes(showgrid=True,gridcolor="black",gridwidth=1)
fig1.update_yaxes(showgrid=True,gridcolor="black",gridwidth=1)

fig1.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font_color="black",
    font_family="Arial Black",
    height=300,
    title_font_color="black"


)
card_content1 = [
    dbc.CardHeader("People Vaccinated"),
    dbc.CardBody(
        [
            html.H5("Vaccination Data", className="card-title"),
            html.H6(
                id='vac',children="""Vaccination Completed:            """+"{:,}".format(restapi.get_vaccination()["total"]),
            ), 
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='dose1',children="""Dose_1: """+"{:,}".format(restapi.get_vaccination()["tot_dose_1"]),
                ),
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='dose2',children="""Dose_2: """+"{:,}".format(restapi.get_vaccination()["tot_dose_2"]),
                ),

            

],)
]
card_content2 = [
    dbc.CardHeader("Registration Done Till Date"),
    dbc.CardBody(
        [
            html.H5("Registrations", className="card-title"),
            html.H6(
                id='regtotal',children="Total Registration: "+"{:,}".format(restapi.get_registration()["total"]),
              
            ), 
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='reg18_45',children="Age 18-45: "+"{:,}".format(restapi.get_registration()["cit_18_45"]),
                ),
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='reg_45plus',children="Age 45+: "+"{:,}".format(restapi.get_registration()["cit_45_above"]),
                ),
        ]
    ),
]
card_content3 = [
    dbc.CardHeader("Sites Conducting Vaccination"),
    dbc.CardBody(
        [
            html.H5("Sites", className="card-title"),
            html.H6(
                id='sitetotal',children="""Total Vaccination Sites:            """+str(restapi.get_sites()["total"]),
              
            ), 
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='sitegovt',children="""Goverment Sites: """+str(restapi.get_sites()["govt"]),
                ),
            html.Hr(style={"height":"2px","border-width":2,"background-color":"black"}),
            html.H6(
                id='sitepvt',children="""Private Sites: """+str(restapi.get_sites()["pvt"]),
                ),
        ]
    ),
]





app.layout=html.Div(id="page-content",children=[
    html.Div([
        html.Div([
            html.H6(children='States'),
            dcc.Dropdown(id='linedropdown1',
                options=restapi.allstate(),
                value='India',
                multi=False,
                clearable=False
            ),
        ],style={'width': '35%','padding-left':'3%', 'textAlign': 'center','padding-right':'1%','fontSize':15},className='col-4'),
     
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
          
          html.Br(),
          html.Div([
          html.Div(
            [
                dbc.Card(card_content1, color="#F1948A",outline=True)

            ],style={'width': '30%','padding-right':'1.5%','padding-left':'1.5%','textAlign': 'center','fontSize':20, 'margin':0, 'border-style': 'solid'}
        ),
        html.Div(
            [
          
                dbc.Card(card_content2, color="#99A3A4",outline=True)
              
            ],style={'width': '30%','padding-right':'1.5%','padding-left':'1.5%','textAlign': 'center','fontSize':20, 'margin':0, 'border-style': 'solid'}
        ),
        html.Div(
            [

                dbc.Card(card_content3, color="#85C1E9",outline=True)
            ],style={'width': '30%','padding-right':'1.5%','padding-left':'1.5%','textAlign': 'center','fontSize':20, 'margin':0, 'border-style': 'solid'}
        )
          ],style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center',"color":"black"},className='row'
          ),



        html.Br()
 
],)




@app.callback(
    Output('linedropdown2', 'options'),
    [Input('linedropdown1', 'value')]
)
def update_output(value1):

    try:
        options=restapi.get_district(value1)
        #print(options)
         
        return options

    except Exception as e:
            print(str(e))

@app.callback(
    Output('linedropdown2', 'value'),
    [Input('linedropdown2', 'options')]
)
def update_output1(value1):

    try:
        data=value1[1]['value']
        print(data)
        
         
        return data

    except Exception as e:
            print(str(e))

@app.callback(
    [
    Output('vac', 'children'),
    Output('dose1', 'children'),
    Output('dose2', 'children'),
    Output('sitetotal', 'children'),
    Output('sitegovt', 'children'),
    Output('sitepvt', 'children')
    ],
    [Input('linedropdown1', 'value'),
    Input('linedropdown2', 'value')]
)
def update_output2(value1,value2):
    print(value1,value2)

    try:
        sites=restapi.get_sites(value1,value2)
        vaccinations=restapi.get_vaccination(value1,value2)
        registration=restapi.get_registration(value1,value2)
        vac_total="Vaccination Completed: "+"{:,}".format(vaccinations["total"])
        vac_dose1="Dose_1: "+"{:,}".format(vaccinations["tot_dose_1"])
        vac_dose2="Dose_2: "+"{:,}".format(vaccinations["tot_dose_2"])
        total="Total Vaccination Sites: "+str(sites["total"])
        govt="Goverment Sites: "+str(sites["govt"])
        pvt="Private Sites: "+str(sites["pvt"])

        
         



        return (vac_total,vac_dose1,vac_dose2,total,govt,pvt)

    except Exception as e:
            print(str(e))


  

if __name__=="__main__":
    app.run_server(host="0.0.0.0",port=8067)

