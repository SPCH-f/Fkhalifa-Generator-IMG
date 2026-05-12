# Django Dashboard - คู่มือการติดตั้งและใช้งาน

## 📋 ข้อกำหนดของระบบ
- Python 3.8 ขึ้นไป
- Django 4.2 ขึ้นไป
- pandas 2.0 ขึ้นไป
- openpyxl 3.1 ขึ้นไป

## 🚀 วิธีการติดตั้ง

### 1. ติดตั้ง Libraries ที่จำเป็น

เปิด Terminal/Command Prompt และไปที่โฟลเดอร์โปรเจกต์:

```bash
cd c:\Project\Myproject
```

ติดตั้ง libraries จากไฟล์ requirements.txt:

```bash
pip install -r requirements.txt
```

หรือติดตั้งทีละตัว:

```bash
pip install Django>=4.2.0
pip install pandas>=2.0.0
pip install openpyxl>=3.1.0
pip install requests>=2.31.0
pip install Pillow>=10.0.0
```

### 2. สร้างไฟล์ Excel ตัวอย่าง

รันสคริปต์เพื่อสร้างไฟล์ Excel ตัวอย่าง:

```bash
python create_sample_excel.py
```

ไฟล์ `Test_Demo_DATA.xlsx` จะถูกสร้างในโฟลเดอร์โปรเจกต์

**หมายเหตุ:** คุณสามารถแทนที่ไฟล์นี้ด้วยไฟล์ Excel ของคุณเองได้ โดยต้องมีคอลัมน์:
- `Product` (ชื่อสินค้า)
- `Sales` (ยอดขาย)
- `Quantity` (จำนวน)
- `Category` (หมวดหมู่)

### 3. ตรวจสอบการตั้งค่า Django

ตรวจสอบว่า `Myapp` อยู่ใน `INSTALLED_APPS` ในไฟล์ `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Myapp',  # ✅ ตรวจสอบว่ามีบรรทัดนี้
]
```

### 4. รัน Migrations (ถ้ายังไม่เคยทำ)

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. เริ่มต้น Development Server

```bash
python manage.py runserver
```

## 🌐 การเข้าถึง Dashboard

เปิดเว็บเบราว์เซอร์และไปที่:

```
http://127.0.0.1:8000/dashboard/
```

## 📊 คุณสมบัติของ Dashboard

### 1. **Stat Cards** (4 ใบ)
- **ยอดขายรวม**: แสดงผลรวมของยอดขายทั้งหมด
- **จำนวนสินค้า**: แสดงผลรวมของจำนวนสินค้า
- **จำนวนรายการ**: แสดงจำนวนแถวข้อมูลในไฟล์ Excel
- **ยอดขายเฉลี่ย**: แสดงค่าเฉลี่ยของยอดขาย

### 2. **กราฟแสดงผลข้อมูล** (3 กราฟ)
- **Bar Chart**: ยอดขายตามสินค้า
- **Doughnut Chart**: สัดส่วนยอดขายตามหมวดหมู่
- **Line Chart**: แนวโน้มจำนวนสินค้า

### 3. **ตารางข้อมูล**
แสดงข้อมูลทั้งหมดจากไฟล์ Excel ในรูปแบบตาราง

## 🎨 การปรับแต่ง Design

Dashboard ใช้ **Tailwind CSS** สำหรับ styling:
- **Sidebar**: Dark mode พร้อม gradient background
- **Stat Cards**: Gradient cards พร้อม hover effects
- **Charts**: ใช้ Chart.js พร้อมสีที่เข้ากับธีม Tailwind
- **Responsive**: รองรับการแสดงผลบนหน้าจอทุกขนาด

## 📝 โครงสร้างไฟล์

```
Myproject/
├── Myapp/
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── custom_filters.py       # Custom template filters
│   ├── templates/
│   │   └── Myapp/
│   │       ├── dashboard.html      # Dashboard template
│   │       └── index.html          # หน้าแรก
│   ├── views.py                    # Views รวมถึง dashboard_view
│   ├── urls.py                     # URL routing
│   └── models.py
├── Test_Demo_DATA.xlsx             # ไฟล์ Excel ข้อมูล
├── create_sample_excel.py          # สคริปต์สร้าง Excel ตัวอย่าง
├── requirements.txt                # Dependencies
└── manage.py
```

## 🔧 การแก้ไขปัญหาที่พบบ่อย

### ปัญหา: ไม่พบไฟล์ Excel
**วิธีแก้:**
1. ตรวจสอบว่าไฟล์ `Test_Demo_DATA.xlsx` อยู่ในโฟลเดอร์โปรเจกต์
2. รันคำสั่ง `python create_sample_excel.py` เพื่อสร้างไฟล์ใหม่

### ปัญหา: ModuleNotFoundError: No module named 'pandas'
**วิธีแก้:**
```bash
pip install pandas openpyxl
```

### ปัญหา: Template ไม่แสดงผล
**วิธีแก้:**
1. ตรวจสอบว่า `Myapp` อยู่ใน `INSTALLED_APPS`
2. รัน `python manage.py collectstatic` (ถ้าใช้ static files)
3. ลองรีสตาร์ท development server

### ปัญหา: กราฟไม่แสดงผล
**วิธีแก้:**
1. ตรวจสอบ console ในเว็บเบราว์เซอร์ (F12)
2. ตรวจสอบว่า Chart.js CDN โหลดสำเร็จ
3. ตรวจสอบว่าข้อมูลใน Excel มีคอลัมน์ที่ถูกต้อง

## 📖 การใช้งานกับไฟล์ Excel ของคุณ

1. เตรียมไฟล์ Excel ที่มีคอลัมน์:
   - `Product` - ชื่อสินค้า
   - `Sales` - ยอดขาย (ตัวเลข)
   - `Quantity` - จำนวน (ตัวเลข)
   - `Category` - หมวดหมู่

2. บันทึกไฟล์เป็นชื่อ `Test_Demo_DATA.xlsx`

3. วางไฟล์ในโฟลเดอร์ `c:\Project\Myproject\`

4. รีเฟรชหน้า Dashboard ในเว็บเบราว์เซอร์

## 💡 การปรับแต่งเพิ่มเติม

### เปลี่ยนชื่อไฟล์ Excel
แก้ไขในไฟล์ `views.py` (บรรทัดที่ 97):

```python
excel_file_path = Path(settings.BASE_DIR) / 'ชื่อไฟล์ของคุณ.xlsx'
```

### เพิ่มคอลัมน์ใหม่
1. เพิ่มการประมวลผลใน `dashboard_view` (views.py)
2. ส่งข้อมูลผ่าน context
3. แสดงผลใน template (dashboard.html)

### เปลี่ยนสีกราฟ
แก้ไขในส่วน JavaScript ของ `dashboard.html`:

```javascript
backgroundColor: 'rgba(59, 130, 246, 0.8)', // เปลี่ยนสีตามต้องการ
```

## 📚 เอกสารอ้างอิง

- [Django Documentation](https://docs.djangoproject.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 🎯 สรุป

ตอนนี้คุณมี Dashboard ที่สวยงามและใช้งานได้จริงสำหรับแสดงข้อมูลจากไฟล์ Excel โดยมีฟีเจอร์:
- ✅ อ่านข้อมูลจาก Excel ด้วย pandas
- ✅ แสดง Summary Statistics (ผลรวม, ค่าเฉลี่ย)
- ✅ กราฟ 3 แบบด้วย Chart.js
- ✅ Design สวยงามด้วย Tailwind CSS
- ✅ Responsive และ Interactive

สนุกกับการพัฒนา Dashboard ครับ! 🚀
