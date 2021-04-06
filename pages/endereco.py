import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Collapse
from dash.dependencies import Input, Output, State
from controller import Andress, SearchOptions, SearchDownload
import dash_html_components as html  
from dash_extensions import Download
from dash_extensions.snippets import send_file
from app import app
import dash
import dash_html_components as html  
from dash.dependencies import Output, Input
from dash_extensions import Download
from dash_extensions.snippets import send_file

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                # html.Img(src="https://institutomontanari.com.br/wp-content/uploads/2020/05/cadastro-no-ifood.png", height="400px", width="400"),
                                        
                                dbc.Card(
                                    [
                                        
                                        html.H3("Endereço: "),
                                        html.P(),
                                        # dbc.Input(id="input_cep", placeholder="CEP", type="text"),
                                        dbc.Select(id="dropdown_estado", options=SearchOptions().all_states(), placeholder="Estado"),
                                        html.P(),
                                        dbc.Select(id="dropdown_cidade", placeholder="Cidade", ),
                                        html.P(),
                                        dbc.Collapse(
                                            dbc.Input(id="dropdown_rua", placeholder="Logradouro", type="text"),
                                            id="collapse_logradouro"
                                        ),
                                        
                                        
                                        html.P(),
                                        dbc.Row(
                                            dbc.Col([
                                                dbc.Collapse(
                                                    [
                                                        dbc.Col(id="card_output"),
                                                        html.Div(id="status_code"),
                                                        html.Div(id="counter"),
                                                        # html.Div(id="card_output", style={'overflowy': 'scroll'},),
                                                        html.P(),
                                                    
                                                    ],
                                                    
                                                    id="collapse_output",
                                                ),
                                                  dbc.Col(
                                                    [
                                                    html.Div([dbc.Button(".JSON",id='b_download_json', block=True, color="danger", size="sm", outline=True), Download(id='download_json')]),
                        
                                                    html.Div([dbc.Button(".CSV",id='b_download_csv', block=True, color="danger", size="sm", outline=True), Download(id='download_csv')])
                                                    ],
                                                ),
                                            ]),
                                            
                                        ),
                                    ],
                                    body=True
                                ),
                            ]
                        ), 
                    ],
                    lg=5,
                    # align="stretch"
                ),
                dbc.Collapse(
                    dbc.Col(
                        dbc.Row(
                            dbc.Card(
                                [
                                    html.Iframe(id="iframe_mapa", height=400, width=600, style={"border": "none"}),
                            
                                ],
                                body=True,
                            ),
                        ),
                        

                    ),
                    id="collapse_mapa",
                    
                ),
                
            ],
            justify="center",
            className="h-50"
        ),
        dbc.Row(),
        dbc.Row(),
    ]
)
@app.callback(
    Output("dropdown_cidade", "options"),
    Input("dropdown_estado", "value"),
    prevent_initial_call=True
)
def update_dropdown_cidade(estado):
    return SearchOptions().cities_from_state(estado)

@app.callback(
    Output("collapse_logradouro", "is_open"),
    Input("dropdown_cidade", "value"),
    prevent_initial_call=True
)
def update_dropdown_cidade(value):
    if value is not None:
        return True
    else: return False

@app.callback(
    Output("card_output", "children"),
    Output("collapse_output", "is_open"),
    #Output("collapse_download", "is_open"),
    Output("status_code", "children"),
    Output("collapse_mapa", "is_open"),
    Output("iframe_mapa", "src"),
    Output("counter", "children"),
    Input("dropdown_rua", "value"),
    [State("dropdown_estado", "value"),
    State("dropdown_cidade", "value"),
    ],
    prevent_initial_call=True
)
def update_dropdown_cidade(logradouro, estado, cidade):
    index = 0
    status200 = dbc.Row(dbc.Badge("200 success", color="success"), justify="center")
    status400 = dbc.Row(dbc.Badge("400 bad request", color="danger"), justify="center")
    endereco = Andress(estado, cidade, logradouro)
    children = []
    status_code = []
    

    if len(logradouro) == 0:
        collapse = False
        collapse_mapa = False
        iframe_mapa = None
    elif len(logradouro) < 3:
        collapse = True
        collapse_mapa = False
        iframe_mapa = None
        status_code.append(status400)
        status_code.append(html.P())
        children.append(html.P("sua busca precisa ter pelo menos 3 caracteres"))
    elif len(logradouro) >= 3:
        collapse = True
        collapse_mapa = True
        SearchDownload(endereco.as_json()).as_csv()
        SearchDownload(endereco.as_json()).as_json()
        iframe_mapa = endereco.mapa()
        status_code.append(status200)
        status_code.append(html.P())

        for i in endereco.as_json():
            index += 1
            for key in i:
                if i[key] != "":
                    children.append(html.P(f"{key.upper()}: {i[key]}"))
                
            children.append(html.Hr())
    
    counter = dbc.Row(dbc.Badge(f"O número de resultados foi: {index}"), justify="center")

    return children, collapse, status_code, collapse_mapa, iframe_mapa, counter

@app.callback(Output("download_csv", "data"), [Input("b_download_csv", "n_clicks")])
def func(n_clicks):
    return send_file("/home/vithor/Área de Trabalho/ViaCep-vamoAI/download/endereços.csv")

@app.callback(Output("download_json", "data"), [Input("b_download_json", "n_clicks")])
def func(n_clicks):
    return send_file("/home/vithor/Área de Trabalho/ViaCep-vamoAI/download/endereços.json")
