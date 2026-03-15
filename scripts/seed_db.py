import sqlite3
import os

def seed_db():
    db_path = 'data/local.db'
    if not os.path.exists('data'):
        os.makedirs('data')
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        role TEXT DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Insert mock data
    users = [
        ('admin', 'admin@polydb.io', 'administrator'),
        ('jane_doe', 'jane@example.com', 'developer'),
        ('john_smith', 'john@data.com', 'analyst')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO users (username, email, role) VALUES (?, ?, ?)', users)
    
    logs = [
        ('Gateway Started', 'SUCCESS'),
        ('Connection to PostgreSQL established', 'SUCCESS'),
        ('Failed login attempt', 'WARNING'),
        ('Database sync completed', 'SUCCESS')
    ]
    
    cursor.executemany('INSERT INTO system_logs (event, status) VALUES (?, ?)', logs)
    
    conn.commit()
    conn.close()
    print(f"Database {db_path} seeded successfully.")

if __name__ == "__main__":
    seed_db()
