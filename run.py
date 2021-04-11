from dash_html_components import Div
from dash_bootstrap_components import Modal

from view import home, navbar, contact
from app import app


app.layout = Div(
    [
        navbar.navbar,
        home.layout,
        contact.contatos
    ]
)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
