import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash_extensions import Download
from dash_extensions.snippets import send_file

from app import app 
from controller import Andress, SearchOptions, SearchDownload  


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
                                        
                                        html.H3("Busca pelo endereço: "),
                                        html.P(),
                                        dbc.Select(id="dropdown_estado", options=SearchOptions().all_states(), placeholder="Estado"),
                                        html.P(),
                                        dbc.Spinner(dbc.Select(id="dropdown_cidade", placeholder="Cidade"), color="danger", type="grow"),
                                        html.P(),
                                        dbc.Collapse(
                                            dbc.Input(id="dropdown_rua", placeholder="Logradouro", type="text"),
                                            id="collapse_logradouro"
                                        ),
                                        html.P(),
                                        dbc.Row(
                                            dbc.Col(
                                                [   dbc.Spinner(
                                                        dbc.Collapse(
                                                            [
                                                                
                                                                dbc.Row(
                                                                    [
                                                                    dbc.Col(html.Div(id="status_code")),
                                                                    dbc.Col(html.Div(id="counter")),
                                                                    html.P(),
                                                                    ]
                                                                ),
                                                                dbc.Row(dbc.Col(id="card_output")), 
                                                        
                                                            ],
                                                            id="collapse_output",
                                                        ),
                                                        type="grow",
                                                        color="danger"
                                                    ),
                                                    dbc.Col(
                                                        [
                                                        Download(id='download_json'),
                                                         
                                                        Download(id='download_csv')
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
                            dbc.Card(html.Iframe(id="iframe_mapa", height=400, width=600, style={"border": "none"}),
                                body=True,
                            ),
                        ),
                        dbc.Row(
                            dbc.Card(
                                [
                                dbc.Row(html.H6("baixar resultados como:"), justify="center"),
                                html.P(),
                                dbc.Row(
                                    [
                                    dbc.Col(dbc.Button(".CSV",id='b_download_csv', block=True, color="danger", size="sm", outline=True)),
                                    dbc.Col(dbc.Button(".JSON",id='b_download_json', block=True, color="danger", size="sm", outline=True)),
                                    ],
                                ),
                                ],
                                body=True
                            ),
                        ),
                        ]
                    ),
                    id="collapse_mapa",
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

@app.callback(
    Output("dropdown_cidade", "options"),
    Input("dropdown_estado", "value"),
)
def update_dropdown_cidade(estado):
    return SearchOptions().cities_from_state(estado)

@app.callback(
    Output("collapse_logradouro", "is_open"),
    Input("dropdown_cidade", "value"),
)
def update_dropdown_cidade(value):
    if value is not None:
        return True
    else: return False

@app.callback(
    Output("card_output", "children"),
    Output("collapse_output", "is_open"),
    Output("status_code", "children"),
    Output("collapse_mapa", "is_open"),
    Output("iframe_mapa", "src"),
    Output("counter", "children"),
    Input("dropdown_rua", "value"),
    [State("dropdown_estado", "value"),
    State("dropdown_cidade", "value"),],
)
def update_dropdown_cidade(logradouro, estado, cidade):
    index = 0
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
        status_code.append(status_badge(404))
        status_code.append(html.P())
    elif len(logradouro) >= 3:
        collapse = True
        collapse_mapa = True
        SearchDownload(endereco.as_json()).as_csv()
        SearchDownload(endereco.as_json()).as_json()
        iframe_mapa = endereco.mapa()
        status_code.append(status_badge(endereco.code()))
        status_code.append(html.P())

        for i in endereco.as_json():
            index += 1
            for key in i:
                if i[key] != "":
                    children.append(html.P(f"{key.upper()}: {i[key]}"))
                
            children.append(html.Hr())
    
    counter = dbc.Row(dbc.Badge(f"{index} resultados"), justify="center")

    return children, collapse, status_code, collapse_mapa, iframe_mapa, counter

@app.callback(Output("download_csv", "data"), [Input("b_download_csv", "n_clicks")])
def func(n_clicks):
    return send_file("./download/endereços.csv")

@app.callback(Output("download_json", "data"), [Input("b_download_json", "n_clicks")])
def func(n_clicks):
    return send_file("./download/endereços.json")
