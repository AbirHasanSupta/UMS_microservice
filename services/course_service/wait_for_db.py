import time
import psycopg2
import os

DB_NAME = os.environ.get("DB_NAME", "course_db")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "course-db")
DB_PORT = os.environ.get("DB_PORT", 5432)

while True:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        print("Database is ready!")
        break
    except Exception as e:
        print("Waiting for database...", e)
        time.sleep(2)
