import psycopg2
import pymysql
import sqlite3
import random
import time
import os
from datetime import datetime, timedelta

# Database Connection Settings from Environment Variables
PG_HOST = os.getenv("POSTGRES_HOST", "localhost")
PG_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
PG_USER = os.getenv("POSTGRES_USER", "admin")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "password")
PG_DB   = os.getenv("POSTGRES_DB", "analytics")

MY_HOST = os.getenv("MYSQL_HOST", "localhost")
MY_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MY_USER = os.getenv("MYSQL_USER", "user")
MY_PASS = os.getenv("MYSQL_PASSWORD", "password")
MY_DB   = os.getenv("MYSQL_DB", "inventory")

SQLITE_PATH = os.getenv("SQLITE_PATH", "data/local.db")

def seed_postgres():
    try:
        conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, user=PG_USER, password=PG_PASS, database=PG_DB)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS sales")
        cursor.execute("""
            CREATE TABLE sales (
                id SERIAL PRIMARY KEY, 
                product TEXT, 
                category TEXT,
                amount DECIMAL, 
                region TEXT,
                sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        products = [('Cloud Server Pro', 'Infra'), ('Data License v2', 'Software'), ('AI Training Pack', 'AI'), ('Support 24/7', 'Service')]
        regions = ['Norte', 'Sul', 'Leste', 'Oeste']
        
        data = []
        for _ in range(20):
            prod = random.choice(products)
            data.append((prod[0], prod[1], round(random.uniform(500, 5000), 2), random.choice(regions)))
            
        cursor.executemany("INSERT INTO sales (product, category, amount, region) VALUES (%s, %s, %s, %s)", data)
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ PostgreSQL ({PG_HOST}): Tabela 'sales' populada com 20 registros variados.")
    except Exception as e:
        print(f"❌ Erro PostgreSQL: {e}")

def seed_mysql():
    try:
        conn = pymysql.connect(host=MY_HOST, port=MY_PORT, user=MY_USER, password=MY_PASS, database=MY_DB)
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS devices")
            cursor.execute("""
                CREATE TABLE devices (
                    id INT AUTO_INCREMENT PRIMARY KEY, 
                    device_name VARCHAR(255), 
                    status VARCHAR(50), 
                    load_percentage INT,
                    last_ping TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            names = ['Node-RAK-01', 'Switch-Core', 'Edge-Gateway-X', 'Sensor-Temp-04', 'Storage-Unit-A']
            statuses = ['Online', 'Online', 'Online', 'Maintenance', 'Warning']
            
            data = []
            for name in names:
                data.append((name, random.choice(statuses), random.randint(10, 95)))
                
            cursor.executemany("INSERT INTO devices (device_name, status, load_percentage) VALUES (%s, %s, %s)", data)
        conn.commit()
        conn.close()
        print(f"✅ MySQL ({MY_HOST}): Tabela 'devices' populada com status de infraestrutura.")
    except Exception as e:
        print(f"❌ Erro MySQL: {e}")

def seed_sqlite():
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(SQLITE_PATH), exist_ok=True)
        conn = sqlite3.connect(SQLITE_PATH)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS audit_logs")
        cursor.execute("""
            CREATE TABLE audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT,
                user TEXT,
                severity TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        logs = [
            ('DB_CONNECT', 'admin', 'INFO'),
            ('QUERY_EXEC', 'dev_user', 'INFO'),
            ('AUTH_FAIL', 'unknown', 'WARNING'),
            ('CONFIG_UPDATE', 'data_eng', 'CRITICAL')
        ]
        cursor.executemany("INSERT INTO audit_logs (action, user, severity) VALUES (?, ?, ?)", logs)
        conn.commit()
        conn.close()
        print(f"✅ SQLite: Tabela 'audit_logs' populada em {SQLITE_PATH}.")
    except Exception as e:
        print(f"❌ Erro SQLite: {e}")

if __name__ == "__main__":
    print("🚀 Populando ecossistema de dados para apresentação...")
    
    # Simple retry logic for Docker network startup
    max_retries = 5
    for i in range(max_retries):
        try:
            seed_postgres()
            seed_mysql()
            seed_sqlite()
            break
        except Exception as e:
            if i < max_retries - 1:
                print(f"Retrying in 5 seconds... ({i+1}/{max_retries})")
                time.sleep(5)
            else:
                print("Failed to seed databases after several retries.")

    print("✨ Processo de seeding finalizado.")

