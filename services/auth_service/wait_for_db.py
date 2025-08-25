import os
import time
import psycopg2
from psycopg2 import OperationalError

db_host = os.environ.get("DATABASE_HOST", "auth-db")
db_port = int(os.environ.get("DATABASE_PORT", 5432))
db_name = os.environ.get("DATABASE_NAME", "auth_db")
db_user = os.environ.get("DATABASE_USER", "postgres")
db_password = os.environ.get("DATABASE_PASSWORD", "1234")

while True:
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.close()
        print("Postgres is ready!")
        break
    except OperationalError:
        print("Waiting for Postgres...")
        time.sleep(1)
