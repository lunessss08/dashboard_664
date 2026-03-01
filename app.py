import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# --- 1. เตรียมข้อมูล ---
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

# --- 2. เริ่มสร้าง Dash App ---
app = dash.Dash(__name__)

# กำหนดสไตล์ส่วนกลาง
COLORS = {"background": "#f9f9f9", "text": "#2c3e50", "card": "#ffffff"}

app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "fontFamily": "sans-serif",
        "padding": "20px",
    },
    children=[
        # ส่วนหัว (Header)
        html.Div(
            [
                html.H1(
                    "🚀 Sales Insight Dashboard",
                    style={"textAlign": "center", "color": COLORS["text"]},
                ),
                html.P(
                    "วิเคราะห์ข้อมูลการขายแบบ Interactive",
                    style={"textAlign": "center", "color": "#7f8c8d"},
                ),
            ],
            style={"marginBottom": "30px"},
        ),
        # ส่วนควบคุมและสรุป (Control Panel & Cards)
        html.Div(
            [
                # Dropdown Card
                html.Div(
                    [
                        html.Label(
                            "🌍 เลือกภูมิภาคเพื่อวิเคราะห์:", style={"fontWeight": "bold"}
                        ),
                        dcc.Dropdown(
                            id="region-dropdown",
                            options=[
                                {"label": f"Region: {r}", "value": r}
                                for r in sorted(df["Region"].unique())
                            ],
                            value="North",
                            clearable=False,
                            style={"marginTop": "10px"},
                        ),
                    ],
                    style={
                        "width": "30%",
                        "display": "inline-block",
                        "verticalAlign": "top",
                        "padding": "20px",
                        "backgroundColor": COLORS["card"],
                        "borderRadius": "10px",
                        "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
                    },
                ),
                # Summary Cards
                html.Div(
                    id="summary-cards",
                    style={"width": "65%", "display": "inline-block", "float": "right"},
                ),
            ],
            style={"marginBottom": "30px", "overflow": "hidden"},
        ),
        # ส่วนกราฟแถวบน (2 กราฟ)
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="bar-chart")],
                    style={
                        "width": "58%",
                        "display": "inline-block",
                        "backgroundColor": COLORS["card"],
                        "borderRadius": "10px",
                        "padding": "10px",
                    },
                ),
                html.Div(
                    [dcc.Graph(id="pie-chart")],
                    style={
                        "width": "38%",
                        "display": "inline-block",
                        "float": "right",
                        "backgroundColor": COLORS["card"],
                        "borderRadius": "10px",
                        "padding": "10px",
                    },
                ),
            ],
            style={"marginBottom": "30px"},
        ),
        # ส่วนกราฟแถวล่าง (1 กราฟเต็มหน้าจอ)
        html.Div(
            [dcc.Graph(id="scatter-plot")],
            style={
                "backgroundColor": COLORS["card"],
                "borderRadius": "10px",
                "padding": "10px",
            },
        ),
    ],
)


# --- 3. Interactivity (Callback) ---
@app.callback(
    [
        Output("bar-chart", "figure"),
        Output("pie-chart", "figure"),
        Output("scatter-plot", "figure"),
        Output("summary-cards", "children"),
    ],
    [Input("region-dropdown", "value")],
)
def update_dashboard(selected_region):
    filtered_df = df[df["Region"] == selected_region]

    # คำนวณค่าสรุป (Summary Stats)
    total_sales = filtered_df["Sales"].sum()
    total_items = len(filtered_df)

    # กราฟที่ 1: Bar Chart (ปรับแต่งสี)
    fig1 = px.bar(
        filtered_df,
        x="Product",
        y="Sales",
        color="Category",
        title=f"📦 ยอดขายรายสินค้าใน {selected_region}",
        template="plotly_white",
    )

    # กราฟที่ 2: Pie Chart (Donut Style)
    fig2 = px.pie(
        filtered_df,
        names="Category",
        values="Sales",
        title="📊 สัดส่วนตามหมวดหมู่",
        hole=0.4,
    )

    # กราฟที่ 3: Scatter Plot
    fig3 = px.scatter(
        filtered_df,
        x="Product",
        y="Sales",
        size="Sales",
        color="Category",
        title="🔍 รายละเอียดการกระจายตัว",
        hover_name="Product",
        height=350,
    )

    # สร้าง UI สำหรับ Summary Cards
    cards = [
        html.Div(
            [
                html.H3(
                    f"฿ {total_sales:,}", style={"color": "#27ae60", "margin": "0"}
                ),
                html.P("ยอดขายรวม", style={"margin": "0", "color": "#95a5a6"}),
            ],
            style={
                "width": "45%",
                "display": "inline-block",
                "textAlign": "center",
                "padding": "15px",
                "backgroundColor": COLORS["card"],
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
            },
        ),
        html.Div(
            [
                html.H3(total_items, style={"color": "#2980b9", "margin": "0"}),
                html.P("จำนวนสินค้าที่ขาย", style={"margin": "0", "color": "#95a5a6"}),
            ],
            style={
                "width": "45%",
                "display": "inline-block",
                "float": "right",
                "textAlign": "center",
                "padding": "15px",
                "backgroundColor": COLORS["card"],
                "borderRadius": "10px",
                "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
            },
        ),
    ]

    return fig1, fig2, fig3, cards


if __name__ == "__main__":
    app.run(debug=True)
