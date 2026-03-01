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
