import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# --- 1. ข้อมูล (เหมือนเดิม) ---
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

# --- 2. เริ่มสร้าง App ---
app = dash.Dash(__name__)

# สไตล์โทนเข้ม
DARK_STYLE = {
    "background": "#1e1e2f",
    "card": "#27293d",
    "text": "#ffffff",
    "accent": "#e14eca",  # สีชมพูสะท้อนแสง
}

app.layout = html.Div(
    style={
        "backgroundColor": DARK_STYLE["background"],
        "color": DARK_STYLE["text"],
        "minHeight": "100vh",
        "padding": "0",
    },
    children=[
        # Sidebar (ฝั่งซ้าย)
        html.Div(
            [
                html.H2(
                    "📊 SALES OS",
                    style={"color": DARK_STYLE["accent"], "textAlign": "center"},
                ),
                html.Hr(style={"borderColor": "#444"}),
                html.P("Filter Control", style={"textAlign": "center"}),
                dcc.Dropdown(
                    id="region-dropdown",
                    options=[
                        {"label": f"📍 {r}", "value": r}
                        for r in sorted(df["Region"].unique())
                    ],
                    value="North",
                    clearable=False,
                    style={"color": "#000"},  # ให้ตัวหนังสือใน dropdown อ่านง่าย
                ),
                html.Div(id="summary-info", style={"marginTop": "40px"}),
            ],
            style={
                "width": "20%",
                "position": "fixed",
                "height": "100%",
                "padding": "20px",
                "backgroundColor": "#1a1a2e",
                "boxShadow": "4px 0 10px rgba(0,0,0,0.3)",
            },
        ),
        # Main Content (ฝั่งขวา)
        html.Div(
            [
                # แถวบน: กราฟเส้น (Trend/Comparison)
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="main-bar")],
                            style={
                                "backgroundColor": DARK_STYLE["card"],
                                "borderRadius": "15px",
                                "padding": "15px",
                            },
                        )
                    ],
                    style={"padding": "20px"},
                ),
                # แถวล่าง: สองกราฟคู่
                html.Div(
                    [
                        html.Div(
                            [dcc.Graph(id="sub-pie")],
                            style={
                                "width": "48%",
                                "display": "inline-block",
                                "backgroundColor": DARK_STYLE["card"],
                                "borderRadius": "15px",
                                "padding": "15px",
                            },
                        ),
                        html.Div(
                            [dcc.Graph(id="sub-scatter")],
                            style={
                                "width": "48%",
                                "float": "right",
                                "backgroundColor": DARK_STYLE["card"],
                                "borderRadius": "15px",
                                "padding": "15px",
                            },
                        ),
                    ],
                    style={"padding": "0 20px 20px 20px"},
                ),
            ],
            style={"marginLeft": "22%", "paddingTop": "20px"},
        ),
    ],
)


# --- 3. Callbacks ---
@app.callback(
    [
        Output("main-bar", "figure"),
        Output("sub-pie", "figure"),
        Output("sub-scatter", "figure"),
        Output("summary-info", "children"),
    ],
    [Input("region-dropdown", "value")],
)
def update_ui(region):
    f_df = df[df["Region"] == region]

    # 1. Bar Chart สไตล์สีรุ้งนีออน
    fig1 = px.bar(
        f_df,
        x="Product",
        y="Sales",
        color="Sales",
        color_continuous_scale="Viridis",
        title=f"PRODUCT PERFORMANCE ({region})",
    )

    # 2. Pie Chart แบบไม่มีพื้นหลัง
    fig2 = px.pie(
        f_df, names="Category", values="Sales", hole=0.6, title="CATEGORY SPLIT"
    )

    # 3. Scatter Chart
    fig3 = px.scatter(
        f_df,
        x="Product",
        y="Sales",
        size="Sales",
        color="Category",
        title="DATA DENSITY",
    )

    # ปรับแต่งธีมกราฟให้เป็น Dark ทุกตัว
    for fig in [fig1, fig2, fig3]:
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#fff",
            title_font_size=18,
        )

    # ข้อมูลสรุปใน Sidebar
    info = html.Div(
        [
            html.Div(
                [
                    html.H4("TOTAL SALES"),
                    html.H2(
                        f"${f_df['Sales'].sum():,}",
                        style={"color": DARK_STYLE["accent"]},
                    ),
                ],
                style={"textAlign": "center", "marginBottom": "20px"},
            ),
            html.Div(
                [html.H4("ITEMS"), html.H2(len(f_df), style={"color": "#4ecdc4"})],
                style={"textAlign": "center"},
            ),
        ]
    )

    return fig1, fig2, fig3, info


if __name__ == "__main__":
    app.run(debug=True)
