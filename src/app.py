import pandas as pd  # Manipulação de dados (Excel, DataFrame etc)
import time  # Pausa entre ações
from playwright.sync_api import sync_playwright

from utils.ceps import ceps_gerais  # Dicionário com CEPs por cidade
from utils.urls import urls_produtos  # Lista com URLs de produtos

# Junta os CEPs em um dicionário (caso queira adicionar mais de uma fonte depois)
ceps = {**ceps_gerais}
raspagem = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    for url in urls_produtos:
        page.goto(url, timeout=25000)  # Abre a página do produto

        for cep in ceps:
            # Remove frete anterior (se aparecer o botão de remover)
            try:
                page.click('') # Preencher o Xpath
            except:
                pass  # Ignora se não tiver nada pra remover

            try:
                # Espera o campo de CEP carregar e preenche
                time.sleep(1)
                page.wait_for_selector('', timeout=1000) # Preencher o Xpath
                page.fill('', cep) # Preencher o Xpath

                # Clica no botão "Consultar"
                page.wait_for_selector('', timeout=500) # Preencher o Xpath
                page.click('') # Preencher o Xpath

                # Espera os resultados aparecerem
                page.wait_for_selector('', timeout=10000) # Preencher o Xpath
                page.wait_for_selector('', timeout=10000) # Preencher o Xpath

                # Extrai os dados de frete, prazo e nome do produto
                frete = page.locator('').first.text_content().strip() # Preencher o Xpath
                prazo = page.locator('').first.text_content().strip() # Preencher o Xpath
                nomeProduto = page.locator('').first.text_content().strip() # Preencher o Xpath

            except Exception as e:
                print(f"Erro ao buscar CEP {cep} para URL {url}: {e}")
                frete, prazo, nomeProduto = "Erro", "Erro", "Erro"

            # Armazena os dados obtidos
            raspagem.append({
                "Produto": nomeProduto,
                "Prazo": prazo,
                "Frete": frete,
                "CEP": cep,
            })

# Salva o resultado num Excel
df = pd.DataFrame(raspagem)
df.to_excel("raspagem/bd.xlsx", index=False)

# Mostra no terminal o que foi raspado
print(raspagem)
print("Raspagem concluída com sucesso.")