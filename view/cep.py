import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_file

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
                                dbc.Card(
                                    [
                                        
                                        html.H3("Busca pelo CEP:"),
                                        html.P(),
                                        dbc.Input(id="input_cep", placeholder="CEP", type="text"),
                                        html.P(),
                                        dbc.Row(
                                            dbc.Col(
                                                [
                                                    dbc.Spinner(
                                                            dbc.Collapse(
                                                            [
                                                                html.Div(id="status_code_cep"),
                                                                dbc.Col(id="card_output_cep"),
                                                                html.P(),
                                                            ],
                                                            id="collapse_output_cep",
                                                        ),
                                                        type="grow",
                                                        color="danger"
                                                    ),
                                                    dbc.Col(
                                                        [
                                                        Download(id='download_json_cep'),
                                                        Download(id='download_csv_cep')
                                                        ],
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ],
                                    body=True
                                ),
                            ]
                        ), 
                    ],
                    lg=5,
                ),
                dbc.Collapse(
                    dbc.Col(
                        [
                        dbc.Row(
                            dbc.Card(
                                [
                                    html.Iframe(id="iframe_mapa_cep", height=400, width=600, style={"border": "none"}),
                            
                                ],
                                body=True,
                            ),
                        ),
                        dbc.Row(
                            dbc.Card(
                                [
                                dbc.Row(html.H6("baixar resultado como:"), justify="center"),
                                html.P(),
                                dbc.Row(
                                    [
                                    dbc.Col(dbc.Button(".CSV",id='b_download_csv_cep', block=True, color="danger", size="sm", outline=True)),
                                    dbc.Col(dbc.Button(".JSON",id='b_download_json_cep', block=True, color="danger", size="sm", outline=True)),
                                    ],
                                ),
                                ],
                                body=True
                            ),
                        ),
                        ]
                    ),
                    id="collapse_mapa_cep",
                ),
            ],
            justify="center",
            className="h-50"
        ),
    ]
)

def status_badge(code):
    if code == 200:
        return dbc.Row(dbc.Badge("200 sucesso", color="success"), justify="center")
    elif code == 404:
        return dbc.Row(dbc.Badge("404 não encontrado", color="danger"), justify="center")
    

@app.callback(Output("download_csv_cep", "data"), [Input("b_download_csv_cep", "n_clicks")])
def func(n_clicks):
    return send_file("./download/endereços.csv")

@app.callback(Output("download_json_cep", "data"), [Input("b_download_json_cep", "n_clicks")])
def func(n_clicks):
    return send_file("./download/endereços.json")


@app.callback(
    Output("card_output_cep", "children"),
    Output("collapse_output_cep", "is_open"),
    Output("status_code_cep", "children"),
    Output("collapse_mapa_cep", "is_open"),
    Output("iframe_mapa_cep", "src"),
    Input("input_cep", "value"),
)
def update_cep(cep):
    children = []
    status_code = []

    if len(cep) == 0:
        collapse = False
        collapse_mapa = False
        iframe_mapa = None

    elif len(cep) < 8 or len(cep) > 9:
        status_code.append(status_badge(404))
        status_code.append(html.P())
        collapse = True
        collapse_mapa = False
        iframe_mapa = None
        
    elif len(cep) == 8 or len(cep) == 9:
        endereco = Andress(cep=cep)
        SearchDownload(endereco.as_json()).as_csv()
        SearchDownload(endereco.as_json()).as_json()

        collapse = True
        status_code.append(status_badge(endereco.code()))
        status_code.append(html.P())
        iframe_mapa = endereco.mapa()
        collapse_mapa = True
        
        for key in endereco.as_json():
            if endereco.as_json()[key] != "":
                children.append(html.P(f"{key.upper()}: {endereco.as_json()[key]}"))
        children.append(html.Hr())

    return children, collapse, status_code, collapse_mapa, iframe_mapa
