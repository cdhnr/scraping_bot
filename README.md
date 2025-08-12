# Automação de consulta de frete e prazo

## Descrição
Raspador que abre cada URL de produto, insere CEPs (lista em `utils/ceps.py`), consulta frete/prazo na página e salva tudo em `raspagem/bd.xlsx`. Usa Playwright (API síncrona) para automação do navegador e pandas + openpyxl para exportar Excel.

> Atenção: o código contém vários `# Preencher o Xpath`. Você mesmo deve preencher com os seletores corretos.

---

## Estrutura sugerida de pastas
```
README.md
LICENSE
src/
├── app.py
├── README.md
├── utils/
│   ├── ceps.py        # dicionário ceps_gerais = {...}
│   └── urls.py        # lista urls_produtos = [...]
├── raspagem/
│   └── bd.xlsx  # output
├── requirements.txt
```

---

## Dependências (mínimas)
Adicione no arquivo `requirements.txt`:
```
playwright
pandas
openpyxl
```

---

## Instalação (passo a passo)
1. Crie e ative virtualenv:
   - Linux/macOS:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Instale navegadores do Playwright:
   ```bash
   playwright install
   ```
4. Execute o script:
   ```bash
   python app.py
   ```

---

## Configurações importantes (no código)
Defina variáveis para facilitar manutenção:
```python
HEADLESS = False        # True para rodar sem abrir navegador
NAV_TIMEOUT = 25000     # Timeout em ms para navegação
SHORT_WAIT = 1          # Delay em segundos entre ações
LONG_TIMEOUT = 10000    # Timeout para espera de elementos
OUTPUT_PATH = "raspagem/bd.xlsx"
```

---

## Encontrar e preencher seletores (XPaths / CSS)
- Abra a página alvo no navegador.
- Use DevTools (F12) → inspect → clique com botão direito no elemento → Copy → Copy selector (ou Copy XPath).
- Cole os seletores nos lugares marcados no código (`page.fill()`, `page.click()`, `page.wait_for_selector()`, `page.locator()`).
- Prefira seletores estáveis, não classes dinâmicas.

---

## Boas práticas
- Use `try/except` para cada CEP, evitando abortar todo o processo.
- Adicione retries em caso de erro.
- Randomize delays para evitar bloqueios.
- Teste com 1 produto e 1 CEP antes de rodar tudo.

---

## Debugging rápido
- Rodar com navegador visível:
```python
browser = p.chromium.launch(headless=False, slow_mo=80)
```
- Ajustar timeouts e delays.
- Testar seletores no DevTools.

---

## Problemas comuns
- Timeout: aumenta timeout, checa seletor.
- Selector vazio: seletor errado ou conteúdo carregado depois, aumente espera.
- Excel corrompido: tente salvar CSV.

---

## Melhorias futuras para pensar
- Versão assíncrona com asyncio para ganho de performance.
- Paralelizar scraping com múltiplos contextos ou threads.
- Lidar com recaptcha, bloqueios e proteções anti-bot.
- Validar e padronizar dados extraídos para garantir qualidade.
- Testes unitários para garantir estabilidade.
- Detectar e classificar tipos de frete (grátis, expresso, agendado, normal, etc).

---
