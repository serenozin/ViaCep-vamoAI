import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Collapse
from dash.dependencies import Input, Output, State

from controller import Andress, SearchOptions

external_stylesheets = [
    'https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css',
]

app = dash.Dash(__name__,
    title='CEP VamoAI',
    update_title='Atualizando...',
    external_stylesheets=external_stylesheets
    )

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/"),
        dbc.DropdownMenuItem("Documentação", href="/"),
        dbc.DropdownMenuItem("Github", href="/"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://www.flaticon.com/svg/vstatic/svg/1287/1287847.svg?token=exp=1617291988~hmac=70ee1b13184ac0fbaccc8518242ea023", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Busca ", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    dropdown, className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="#EA1D2C",
    dark=True,
    className="mb-4",
)


app.layout = html.Div(
    [
        navbar,
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
                                            dbc.Col(
                                                dbc.Collapse(
                                                    [
                                                        dbc.Col(id="card_output"),
                                                        html.Div(id="status_code"),
                                                        # html.Div(id="card_output", style={'overflowy': 'scroll'},),
                                                        html.P(),
                                                    
                                                    ],
                                                    
                                                    id="collapse_output",
                                                ),
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
                                    html.Iframe(id="iframe_mapa", height=400, width=600, style={"border": "none"}),
                            
                                ],
                                body=True,
                            ),
                        ),
                        

                    ),
                    id="collapse_mapa",
                    
                ),
                dbc.Collapse(
                    dbc.Col(
                        dbc.Row(
                            [
                            dbc.Button(".JSON", block=True, color="danger", size="sm", outline=True),
                            dbc.Button(".CSV", block=True, color="danger", size="sm", outline=True)
                            ],
                        ),
                        width=3,
                    ),
                    id="collapse_download"
                )
            ],
            justify="center",
            align="center",
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
    Output("collapse_download", "is_open"),
    Output("status_code", "children"),
    Output("collapse_mapa", "is_open"),
    Output("iframe_mapa", "src"),
    Input("dropdown_rua", "value"),
    [State("dropdown_estado", "value"),
    State("dropdown_cidade", "value"),
    ],
    prevent_initial_call=True
)
def update_dropdown_cidade(logradouro, estado, cidade):
    status200 = dbc.Row(dbc.Badge("200 success", color="success"), justify="center")
    status400 = dbc.Row(dbc.Badge("400 bad request", color="danger"), justify="center")
    endereco = Andress(estado, cidade, logradouro)
    children = []
    status_code = []

    if len(logradouro) == 0:
        collapse = False
        download = False
        collapse_mapa = False
        iframe_mapa = None
    elif len(logradouro) < 3:
        collapse = True
        download = False
        collapse_mapa = False
        iframe_mapa = None
        status_code.append(status400)
        status_code.append(html.P())
        children.append(html.P("sua busca precisa ter pelo menos 3 caracteres"))
    elif len(logradouro) >= 3:
        collapse = True
        download = True
        collapse_mapa = True
        iframe_mapa = endereco.mapa()
        status_code.append(status200)
        status_code.append(html.P())
        for i in endereco.to_json():
            for key in i:
                if i[key] != "":
                    children.append(html.P(f"{key.upper()}: {i[key]}"))
            children.append(html.Hr())

    return children, collapse, download, status_code, collapse_mapa, iframe_mapa

# @app.callback(
#     Output("collapse_mapa", "is_open"),
#     Output("iframe_mapa", "src"),
#     Input("input_cep", "value"),
#     prevent_initial_call=True
# )
# def show_map(cep):
    
#     if len(cep) == 8:
#         collapse = True
#         iframe = Mapa(cep).url
#     else:
#         collapse = False
#         iframe = None

#     return collapse, iframe