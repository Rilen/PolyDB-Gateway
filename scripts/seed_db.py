import sqlite3
import os

def create_db(name, data_list):
    path = f'data/{name}.db'
    if not os.path.exists('data'):
        os.makedirs('data')
        
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    
    # Tabela Genérica para Demo
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS demo_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        value REAL,
        category TEXT
    )
    ''')
    
    cursor.executemany('INSERT INTO demo_table (name, value, category) VALUES (?, ?, ?)', data_list)
    conn.commit()
    conn.close()
    print(f"Banco {path} criado com sucesso.")

if __name__ == "__main__":
    # Dados para o "Simulador de Postgres"
    pg_data = [('Faturamento Jan', 15000.50, 'Financeiro'), ('Faturamento Fev', 18200.00, 'Financeiro')]
    create_db('postgres_prod', pg_data)
    
    # Dados para o "Simulador de MySQL"
    my_data = [('Sensor A', 22.5, 'IoT'), ('Sensor B', 24.1, 'IoT')]
    create_db('mysql_inventory', my_data)
    
    # Dados para o SQLite Local
    sq_data = [('Cache 1', 1.0, 'System'), ('Cache 2', 2.0, 'System')]
    create_db('local', sq_data)
