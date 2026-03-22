import pymysql
import json

def get_device_as_json():
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="user", password="password", database="inventory")
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM devices LIMIT 1")
            result = cursor.fetchone()
            
            # Formata o resultado como JSON bonito (com indentação)
            json_data = json.dumps(result, indent=2, default=str)
            print("--- BANCO DE DADOS (LINHA TABULAR) ---")
            print(result) # Isso vai mostrar como um dicionário Python (similar à linha do banco)
            print("\n--- JSON PARA O PROGRAMADOR ---")
            print(json_data)
            
        conn.close()
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    get_device_as_json()
