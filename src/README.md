## Fluxo do script
1. Lê `ceps` e `urls_produtos`.
2. Abre Playwright e cria página.
3. Para cada URL de produto:
   - Abre a página.
   - Para cada CEP:
     - Remove frete antigo (se existir).
     - Preenche CEP.
     - Clica em consultar.
     - Espera resultado.
     - Extrai frete, prazo e nome do produto.
     - Armazena em lista.
4. Salva resultados em Excel.
5. Exibe dados no terminal.

<p align="center">
Demonstração do script em execução.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d936c5da-e4f1-4bae-b6bb-dbaf2bd5e741" alt="scraping_bot em ação" width="800"/>
</p>
