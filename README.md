# FILMkhalifa AI Image Generator

แอปพลิเคชันเว็บสำหรับสร้างรูปภาพด้วย AI โดยใช้เฟรมเวิร์ก Django ที่เน้นความเรียบง่ายแต่ทรงพลัง ผู้ใช้สามารถพิมพ์คำสั่ง (Prompt) เพื่อเน้นสร้างสรรค์ผลงานศิลปะดิจิทัลผ่านระบบ AI ของ Pollinations ได้ทันที

## คุณสมบัติเด่น
- Text-to-Image Generation: สร้างรูปภาพจากข้อความได้อย่างแม่นยำ
- Prompt Autocomplete: ระบบเดาคำศัพท์อัจฉริยะ ช่วยให้คุณเขียน Prompt ได้เหมือนมือโปร
- Image Optimization: แปลงไฟล์เป็น WebP และสร้าง Thumbnail อัตโนมัติเพื่อการโหลดหน้าเว็บที่รวดเร็ว
- History Management: บันทึกประวัติการสร้างรูปภาพและสามารถเลือกดาวน์โหลดหรือลบรูปภาพได้
- Responsive Design: หน้าเว็บสวยงาม รองรับทั้งการใช้งานบนคอมพิวเตอร์และมือถือ

## เทคโนโลยีที่ใช้
- Backend: Django (Python)
- Frontend: HTML5, JavaScript, Tailwind CSS
- AI Engine: Pollinations AI
- Image Processing: Pillow (PIL)
- Database: SQLite

---

## ขั้นตอนการติดตั้ง (Setup Instruction)

1. เตรียมความพร้อมของระบบ
ตรวจสอบว่าคุณได้ติดตั้ง Python 3.8 ขึ้นไปในเครื่องเรียบร้อยแล้ว

2. สร้างสภาพแวดล้อมจำลอง (Virtual Environment)
เปิด Terminal ในโฟลเดอร์โปรเจกต์แล้วรันคำสั่ง:
python -m venv venv

3. เปิดใช้งาน Virtual Environment
- Windows:
venv\Scripts\activate
- Mac/Linux:
source venv/bin/activate

4. ติดตั้ง Library ที่จำเป็น
รันคำสั่งเพื่อติดตั้ง Dependencies ทั้งหมด:
pip install -r requirements.txt

5. ตั้งค่าสภาพแวดล้อม (.env)
สร้างไฟล์ชื่อ .env ไว้ที่โฟลเดอร์หลักของโปรเจกต์ และใส่ข้อมูลดังนี้:
HUGGINGFACE_TOKEN=your_token_here
SECRET_KEY=your_secret_key_here
DEBUG=True

6. รันคำสั่งพื้นฐานของ Django
ทำจัดการโครงสร้างฐานข้อมูล:
python manage.py makemigrations
python manage.py migrate

---

## วิธีการใช้งาน (How to Run)

1. รันเซิร์ฟเวอร์
รันคำสั่งเพื่อเริ่มใช้งาน:
python manage.py runserver

2. เข้าใช้งานผ่านเบราว์เซอร์
เปิดเบราว์เซอร์แล้วไปที่ URL:
http://127.0.0.1:8000/

3. เริ่มสร้างรูปภาพ
- พิมพ์สิ่งที่ต้องการในช่อง "Enter your prompt"
- สังเกตคำแนะนำที่จะปรากฏขึ้นขณะพิมพ์เพื่อช่วยเสริมการแต่ง Prompt
- กดปุ่ม "Generate" และรอสักครู่เพื่อรับชมผลงาน

---

## การจัดการรูปภาพ
- รูปภาพต้นฉบับจะถูกเก็บไว้ที่: media/generated_images/
- รูปภาพจิ๋ว (Thumbnail) จะถูกเก็บไว้ที่: media/generated_thumbnails/
