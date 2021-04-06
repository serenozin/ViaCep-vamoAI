import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = ["https://unpkg.com/bootstrap-material-design@4.1.1/dist/css/bootstrap-material-design.min.css"]

app = dash.Dash(__name__,
    title='CEP VamoAI',
    update_title='Atualizando...',
    external_stylesheets=external_stylesheets,
    prevent_initial_callbacks=True
    )


server = app.server
app.config.suppress_callback_exceptions = True