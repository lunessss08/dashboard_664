import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# =============================
# Load Dataset
# =============================
df = px.data.gapminder()

# =============================
# Create App with Bootstrap Theme
# =============================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# =============================
# Layout
# =============================
app.layout = dbc.Container(
    [
        # ===== Title =====
        dbc.Row(
            dbc.Col(
                html.H1(
                    "🌍 World Analytics Dashboard",
                    className="text-center text-primary mb-4",
                ),
            )
        ),
        # ===== Dropdown =====
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Select Continent:", className="fw-bold"),
                        dcc.Dropdown(
                            id="continent-dropdown",
                            options=[
                                {"label": c, "value": c}
                                for c in df["continent"].unique()
                            ],
                            value="Asia",
                            clearable=False,
                        ),
                    ],
                    width=6,
                )
            ],
            className="mb-4",
        ),
        # ===== KPI Cards =====
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Average Life Expectancy",
                                        className="card-title",
                                    ),
                                    html.H2(id="avg-life", className="text-info"),
                                ]
                            )
                        ],
                        className="shadow",
                    ),
                    width=4,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Average GDP per Capita", className="card-title"
                                    ),
                                    html.H2(id="avg-gdp", className="text-success"),
                                ]
                            )
                        ],
                        className="shadow",
                    ),
                    width=4,
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Total Population", className="card-title"),
                                    html.H2(id="total-pop", className="text-warning"),
                                ]
                            )
                        ],
                        className="shadow",
                    ),
                    width=4,
                ),
            ],
            className="mb-4",
        ),
        # ===== Graphs =====
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="life-exp-graph"), width=6),
                dbc.Col(dcc.Graph(id="gdp-graph"), width=6),
            ],
            className="mb-4",
        ),
        dbc.Row([dbc.Col(dcc.Graph(id="population-graph"), width=12)]),
    ],
    fluid=True,
)


# =============================
# Callback
# =============================
@app.callback(
    Output("life-exp-graph", "figure"),
    Output("gdp-graph", "figure"),
    Output("population-graph", "figure"),
    Output("avg-life", "children"),
    Output("avg-gdp", "children"),
    Output("total-pop", "children"),
    Input("continent-dropdown", "value"),
)
def update_dashboard(selected_continent):

    filtered_df = df[df["continent"] == selected_continent]

    # ===== Graph 1 =====
    fig1 = px.line(
        filtered_df,
        x="year",
        y="lifeExp",
        color="country",
        title="Life Expectancy Over Time",
    )

    # ===== Graph 2 =====
    fig2 = px.line(
        filtered_df,
        x="year",
        y="gdpPercap",
        color="country",
        title="GDP per Capita Over Time",
    )

    # ===== Graph 3 =====
    latest_year = filtered_df["year"].max()
    latest_df = filtered_df[filtered_df["year"] == latest_year]

    fig3 = px.bar(
        latest_df, x="country", y="pop", title=f"Population by Country ({latest_year})"
    )

    # ===== KPI Calculation =====
    avg_life = round(filtered_df["lifeExp"].mean(), 2)
    avg_gdp = round(filtered_df["gdpPercap"].mean(), 2)
    total_pop = f"{int(latest_df['pop'].sum()):,}"

    return fig1, fig2, fig3, avg_life, avg_gdp, total_pop
