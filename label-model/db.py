import psycopg2
import json
from config import settings

def get_db_connection():
    conn = psycopg2.connect(
        dbname=settings.db_name,
        user=settings.db_username,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port
    )
    return conn

# ฟังก์ชั่นสำหรับเก็บข้อมูลรูปภาพและ Label ในตาราง Pre-label
def store_pre_label_in_db(image_path: str, label: dict):
    with open(image_path, 'rb') as file:
        binary_data = file.read()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO images.pre_label (image_data, label) VALUES (%s, %s) RETURNING id",
                (psycopg2.Binary(binary_data), json.dumps(label)))
    pre_label_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return pre_label_id

# ฟังก์ชั่นสำหรับเก็บข้อมูล Re-label ในตาราง Re-label
def store_re_label_in_db(pre_label_id: int, image_path: str, label: dict):
    with open(image_path, 'rb') as file:
        binary_data = file.read()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO images.re_label (pre_label_id, image_data, label) VALUES (%s, %s, %s)",
                (pre_label_id, psycopg2.Binary(binary_data), json.dumps(label)))
    conn.commit()
    cur.close()
    conn.close()
