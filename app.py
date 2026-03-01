import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# 1. เตรียมข้อมูลจำลอง (Mock Data)
data = {
    "Category": [
        "Electronics",
        "Electronics",
        "Clothing",
        "Clothing",
        "Home",
        "Home",
        "Electronics",
        "Home",
    ],
    "Product": [
        "Laptop",
        "Mouse",
        "T-Shirt",
        "Jeans",
        "Lamp",
        "Chair",
        "Keyboard",
        "Table",
    ],
    "Sales": [1200, 300, 500, 700, 150, 450, 200, 800],
    "Region": ["North", "South", "North", "East", "West", "North", "East", "South"],
}
df = pd.DataFrame(data)

# 2. เริ่มสร้าง Dash App
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Sales Analysis Dashboard",
            style={"textAlign": "center", "color": "#2c3e50"},
        ),
        html.Div(
            [
                html.Label("เลือกภูมิภาค (Interactive Filter):"),
                dcc.Dropdown(
                    id="region-dropdown",
                    options=[{"label": r, "value": r} for r in df["Region"].unique()],
                    value="North",  # ค่าเริ่มต้น
                    clearable=False,
                    style={"width": "50%"},
                ),
            ],
            style={"padding": "20px"},
        ),
        html.Div(
            [
                # กราฟที่ 1: ยอดขายรายสินค้า (Bar Chart)
                dcc.Graph(
                    id="bar-chart", style={"display": "inline-block", "width": "48%"}
                ),
                # กราฟที่ 2: สัดส่วนหมวดหมู่ (Pie Chart)
                dcc.Graph(
                    id="pie-chart", style={"display": "inline-block", "width": "48%"}
                ),
            ]
        ),
        # กราฟที่ 3: กระจายตัวของราคา (Scatter Plot)
        html.Div([dcc.Graph(id="scatter-plot")]),
    ]
)


# 3. ส่วนของ Interactivity (Callback)
@app.callback(
    [
        Output("bar-chart", "figure"),
        Output("pie-chart", "figure"),
        Output("scatter-plot", "figure"),
    ],
    [Input("region-dropdown", "value")],
)
def update_graphs(selected_region):
    # กรองข้อมูลตามภูมิภาคที่เลือก
    filtered_df = df[df["Region"] == selected_region]

    # สร้าง Bar Chart
    fig1 = px.bar(
        filtered_df,
        x="Product",
        y="Sales",
        title=f"Sales by Product in {selected_region}",
        color="Product",
    )

    # สร้าง Pie Chart
    fig2 = px.pie(
        filtered_df, names="Category", values="Sales", title=f"Sales share by Category"
    )

    # สร้าง Scatter Plot
    fig3 = px.scatter(
        filtered_df,
        x="Product",
        y="Sales",
        size="Sales",
        color="Category",
        title=f"Sales Distribution Details",
        hover_name="Product",
    )

    return fig1, fig2, fig3


if __name__ == "__main__":
    app.run_server(debug=True)
