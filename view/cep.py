import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash_extensions.snippets import send_file
from dash_extensions import Download

from controller import Andress, SearchDownload
from app import app

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
                                        
                                        html.H3("Busca pelo CEP:"),
                                        html.P(),
                                        dbc.Input(id="input_cep", placeholder="CEP", type="text"),
                                        
                                        html.P(),
                                        dbc.Row(
                                            dbc.Col([
                                                dbc.Collapse(
                                                    [
                                                        dbc.Col(id="card_output_cep"),
                                                        html.Div(id="status_code_cep"),
                                                        # html.Div(id="card_output", style={'overflowy': 'scroll'},),
                                                        html.P(),
                                                    
                                                    ],
                                                
                                                    
                                                    id="collapse_output_cep",
                                                ),
                                                 dbc.Col(
                                                    [
                                                    html.Div([dbc.Button(".JSON",id='b_download_json_cep', block=True, color="danger", size="sm", outline=True), Download(id='download_json_cep')]),
                        
                                                    html.Div([dbc.Button(".CSV",id='b_download_csv_cep', block=True, color="danger", size="sm", outline=True), Download(id='download_csv_cep')])
                                                    ],
                                                ),]
                                            ),
                                            
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
                                    html.Iframe(id="iframe_mapa_cep", height=400, width=600, style={"border": "none"}),
                            
                                ],
                                body=True,
                            ),
                        ),
                        

                    ),
                    id="collapse_mapa_cep",
                    
                ),
            ],
            justify="center",
            align="center",
            className="h-50"
        ),
        dbc.Row(),
        dbc.Row(),
    ]
)
@app.callback(Output("download_csv_cep", "data"), [Input("b_download_csv_cep", "n_clicks")])
def func(n_clicks):
    return send_file("/./download/endereços.csv")

@app.callback(Output("download_json_cep", "data"), [Input("b_download_json_cep", "n_clicks")])
def func(n_clicks):
    return send_file("./download/endereços.json")


@app.callback(
    Output("card_output_cep", "children"),
    Output("collapse_output_cep", "is_open"),
    #Output("collapse_download_cep", "is_open"),
    Output("status_code_cep", "children"),
    Output("collapse_mapa_cep", "is_open"),
    Output("iframe_mapa_cep", "src"),
    Input("input_cep", "value"),
    prevent_initial_call=True
)
def update_dropdown_cidade(cep):
    status200 = dbc.Row(dbc.Badge("200 success", color="success"), justify="center")
    status400 = dbc.Row(dbc.Badge("400 bad request", color="danger"), justify="center")
    endereco = Andress(cep=cep)
    children = []
    status_code = []

    if len(cep) == 0:
        collapse = False
        download = False
        collapse_mapa = False
        iframe_mapa = None
    elif len(cep) < 8:
        collapse = True
        download = False
        collapse_mapa = False
        iframe_mapa = None
        status_code.append(status400)
        status_code.append(html.P())
        children.append(html.P("sua busca precisa ter pelo menos 3 caracteres"))
    elif len(cep) >= 8:
        collapse = True
        download = True
        collapse_mapa = True
        SearchDownload(endereco.as_json()).as_csv()
        SearchDownload(endereco.as_json()).as_json()
        iframe_mapa = endereco.mapa()
        status_code.append(status200)
        status_code.append(html.P())
    
        for key in endereco.as_json():
            if endereco.as_json()[key] != "":
                children.append(html.P(f"{key.upper()}: {endereco.as_json()[key]}"))
        children.append(html.Hr())

    return children, collapse,status_code, collapse_mapa, iframe_mapa
