from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dataset as ds

# Initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Build components
header = html.H2("MPG Analysis Dashboard", className="text-center alert alert-info")



# App Layout
app.layout = html.Div([
        dbc.Row(header, class_name="rounded mt-0")
])



# Run the app
if __name__ == "__main__" :
    app.run_server()
