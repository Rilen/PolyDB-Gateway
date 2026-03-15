import psycopg2
import pymysql
import time

def seed_postgres():
    try:
        conn = psycopg2.connect(host="localhost", port=5432, user="admin", password="password", database="analytics")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS sales (id SERIAL PRIMARY KEY, product TEXT, amount DECIMAL, sale_date DATE DEFAULT CURRENT_DATE)")
        cursor.execute("INSERT INTO sales (product, amount) VALUES ('Cloud Subscription', 1200.00), ('Data Storage Plan', 450.50), ('API Access Key', 75.00)")
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ PostgreSQL semeado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao semear PostgreSQL: {e}")

def seed_mysql():
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="user", password="password", database="inventory")
        with conn.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS stock (id INT AUTO_INCREMENT PRIMARY KEY, item_name VARCHAR(255), quantity INT)")
            cursor.execute("INSERT INTO stock (item_name, quantity) VALUES ('Server Rack', 12), ('Switch 24 Port', 45), ('Fiber Cable 10m', 150)")
        conn.commit()
        conn.close()
        print("✅ MySQL semeado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao semear MySQL: {e}")

if __name__ == "__main__":
    print("Iniciando semeadura dos bancos Docker...")
    seed_postgres()
    seed_mysql()
