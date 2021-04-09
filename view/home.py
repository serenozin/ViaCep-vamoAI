import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from view import endereco, cep
from app import app

layout = html.Div(
    [
    dbc.Collapse(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                html.P(),
                                dbc.Row(html.H5("BEM-VINDA AO"), justify="center"),
                                dbc.Row(html.H1("BUSCA ENDEREÇO"), justify="center"),
                                html.P()
                            ],
                            body=True
                        ),
                        lg=4
                    )
                ],
                justify="center"
            ),

            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                html.H4(
                                    children='Selecione o método de busca:', 
                                    className="text-center"
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button("CEP", href="/", color="danger",outline=True,block=True, id="button-cep"),
                                            className="mt-3", 
                                        ),

                                        dbc.Col(
                                            dbc.Button("logradouro", href="/", color="danger",outline=True,block=True, id="button-endereco"),
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