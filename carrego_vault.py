import os
import zipfile
import pyzipper # Requer: pip install pyzipper
from datetime import datetime

def gerar_pacote_carrego(password):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    nome_arquivo = f"PolyDB_Vault_{timestamp}.zip"
    
    # Pastas e arquivos cruciais para o funcionamento
    pastas_obrigatorias = ['SEG', 'scripts', 'docker', 'api']
    arquivos_raiz = ['docker-compose.yml', 'Dockerfile', 'requirements.txt', '.gitignore']

    print(f"🔐 Iniciando Protocolo de Carrego: {nome_arquivo}...")

    with pyzipper.AESZipFile(nome_arquivo, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as vault:
        vault.setpassword(password.encode())

        # Adiciona pastas obrigatórias (incluindo a sensível SEG)
        for pasta in pastas_obrigatorias:
            if os.path.exists(pasta):
                for root, _, files in os.walk(pasta):
                    for file in files:
                        caminho_completo = os.path.join(root, file)
                        vault.write(caminho_completo)
                print(f" ✅ Pasta '{pasta}' encriptada.")

        # Adiciona arquivos de configuração da raiz
        for arq in arquivos_raiz:
            if os.path.exists(arq):
                vault.write(arq)
                print(f" ✅ Arquivo '{arq}' adicionado.")

    print(f"\n🚀 Pronto! O projeto + SEG estão blindados em: {nome_arquivo}")
    print("⚠️  Lembre-se: Nunca envie a senha pelo mesmo canal do arquivo.")

if __name__ == "__main__":
    pwd = input("Defina a senha para o Vault de Carrego: ")
    gerar_pacote_carrego(pwd)