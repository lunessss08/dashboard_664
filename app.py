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
