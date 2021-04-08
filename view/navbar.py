import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("Documentação", href="https://github.com/serenozin/ViaCep-vamoAI/wiki"),
        dbc.DropdownMenuItem("Github", href="https://github.com/serenozin/ViaCep-vamoAI"),
        dbc.DropdownMenuItem("Contatos", id="buttom-contato")
    ],
    nav = True,
    in_navbar = True,
    label = "SOBRE",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="assets/favicon.ico", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Busca", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="#666666",
    dark=True,
    className="mb-4",
    sticky='top',

)


@app.callback(
    Output("navbar-collapse2", "is_open"),
    Input("navbar-toggler2", "n_clicks"),
    State("navbar-collapse2", "is_open"),
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("modal-contatos", "is_open"),
    [Input('buttom-contato', "n_clicks"), 
    Input("close-contatos", "n_clicks")],
    State("modal-contatos", "is_open"),
)
def toggle_modal(n, n2, is_open):
    if n or n2:
        return not is_open
    return is_open