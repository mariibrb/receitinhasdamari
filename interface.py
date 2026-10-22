"""Pedaços de tela usados nas duas páginas."""

from __future__ import annotations

import streamlit as st

from dados import chave_item
from memoria import definir


def definir_marcacao(ids: list[str], valor: bool) -> None:
    definir(ids, valor)
    for item_id in ids:
        st.session_state[chave_item(item_id)] = valor


def ao_alternar(item_id: str) -> None:
    definir([item_id], bool(st.session_state[chave_item(item_id)]))


def checkbox_item(item: dict) -> None:
    nota = item.get("nota")
    if nota is None and not item["receitas"]:
        nota = "Item da lista de produção, sem ficha detalhada neste livro."
    st.checkbox(
        f"**{item['nome']}** — {item['quantidade']}",
        key=chave_item(item["id"]),
        help=nota,
        width="stretch",
        on_change=ao_alternar,
        args=(item["id"],),
    )


def faixa_estampada() -> None:
    st.html(
        """
        <div style="
          height: 78px;
          border-radius: 24px;
          border: 3px solid #ff7eb6;
          box-shadow: 6px 6px 0 #c9b3ff;
          background-color: #ffe3f3;
          background-image:
            radial-gradient(circle at 10px 10px, #ff6fae 2.6px, transparent 2.8px),
            radial-gradient(circle at 30px 28px, #49c6e8 2.4px, transparent 2.7px),
            linear-gradient(45deg, #ffd0ea 25%, transparent 25%, transparent 75%, #ffd0ea 75%),
            linear-gradient(45deg, #ffd0ea 25%, transparent 25%, transparent 75%, #ffd0ea 75%);
          background-size: 40px 40px, 40px 40px, 26px 26px, 26px 26px;
          background-position: 0 0, 0 0, 0 0, 13px 13px;
        "></div>
        """
    )
