import dash_bootstrap_components as dbc
import dash_html_components as html

card = dbc.Card(
    [
        dbc.CardImg(src="https://i.pinimg.com/originals/6f/33/b4/6f33b41def2a0d0ea3d7d78f0ba45309.png", top=True),
        dbc.CardBody(
            [
                html.H4("Vithor", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary"),
                dbc.Button("GitHub", color="danger"),
                dbc.Button("Blog", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)
card1 = dbc.Card(
    [
        dbc.CardImg(src="https://lastfm.freetls.fastly.net/i/u/770x0/99c52b319a0440e1ab3d7dbb127a5e33.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Patryck", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary"),
                dbc.Button("GitHub", color="danger"),
                dbc.Button("Blog", color="primary"),
            ]
        ),
    ],
    style={"width": "15rem"},
)
card2 = dbc.Card(
    [
        dbc.CardImg(src="https://lastfm.freetls.fastly.net/i/u/770x0/ae2528c7962b65400a481c3574051f95.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Demétrio", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary"),
                dbc.Button("GitHub", color="danger"),
                dbc.Button("Blog", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)
card3 = dbc.Card(
    [
        dbc.CardImg(src="https://revistafactual.com.br/wp-content/uploads/2020/05/gabriel-o-pensador-foto-luringa.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Gabriel", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary"),
                dbc.Button("GitHub", color="danger"),
                dbc.Button("Blog", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)



lista =[
        dbc.Row([
            dbc.Col(card),
            dbc.Col(card1),
            dbc.Col(card2),
            dbc.Col(card3)
    ])
    ]