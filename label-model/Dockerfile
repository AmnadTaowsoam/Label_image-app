# ใช้ภาพพื้นฐานจาก python
FROM python:3.8-slim

# ตั้งค่าตัวแปรสภาพแวดล้อม
ENV PYTHONUNBUFFERED=1

# ตั้งค่าไดเร็กทอรีทำงานในคอนเทนเนอร์
WORKDIR /app

# คัดลอกไฟล์ที่จำเป็น
COPY . /app

# ติดตั้งไลบรารีที่จำเป็น
RUN pip install --upgrade pip \
    && pip install fastapi uvicorn torch torchvision pydantic python-dotenv psycopg2-binary pydantic-settings

# รันแอปพลิเคชัน
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
