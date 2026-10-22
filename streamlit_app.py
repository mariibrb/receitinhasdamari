from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Livro de receitas congeladas",
    page_icon=":material/menu_book:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.html(Path(__file__).with_name("estilo.css"))

pagina = st.navigation(
    [
        st.Page("app_pages/receitas.py", title="Receitas", icon=":material/menu_book:", default=True),
        st.Page("app_pages/compras.py", title="No mercado", icon=":material/shopping_cart:", url_path="mercado"),
    ],
    position="top",
)

with st.container(key="tecido"):
    st.title(pagina.title, icon=pagina.icon)
    st.caption("Livro de receitas: produção de congelados.")
    pagina.run()
