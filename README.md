# Simple Sales Dashboard

โปรเจกต์นี้เป็น Dashboard อย่างง่ายที่สร้างด้วย Python Dash เพื่อแสดงผลยอดขายสินค้าในแต่ละภูมิภาค

## ส่วนประกอบของ Dashboard
1. **Interactive Dropdown:** ใช้เลือกภูมิภาค (North, South, East, West) เพื่อกรองข้อมูล
2. **Bar Chart:** แสดงยอดขายแยกตามรายชื่อสินค้า
3. **Pie Chart:** แสดงสัดส่วนยอดขายตามหมวดหมู่สินค้า (Category)
4. **Scatter Plot:** แสดงการกระจายตัวของยอดขาย

## วิธีการติดตั้งและรันโปรเจกต์

### 1. เตรียมความพร้อม
ตรวจสอบว่าคุณมี Python ติดตั้งอยู่ในเครื่อง (แนะนำเวอร์ชัน 3.8 ขึ้นไป)

### 2. ติดตั้ง Library ที่จำเป็น
เปิด Terminal หรือ Command Prompt แล้วรันคำสั่ง:
```bash
pip install dash pandas plotly