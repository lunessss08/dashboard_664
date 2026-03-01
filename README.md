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

	•	dash ใช้สร้าง Web Application แบบ Interactive
	•	dcc (Dash Core Components) ใช้สร้าง Graph และ Dropdown
	•	html ใช้สร้างโครงสร้าง HTML
	•	Input, Output ใช้กำหนด Callback สำหรับทำ Interactive
	•	dash_bootstrap_components (dbc) ใช้จัด Layout และ Theme ให้สวยงาม
	•	plotly.express ใช้สร้างกราฟ
	•	pandas ใช้จัดการข้อมูล

ใช้ Dataset สำเร็จรูปจาก Plotly ชื่อ Gapminder
ประกอบด้วยข้อมูล:
	•	continent
	•	country
	•	year
	•	life expectancy
	•	GDP per capita
	•	population

สร้าง Dash application
ใช้ Bootstrap Theme ชื่อ CYBORG (Dark Mode)
ทำให้ Dashboard ดูทันสมัย

Callback ทำหน้าที่:

เมื่อผู้ใช้เลือกทวีปจาก Dropdown:
	1.	ระบบจะ filter ข้อมูลตามทวีป
	2.	คำนวณค่า KPI ใหม่
	3.	สร้างกราฟใหม่ทั้ง 3 กราฟ
	4.	อัปเดตข้อมูลบนหน้าเว็บทันที
