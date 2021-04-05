import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from pages import endereco
from app import app

layout = html.Div(
    [
    dbc.Collapse(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.H1("Bem Vindo ao BUSCA CEP/ENDEREÇO", className="text-center"
                        ), 
                        className="mb-5 mt-5"
                    )
                ]
            ),

            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                html.H3(
                                    children='Selecione o tipo de busca:', 
                                    className="text-center"
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button("CEP", href="/", color="danger",outline=True,block=True),
                                            className="mt-3", 
                                        ),

                                        dbc.Col(
                                            dbc.Button("Cidade ", href="/", color="danger",outline=True,block=True, id="button-endereco"),
                                            className="mt-3"
                                        ),
                                    ],
                                        justify="center"
                                ),
                            ],
                            body=True, color="danger", outline=True
                        ),
                        lg=4, 
                        className="mb-4",
                    ),
                ],
                className="mb-5", 
                justify='center'
            ),
        ],
        is_open=True,
        id="collapse-home",
    ),
    dbc.Collapse(endereco.layout, id="collapse-endereco"),
    ]
)
@app.callback(
    Output("collapse-home", "is_open"),
    Output("collapse-endereco", "is_open"),
    Input("button-endereco", "n_clicks"),
    prevent_initial_call=True

)
def change_pages(n):
    if n:
        endereco = True
        home = False
    return home, endereco