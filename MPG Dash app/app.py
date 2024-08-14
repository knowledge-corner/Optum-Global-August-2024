from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dataset as ds
import plotly.express as px

# Initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

# Build components
header = html.H2("MPG Analysis Dashboard", className="text-center alert alert-info")
bar1 = px.bar(ds.get_pivot_data(), x = "model year", y = "car name", color = "origin", barmode="group", width=800, title="Number of car by model year and country",
              labels={"car name" : ""})
hist1 = px.histogram(ds.df, x = "origin", y = "mpg", text_auto=True, color = "origin", width=500, histfunc="avg")
scatter1 = px.scatter(ds.df, x = "horsepower", y = "mpg", width = 800, facet_col = "origin", trendline="ols")
pairplot1 = px.scatter_matrix(ds.df, dimensions=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'], height=600)

# App Layout
app.layout = html.Div([ header, html.Hr(),
                       dcc.Graph(figure=bar1, id="bar1"), html.Br(),
                       dbc.Row(
                           [
                               dbc.Col(dcc.Graph(figure=hist1, id="hist1")),
                               dbc.Col(dcc.Graph(figure=scatter1, id="scatter1")),
                           ]
                       ),
                       dcc.Graph(figure=pairplot1, id="pairplot1")
])



# Run the app
if __name__ == "__main__" :
    app.run_server()
