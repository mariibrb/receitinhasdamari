from pathlib import Path

import streamlit as st

from interface import faixa_estampada
from memoria import HORAS, aplicar, hora_local, proxima_saida

st.set_page_config(
    page_title="Livro de receitas congeladas",
    page_icon=":material/menu_book:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.html(Path(__file__).with_name("estilo.css"))
vivos = aplicar(st.session_state)

pagina = st.navigation(
    [
        st.Page("app_pages/receitas.py", title="Receitas", icon=":material/menu_book:", default=True),
        st.Page("app_pages/compras.py", title="No mercado", icon=":material/shopping_cart:", url_path="mercado"),
    ],
    position="top",
)

faixa_estampada()
with st.container(key="tecido"):
    st.title(pagina.title, icon=pagina.icon)
    st.caption("Livro de receitas: produção de congelados.")
    saida = proxima_saida(vivos)
    if saida is None:
        st.caption(
            f"Marque em casa o que já tem. No mercado, abra este mesmo site: "
            f"a marcação dura {HORAS} horas e depois apaga sozinha."
        )
    else:
        st.caption(
            f"A marcação mais antiga sai às {hora_local(saida)}. "
            f"Cada item marcado dura {HORAS} horas."
        )
    pagina.run()
