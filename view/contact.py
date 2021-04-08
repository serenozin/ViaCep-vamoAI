import dash_bootstrap_components as dbc
import dash_html_components as html

card0 = dbc.Card(
    [
        dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C4D03AQFpPViamIaVmA/profile-displayphoto-shrink_800_800/0/1613079027780?e=1623283200&v=beta&t=NSF9lVeUXZLdY2sTA9gBJofC__GNG7b2zPhdMAa1tZY", top=True),
        dbc.CardBody(
            [
                html.H4("Vithor", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary", href="https://www.linkedin.com/in/vithor-data/"),
                dbc.Button("GitHub", color="danger", href="https://github.com/Vithork/"),
                dbc.Button("Blog", color="primary", href="https://vithor.tech/"),
            ]
        ),
    ],
    style={"width": "18rem"},
)
card1 = dbc.Card(
    [
        dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C5603AQHasmiWEG3f-A/profile-displayphoto-shrink_800_800/0/1612849551283?e=1623283200&v=beta&t=B95GtN3khL1ebF0Vr0hYpAg_8b_P7sz7EFdvuNEbmrQ", top=True),
        dbc.CardBody(
            [
                html.H4("Patryck", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin",  color="primary", href="https://www.linkedin.com/in/patryckharley/"),
                dbc.Button("GitHub", color="danger", href="https://github.com/serenozin/"),
            ]
        ),
    ],
    style={"width": "15rem"},
)
card2 = dbc.Card(
    [
        dbc.CardImg(src="https://media-exp1.licdn.com/dms/image/C5603AQFRgwx0wE6VFg/profile-displayphoto-shrink_800_800/0/1596493485381?e=1623283200&v=beta&t=fL4OS3_bwWxKlY8FoOwk9zOYSUQvMfUz8FgtfP8GR7s", top=True),
        dbc.CardBody(
            [
                html.H4("Demétrio", className="card-title"),
                html.P(
                    "Desenvolvedor Python",
                    className="card-text",
                ),
                dbc.Button("Linkedin", color="primary", href="https://www.linkedin.com/in/dem%C3%A9trio-fragoso/"),
                dbc.Button("GitHub", color="danger", href="https://github.com/demetriofragoso"),
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
            dbc.Col(card0),
            dbc.Col(card1),
            dbc.Col(card2),
            dbc.Col(card3)
    ])
    ]

contatos =[
        dbc.ModalHeader(dbc.Col(html.H1("Contatos"),align="True")),
        dbc.ModalBody(lista),
        dbc.ModalFooter(
            dbc.Button(
                "Close", id="close-contatos", className="ml-auto"
            )
        ),
    ]
