# 📰 G1 Daily Headline Bot

Este projeto é um bot de automação que captura diariamente a manchete principal do portal G1 e salva em um arquivo de texto neste repositório.

## 🛠️ Tecnologias Utilizadas
- **Python 3.10**
- **Requests & BeautifulSoup4** (Web Scraping)
- **GitHub Actions** (Automação CI/CD)

## ⚙️ Como funciona
1. O **GitHub Actions** dispara o workflow todos os dias às 06:00 (Horário de SP).
2. O script Python acessa o `g1.globo.com`.
3. A manchete principal é extraída e salva em `headline.txt`.
4. O bot faz um **commit** automático salvando o novo arquivo no repositório.

## 📂 Estrutura
- `scraper.py`: Código lógico de extração.
- `.github/workflows/daily_scrape.yml`: Configuração da automação.
- `headline.txt`: Arquivo gerado automaticamente (output).