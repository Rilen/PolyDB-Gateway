import pymysql

try:
    conn = pymysql.connect(host="localhost", port=3306, user="user", password="password", database="inventory")
    with conn.cursor() as cur:
        cur.execute("SHOW TABLES")
        tables = [row[0] for row in cur.fetchall()]
        print(f"Tabelas encontradas no banco MySQL 'inventory':")
        for t in tables:
            print(f" - {t}")
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
