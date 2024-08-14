from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dataset as ds

# Initialize app
app = Dash(__name__)

# Build components
header = html.H2("MPG Analysis Dashboard")


# App Layout
app.layout = html.Div([
        dbc.Row(header)
])



# Run the app
if __name__ == "__main__" :
    app.run_server()
