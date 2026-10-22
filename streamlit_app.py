from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Livro de receitas congeladas",
    page_icon=":material/menu_book:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

raiz = Path(__file__).resolve().parent
st.html(raiz / "estilo.css")

receitas = raiz / "app_pages" / "receitas.py"
compras = raiz / "app_pages" / "compras.py"
faltando = [
    caminho.name
    for caminho in (receitas, compras, raiz / "dados.py", raiz / "plano.py", raiz / "estilo.css")
    if not caminho.is_file()
]
if faltando:
    st.error(
        "Estes arquivos não estão na pasta publicada do app: "
        + ", ".join(faltando)
        + ". Eles ficam junto de streamlit_app.py e precisam ir para o GitHub."
    )
    st.stop()

pagina = st.navigation(
    [
        st.Page(receitas, title="Receitas", icon=":material/menu_book:", default=True),
        st.Page(compras, title="No mercado", icon=":material/shopping_cart:", url_path="mercado"),
    ],
    position="top",
)

with st.container(key="tecido"):
    st.title(pagina.title, icon=pagina.icon)
    st.caption("Livro de receitas: produção de congelados.")
    pagina.run()
