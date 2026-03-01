import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# 1. จำลองข้อมูล (Mock Data)
data = {
    "Category": ["Laptop", "Smartphone", "Tablet", "Monitor"] * 25,
    "Region": np.random.choice(["North", "South", "East", "West"], 100),
    "Sales": np.random.randint(100, 1000, 100),
    "Profit": np.random.randint(10, 300, 100),
    "Month": np.random.choice(["Jan", "Feb", "Mar", "Apr"], 100),
}
df = pd.DataFrame(data)

# 2. เริ่มต้น Dash App
app = dash.Dash(__name__)

# 3. ออกแบบ Layout (โครงสร้างหน้าจอ)
app.layout = html.Div(
    [
        html.H1("Sales Analysis Dashboard", style={"textAlign": "center"}),
        html.Div(
            [
                html.Label("เลือกประเภทสินค้า:"),
                dcc.Dropdown(
                    id="category-dropdown",
                    options=[{"label": i, "value": i} for i in df["Category"].unique()],
                    value="Laptop",  # ค่าเริ่มต้น
                    clearable=False,
                ),
            ],
            style={"width": "30%", "margin": "0 auto", "padding": "20px"},
        ),
        html.Div(
            [
                dcc.Graph(id="bar-chart"),
                dcc.Graph(id="scatter-plot"),
                dcc.Graph(id="pie-chart"),
            ],
            style={"display": "flex", "flexDirection": "column"},
        ),
    ]
)


# 4. Callback (สร้างความ Interactive)
@app.callback(
    [
        Output("bar-chart", "figure"),
        Output("scatter-plot", "figure"),
        Output("pie-chart", "figure"),
    ],
    [Input("category-dropdown", "value")],
)
def update_graphs(selected_category):
    # กรองข้อมูลตามที่ผู้ใช้เลือกใน Dropdown
    filtered_df = df[df["Category"] == selected_category]

    # กราฟที่ 1: ยอดขายรวมตามภูมิภาค (Bar Chart)
    fig1 = px.bar(
        filtered_df,
        x="Region",
        y="Sales",
        color="Region",
        title=f"Total Sales by Region for {selected_category}",
    )

    # กราฟที่ 2: ความสัมพันธ์ระหว่าง Sales และ Profit (Scatter Plot)
    fig2 = px.scatter(
        filtered_df,
        x="Sales",
        y="Profit",
        size="Sales",
        title=f"Sales vs Profit for {selected_category}",
    )

    # กราฟที่ 3: สัดส่วนยอดขายตามเดือน (Pie Chart)
    fig3 = px.pie(
        filtered_df, names="Month", values="Sales", title=f"Sales Distribution by Month"
    )

    return fig1, fig2, fig3


if __name__ == "__main__":
    app.run(debug=True)
