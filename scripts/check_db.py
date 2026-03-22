import psycopg2

try:
    conn = psycopg2.connect(host="localhost", port=5432, user="admin", password="password", database="analytics")
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = [row[0] for row in cur.fetchall()]
    print(f"Tabelas encontradas no banco PostgreSQL 'analytics':")
    for t in tables:
        print(f" - {t}")
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
