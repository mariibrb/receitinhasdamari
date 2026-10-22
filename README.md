# Livro de receitas congeladas

App para consultar as fichas de produção de congelados e marcar a lista de compras no mercado.

## Rodar no computador

```bash
uv venv --python 3.13
uv pip install -r requirements.txt
uv run --python .venv streamlit run streamlit_app.py
```

Se o ambiente já existir:

```bash
.venv\Scripts\streamlit run streamlit_app.py
```

## Publicar no Streamlit

1. Crie um repositório público no GitHub e envie esta pasta (sem a pasta `.venv`).
2. Entre em [share.streamlit.io](https://share.streamlit.io) com a mesma conta do GitHub.
3. Em **Create app**, escolha o repositório, o branch `main` e o arquivo `streamlit_app.py`.
4. Clique em **Deploy**. O app usa o `requirements.txt`.

Em **No mercado**, escolha as receitas e a quantidade de cada recheio. A lista soma só isso. Marque o que já tem hoje e baixe o arquivo para abrir no celular, mesmo fora do Wi-Fi de casa. A marcação dura 4 horas.
