import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# =============================
# Load Dataset
# =============================
df = px.data.gapminder()

# =============================
# Create App
# =============================
app = dash.Dash(__name__)

# =============================
# Layout
# =============================
app.layout = html.Div(
    [
        html.H1("🌍 World Data Dashboard", style={"textAlign": "center"}),
        html.Label("Select Continent:"),
        dcc.Dropdown(
            id="continent-dropdown",
            options=[{"label": c, "value": c} for c in df["continent"].unique()],
            value="Asia",
            clearable=False,
        ),
        dcc.Graph(id="life-exp-graph"),
        dcc.Graph(id="gdp-graph"),
        dcc.Graph(id="population-graph"),
    ]
)


# =============================
# Callback (Interactive)
# =============================
@app.callback(
    Output("life-exp-graph", "figure"),
    Output("gdp-graph", "figure"),
    Output("population-graph", "figure"),
    Input("continent-dropdown", "value"),
)
def update_graphs(selected_continent):

    filtered_df = df[df["continent"] == selected_continent]

    fig1 = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        color="country",
        title="Life Expectancy Over Time",
    )

    fig2 = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        color="country",
        title="GDP per Capita Over Time",
    )

    fig3 = px.bar(filtered_df, x="country", y="pop", title="Population by Country")

    return fig1, fig2, fig3


# =============================
# Run App
# =============================
if __name__ == "__main__":
    app.run(debug=False)
