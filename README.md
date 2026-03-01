# World Analytics Dashboard

## 📌 Project Overview

This project is a simple interactive dashboard developed using Dash and Plotly.

The dashboard visualizes world development data using the Gapminder dataset.

## 🎯 Features

- 3 Interactive Graphs
- KPI Summary Cards
- Dropdown Filter by Continent
- Responsive Bootstrap Layout
- Dark Theme Design

## 📊 Graphs Included

1. Life Expectancy Over Time (Line Chart)
2. GDP per Capita Over Time (Line Chart)
3. Population by Country (Bar Chart - Latest Year)

## 🛠 Technologies Used

- Python
- Dash
- Plotly Express
- Dash Bootstrap Components
- Pandas

## ⚙️ Installation

1. Create virtual environment (optional but recommended)

```
python -m venv env
source env/bin/activate   # Mac/Linux
```

2. Install required packages

```
pip install dash
pip install plotly
pip install pandas
pip install dash-bootstrap-components
```

or use:

```
pip install -r requirements.txt
```

## ▶️ How to Run

Run the application using:

```
python app.py
```

After running, open your browser and go to:

```
http://127.0.0.1:8050
```

## 🧠 Interactive Mechanism

When the user selects a continent from the dropdown menu:

- Data is filtered dynamically
- All graphs update automatically
- KPI values are recalculated

This demonstrates the use of Dash Callback for interactive components.