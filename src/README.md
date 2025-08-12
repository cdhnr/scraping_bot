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

### Demonstração do script em execução

<p align="center">
  <img src="https://link-para-sua-gif-aqui.gif" alt="scraping_bot em ação" />
</p>
