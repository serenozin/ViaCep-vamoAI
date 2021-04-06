import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash
from dash.dependencies import Output, Input
from dash_extensions import Download
from pages import endereco, cep
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
                                            dbc.Button("CEP", href="/", color="danger",outline=True,block=True, id="button-cep"),
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
    dbc.Collapse(cep.layout, id="collapse-cep")
    ]
)
@app.callback(
    Output("collapse-home", "is_open"),
    Output("collapse-endereco", "is_open"),
    Output("collapse-cep", "is_open"),
    Input("button-endereco", "n_clicks"),
    Input("button-cep", "n_clicks"),
    prevent_initial_call=True
)
def change_pages(n_endereco,n_cep):
    if n_endereco:
        endereco = True
        cep = False
        home = False
    elif n_cep:
        endereco = False
        cep = True
        home = False
    return home, endereco, cep