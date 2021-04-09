import dash

app = dash.Dash(__name__,
    title='CEP VamoAI',
    update_title='Atualizando...',
    # external_stylesheets=external_stylesheets,
    prevent_initial_callbacks=True
    )
app.config.suppress_callback_exceptions = True