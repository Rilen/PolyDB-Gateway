import psycopg2
import pymysql
import sqlite3
import random
import time
from datetime import datetime, timedelta

def seed_postgres():
    try:
        conn = psycopg2.connect(host="localhost", port=5432, user="admin", password="password", database="analytics")
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
        print("✅ PostgreSQL: Tabela 'sales' populada com 20 registros variados.")
    except Exception as e:
        print(f"❌ Erro PostgreSQL: {e}")

def seed_mysql():
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="user", password="password", database="inventory")
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
        print("✅ MySQL: Tabela 'devices' populada com status de infraestrutura.")
    except Exception as e:
        print(f"❌ Erro MySQL: {e}")

def seed_sqlite():
    try:
        path = 'data/local.db'
        conn = sqlite3.connect(path)
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
        print(f"✅ SQLite: Tabela 'audit_logs' populada em {path}.")
    except Exception as e:
        print(f"❌ Erro SQLite: {e}")

if __name__ == "__main__":
    print("🚀 Populando ecossistema de dados para apresentação...")
    seed_postgres()
    seed_mysql()
    seed_sqlite()
    print("✨ Tudo pronto para os prints!")
