import json

# --- AULA 3: SINTAXE E O "CSS" (COMO SE SUJAR) ---

def test_json(title, json_string):
    print(f"--- TESTANDO: {title} ---")
    print(f"TEXTO: {json_string}")
    try:
        data = json.loads(json_string)
        print("✅ VÁLIDO! O computador entendeu perfeitamente.")
    except json.JSONDecodeError as e:
        print(f"❌ ERRO! O computador parou aqui: {e}")
    print("-" * 30 + "\n")

def aula_sintaxe():
    print("--- 🧠 AULA 3: OS SÍMBOLOS E OS ERROS COMUNS ---\n")

    # 1. O JSON PERFEITO
    # Regras: Chaves em aspas duplas, valores texto em aspas duplas, vírgula só entre itens.
    perfeito = '{"id": 1, "status": "Ativo"}'
    test_json("O JSON Perfeito", perfeito)

    # 2. O ERRO DAS ASPAS SIMPLES (O mais comum!)
    # No JSON, aspas simples ' ' NÃO VALEM para o computador.
    erro_aspas = "{'id': 2, 'status': 'Erro'}"
    test_json("Erro de Aspas Simples", erro_aspas)

    # 3. A VÍRGULA ESQUECIDA
    # Sem vírgula, o computador não sabe que o primeiro item acabou.
    erro_virgula = '{"id": 3 "status": "Erro"}'
    test_json("Erro de Vírgula Faltando", erro_virgula)

    # 4. A VÍRGULA NO FINAL (The Trailing Comma)
    # Colocar uma vírgula depois do último item faz o computador achar que virá algo depois.
    erro_extra = '{"id": 4, "status": "Erro",}'
    test_json("Erro de Vírgula Sobrando", erro_extra)

    # 5. O CASO DO NÚMERO vs TEXTO
    # "100" é texto. 100 é número. JSON sabe a diferença!
    diferente = '{"venda_id": 100, "texto_id": "100"}'
    test_json("Número vs Texto", diferente)

if __name__ == "__main__":
    aula_sintaxe()
