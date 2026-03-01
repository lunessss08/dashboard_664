# Simple Interactive Sales Dashboard

โปรเจกต์นี้สร้างขึ้นเพื่อทดสอบความเข้าใจในการสร้าง Dashboard ด้วย **Python** และ **Plotly Dash** โดยเน้นการสร้างความสัมพันธ์ (Interactivity) ระหว่างคอมโพเนนต์

### รายละเอียด Dashboard
- **Dropdown Menu:** ใช้สำหรับเลือกประเภทสินค้า
- **Graph 1 (Bar Chart):** แสดงยอดขายแยกตามภูมิภาค
- **Graph 2 (Scatter Plot):** แสดงความสัมพันธ์ระหว่างยอดขายและกำไร
- **Graph 3 (Pie Chart):** แสดงสัดส่วนยอดขายในแต่ละเดือน

### โครงสร้างไฟล์
- `app.py`: โค้ดหลักในการประมวลผลข้อมูลและสร้าง UI
- `requirements.txt`: รายการไลบรารีที่จำเป็น

### วิธีการติดตั้งและรันโปรแกรม

1. **เตรียม Environment (แนะนำให้ใช้ Virtual Env):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # สำหรับ Mac/Linux
   # หรือ
   venv\Scripts\activate  # สำหรับ Windows