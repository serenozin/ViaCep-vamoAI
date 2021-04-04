from logging import log
from dash_bootstrap_components._components import Modal
from dash_bootstrap_components._components.Card import Card
from dash_bootstrap_components._components.ModalBody import ModalBody
import dash_core_components as dcc
from dash_core_components.Markdown import Markdown
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash_html_components.Center import Center
from pages import contact
from app import server
from app import app
#importar as layouts
from pages import contact, home

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Documentação", href="/"),
        dbc.DropdownMenuItem("Github", href="https://github.com/serenozin/ViaCep-vamoAI"),
        dbc.DropdownMenuItem("Contato", id="buttom-contato")
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
)

contatos =  [
                dbc.ModalHeader(dbc.Col(html.H1("Contatos"),align="True")),
                dbc.ModalBody(contact.lista),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close-contatos", className="ml-auto"
                    )
                ),
            ]


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
    dbc.Modal(contatos, centered=True,id="modal-contatos",size="lg")
])


@app.callback(
            Output("modal-contatos", "is_open"),
            [Input('buttom-contato', "n_clicks"), Input("close-contatos", "n_clicks")],
            [State("modal-contatos", "is_open")],
)   

def toggle_modal(n, n2, is_open):
    if n or n2:
        return not is_open
    return is_open
    


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return home.layout

if __name__ == '__main__':
    app.run_server(debug=True,)
