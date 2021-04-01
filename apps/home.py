import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Bem Vindo ao BUSCA CEP/ENDEREÇO", className="text-center")
                    , className="mb-5 mt-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Selecione o tipo de busca:', className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("CEP", href="/", color="danger",outline=True,block=True), className="mt-3", ),
                                                dbc.Col(dbc.Button("Cidade ", href="/", color="danger",outline=True,block=True),className="mt-3")],justify="center")],
                             body=True, color="danger", outline=True)
                    , width=4, className="mb-4", ),
        ], className="mb-5", justify='center'),
    ])

])