import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# ===============================
# Load Dataset
# ===============================
df = px.data.iris()  # ใช้ dataset iris สำเร็จรูป

# ===============================
# Create Dash App
# ===============================
app = dash.Dash(__name__)
app.title = "Simple Iris Dashboard"

# ===============================
# Layout
# ===============================
app.layout = html.Div(
    [
        html.H1("Iris Interactive Dashboard"),
        # Dropdown เลือก Species
        html.Label("Select Species:"),
        dcc.Dropdown(
            id="species-dropdown",
            options=[{"label": s, "value": s} for s in df["species"].unique()],
            value="setosa",
        ),
        # Slider เลือกช่วง Petal Length
        html.Label("Minimum Petal Length:"),
        dcc.Slider(
            id="petal-slider",
            min=df["petal_length"].min(),
            max=df["petal_length"].max(),
            step=0.1,
            value=1,
            marks=None,
            tooltip={"placement": "bottom"},
        ),
        # Graph 1
        dcc.Graph(id="scatter-plot"),
        # Graph 2
        dcc.Graph(id="histogram"),
        # Graph 3
        dcc.Graph(id="box-plot"),
    ]
)


# ===============================
# Callback (Interactive Part)
# ===============================
@app.callback(
    Output("scatter-plot", "figure"),
    Output("histogram", "figure"),
    Output("box-plot", "figure"),
    Input("species-dropdown", "value"),
    Input("petal-slider", "value"),
)
def update_graphs(selected_species, min_petal_length):

    # Filter data
    filtered_df = df[
        (df["species"] == selected_species) & (df["petal_length"] >= min_petal_length)
    ]

    # Graph 1: Scatter Plot
    scatter = px.scatter(
        filtered_df,
        x="sepal_length",
        y="sepal_width",
        color="species",
        title="Sepal Length vs Sepal Width",
    )

    # Graph 2: Histogram
    histogram = px.histogram(
        filtered_df, x="petal_length", nbins=20, title="Distribution of Petal Length"
    )

    # Graph 3: Box Plot
    box = px.box(filtered_df, y="petal_width", title="Petal Width Distribution")

    return scatter, histogram, box


# ===============================
# Run Server
# ===============================
if __name__ == "__main__":
    app.run_server(debug=True)
