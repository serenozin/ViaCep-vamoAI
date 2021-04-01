import dash
from dash_bootstrap_components._components.Button import Button
from dash_bootstrap_components._components.Collapse import Collapse
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from numpy.core.shape_base import block

from model import Estados, Cidades, Endereco

external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/materia/bootstrap.min.css',
    ]

app = dash.Dash(__name__,
    title='CEP VamoAI',
    update_title='Atualizando...',
    external_stylesheets=external_stylesheets
    )


app.layout = html.Div(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row(
                    [
                    dbc.Card(
                        [
                                dcc.Dropdown(id="dropdown_estado", options=Estados().get_all(), placeholder="Estado"),
                                dcc.Dropdown(id="dropdown_cidade", placeholder="Cidade"),
                                dcc.Input(id="dropdown_rua", placeholder="Logradouro", type="text"),
                                html.P(),
                                dbc.Collapse(
                                    dbc.Row(
                                        dbc.Col(
                                            dbc.Card(body=True, id="card_output"),
                                            style={'overflowx': 'scroll'}
                                        ),
                                    ),
                                    id="collapse_output",
                                ),
                                # dbc.Row(
                                #     [
                                #         dbc.Col(width=1),
                                #         dbc.Col(
                                #             [
                                #                 dbc.Button("BUSCAR", block=True, id="button_search", color="danger"),
                                #             ],
                                #             width=10
                                #         ),
                                #         dbc.Col(width=1),
                                #     ]
                                # ),
                        ],
                        body=True
                    ),
                    ]
                    ), 
                ],
                lg=5
            )
        ],
        justify="center"
    )

)

@app.callback(
    Output("dropdown_cidade", "options"),
    Input("dropdown_estado", "value"),
    prevent_initial_call=True
)
def update_dropdown_cidade(estado):
    id = Estados().get_id(estado)
    options = Cidades().get_cidade_from_estadoid(id)

    return options

@app.callback(
    Output("card_output", "children"),
    Output("collapse_output", "is_open"),
    Input("dropdown_rua", "value"),
    [State("dropdown_estado", "value"),
    State("dropdown_cidade", "value"),
    ],
    prevent_initial_call=True
)
def update_dropdown_cidade(logradouro, estado, cidade):
    
    children = []
    if len(logradouro) == 0:
        collapse = False
    elif len(logradouro) < 3:
        collapse = True
        children.append(dbc.Badge("200", color="danger"))
    elif len(logradouro) >= 3:
        input = Endereco().request_by_endereco(estado, cidade, logradouro)
        collapse = True
        for i in range(len(input)):
            
            
                children.append(html.P(f"CEP: {input[i]['cep']}"))
                children.append(html.P(f"Logradouro: {input[i]['logradouro']}"))
                children.append(html.P(f"Complemento: {input[i]['complemento']}"))
                children.append(html.P(f"Bairro: {input[i]['bairro']}"))
                children.append(html.P(f"Localidade: {input[i]['localidade']}"))
                children.append(html.P(f"UF: {input[i]['uf']}"))
                children.append(html.P(f"DDD: {input[i]['ddd']}"))
                children.append(html.P(f"IBGE: {input[i]['ibge']}"))
                children.append(html.Hr())

    return children, collapse

