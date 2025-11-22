import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# Configurações
URL = "https://g1.globo.com/"
# User-Agent é essencial para o site não bloquear o bot achando que é um ataque
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_headline():
    try:
        # 1. Requisição
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status() # Para se der erro 404 ou 500
        
        # 2. Parsing
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 3. Extração (Baseado na estrutura do G1 em 2024/2025)
        # A classe 'feed-post-link' geralmente é o link da matéria principal/destaque
        element = soup.find('a', class_='feed-post-link')
        
        if element:
            title = element.text.strip()
            link = element['href']
            return title, link
        else:
            print("Elemento da manchete não encontrado.")
            return None, None

    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        return None, None

def save_to_file(title, link):
    tz_sp = pytz.timezone('America/Sao_Paulo')
    now = datetime.now(tz_sp).strftime('%Y-%m-%d %H:%M:%S')
    
    content = f"Data: {now}\nManchete: {title}\nLink: {link}\n{'-'*40}\n"
    
    # Modo 'w' sobrescreve o arquivo. Se quiser histórico acumulativo, use 'a' (append)
    with open("headline.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("Arquivo atualizado com sucesso!")

if __name__ == "__main__":
    print("Iniciando scraper...")
    title, link = get_headline()
    
    if title and link:
        print(f"Manchete encontrada: {title}")
        save_to_file(title, link)
    else:
        print("Não foi possível capturar a manchete hoje.")
        # Opcional: sair com erro para o GitHub Actions saber que falhou
        # exit(1)