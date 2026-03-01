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
        html.H1("🌍 Gapminder Dashboard", style={"textAlign": "center"}),
        # Dropdown สำหรับเลือกทวีป
        html.Label("Select Continent:"),
        dcc.Dropdown(
            id="continent-dropdown",
            options=[{"label": i, "value": i} for i in df["continent"].unique()],
            value="Asia",
        ),
        # กราฟที่ 1
        dcc.Graph(id="life-exp-graph"),
        # กราฟที่ 2
        dcc.Graph(id="gdp-graph"),
        # กราฟที่ 3
        dcc.Graph(id="population-graph"),
    ]
)


# =============================
# Callback (Interactive Part)
# =============================
@app.callback(
    Output("life-exp-graph", "figure"),
    Output("gdp-graph", "figure"),
    Output("population-graph", "figure"),
    Input("continent-dropdown", "value"),
)
def update_graphs(selected_continent):

    filtered_df = df[df["continent"] == selected_continent]

    # Graph 1: Life Expectancy over time
    fig1 = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        color="country",
        title="Life Expectancy Over Time",
    )

    # Graph 2: GDP per capita
    fig2 = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        color="country",
        title="GDP per Capita Over Time",
    )

    # Graph 3: Population
    fig3 = px.bar(
        filtered_df,
        x="country",
        y="pop",
        color="country",
        title="Population by Country",
    )

    return fig1, fig2, fig3


# =============================
# Run Server
# =============================
if __name__ == "__main__":
    app.run(debug=False)
