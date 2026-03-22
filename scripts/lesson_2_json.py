import json

# --- AULA 2: A FÁBRICA DE JSON ---

def aula_pratica_json():
    print("--- 📚 AULA 2: CRIANDO E LENDO JSON ---\n")

    # 1. PEÇAS DO QUEBRA-CABEÇA (Variáveis no Código)
    # Imaginamos que o programador tem estas informações de uma nova venda:
    produto = "Plano Bronze v1"
    quantidade = 2
    preco_unitario = 99.90
    cliente_vip = True
    tags = ["software", "assinatura", "cloud"]

    # 2. MONTANDO O JSON (O "DUMPS")
    # O programador usa o comando 'json.dumps' para 'carimbar' as informações num texto JSON.
    # É isso aqui que vai ser enviado pela internet!
    
    dados_venda = {
        "nome_produto": produto,
        "qtd": quantidade,
        "valor_unitario": preco_unitario,
        "is_vip": cliente_vip,
        "categorias": tags
    }

    print("⚠️ PASSO 1: O Programador prepara os dados no código:")
    print(dados_venda)
    print("\n-------------------------------------------")

    # Transforma o dicionário em uma STRING JSON (um texto corrido)
    texto_json_enviado = json.dumps(dados_venda, indent=4, ensure_ascii=False)

    print("⚡ PASSO 2: O 'JSON' pronto para ser enviado (virei um texto!):")
    print(texto_json_enviado)
    print("\n-------------------------------------------")

    # 3. RECEBENDO E LENDO O JSON (O "LOADS")
    # Quando o outro lado (o servidor) recebe esse texto, ele usa 'json.loads' para 'ler' o JSON.
    
    dados_recebidos = json.loads(texto_json_enviado)

    print("📖 PASSO 3: O Servidor leu o JSON e agora entende cada parte:")
    print(f"Nome do Produto: {dados_recebidos['nome_produto']}")
    print(f"Valor Total: R$ {dados_recebidos['qtd'] * dados_recebidos['valor_unitario']:.2f}")

if __name__ == "__main__":
    aula_pratica_json()
