"""Monta a lista a partir das receitas, do recheio e da quantidade."""

from __future__ import annotations

import time
from html import escape

from dados import CATEGORIAS, titulo_receita

HORAS = 4
SEGUNDOS = HORAS * 60 * 60

APELIDOS = {
    "vulcao": "Vulcão",
    "panqueca": "Panqueca",
    "escondidinho": "Escondidinho",
    "esfirras": "Esfirras",
    "pastel": "Pastel",
    "pizza": "Mini pizza",
    "bandas": "Pão recheado",
    "hamburguer": "Hambúrguer",
    "almondega": "Almôndega",
    "bolo_cenoura": "Bolo de cenoura",
    "bolo_banana": "Bolo de banana",
    "bolo_nega": "Nega maluca",
    "bolo_laranja": "Bolo de laranja",
    "bolo_coco": "Bolo de coco",
    "palha": "Palha italiana",
    "pudim": "Mini pudim",
    "brigadeiro": "Brigadeiro",
}

ORDEM = list(APELIDOS)


def item(ident: str, nome: str, qtd: float | None, unidade: str, categoria: str) -> dict:
    return {
        "id": ident,
        "nome": nome,
        "qtd": qtd,
        "unidade": unidade,
        "categoria": categoria,
    }


def gosto(ident: str, nome: str, categoria: str) -> dict:
    return item(ident, nome, None, "a gosto", categoria)


def _recheio(ident: str, nome: str, itens: list[dict]) -> dict:
    return {"id": ident, "nome": nome, "itens": itens}


FICHAS = {
    "vulcao": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("carne_moida", "Carne moída (patinho ou acém)", 700, "g", "acougue"),
            item("batata", "Batata inglesa", 800, "g", "hortifruti"),
            item("mucarela", "Queijo muçarela", 150, "g", "laticinios"),
            item("cebola", "Cebola", 0.5, "unidade", "hortifruti"),
            item("alho", "Alho", 2, "dente", "hortifruti"),
            item("manteiga", "Manteiga", 22, "g", "laticinios"),
            item("leite", "Leite integral", 50, "ml", "laticinios"),
            gosto("cheiro", "Cheiro-verde", "hortifruti"),
            gosto("sal", "Sal", "mercearia"),
            gosto("pimenta", "Pimenta-do-reino", "mercearia"),
        ],
        "recheios": [],
    },
    "panqueca": {
        "modo": "por_recheio",
        "rotulo_base": "Fornadas",
        "base": [
            item("espinafre", "Espinafre", 300, "g", "hortifruti"),
            item("refogado", "Refogado de legumes (cenoura, abobrinha e chuchu)", 200, "g", "hortifruti"),
            item("leite", "Leite integral", 240, "ml", "laticinios"),
            item("farinha", "Farinha de trigo", 120, "g", "mercearia"),
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("cebola", "Cebola", 0.5, "unidade", "hortifruti"),
            item("alho", "Alho", 2, "dente", "hortifruti"),
            gosto("azeite", "Azeite", "mercearia"),
            gosto("sal", "Sal", "mercearia"),
            gosto("pimenta", "Pimenta-do-reino", "mercearia"),
        ],
        "recheios": [
            _recheio("frango", "Frango desfiado", [item("frango", "Frango desfiado", 400, "g", "acougue")]),
            _recheio("carne", "Carne moída", [item("carne_moida", "Carne moída (patinho ou acém)", 400, "g", "acougue")]),
        ],
    },
    "escondidinho": {
        "modo": "por_recheio",
        "rotulo_base": "Fornadas",
        "base": [
            item("batata", "Batata inglesa", 700, "g", "hortifruti"),
            item("refogado", "Refogado de legumes (cenoura, abobrinha e chuchu)", 150, "g", "hortifruti"),
            item("mucarela", "Queijo muçarela", 150, "g", "laticinios"),
            item("requeijao", "Requeijão culinário", 100, "g", "laticinios"),
            item("azeitona", "Azeitona", 50, "g", "mercearia"),
            item("molho_tomate", "Molho ou extrato de tomate", 0.5, "sachê", "mercearia"),
            item("manteiga", "Manteiga", 15, "g", "laticinios"),
            item("leite", "Leite integral", 50, "ml", "laticinios"),
            gosto("sal", "Sal", "mercearia"),
        ],
        "recheios": [
            _recheio("frango", "Frango desfiado", [item("frango", "Frango desfiado", 400, "g", "acougue")]),
            _recheio("carne", "Carne moída", [item("carne_moida", "Carne moída (patinho ou acém)", 400, "g", "acougue")]),
        ],
    },
    "esfirras": {
        "modo": "compartilhada",
        "rotulo_base": "Fornadas da massa",
        "base": [
            item("farinha", "Farinha de trigo", 500, "g", "mercearia"),
            item("fermento_bio", "Fermento biológico seco", 10, "g", "mercearia"),
            item("acucar", "Açúcar", 12, "g", "mercearia"),
            item("oleo", "Óleo", 45, "ml", "mercearia"),
            item("agua", "Água", 250, "ml", "mercearia"),
            gosto("sal", "Sal", "mercearia"),
        ],
        "recheios": [
            _recheio(
                "carne",
                "Carne (8 abertas)",
                [
                    item("carne_moida", "Carne moída (patinho ou acém)", 300, "g", "acougue"),
                    item("tomate", "Tomate", 1, "unidade", "hortifruti"),
                    item("cebola", "Cebola", 0.5, "unidade", "hortifruti"),
                    gosto("pimenta", "Pimenta-do-reino", "mercearia"),
                    gosto("limao", "Limão", "hortifruti"),
                ],
            ),
            _recheio(
                "frango",
                "Frango cremoso (8 fechadas)",
                [
                    item("frango", "Frango desfiado", 300, "g", "acougue"),
                    item("milho", "Milho verde", 0.5, "lata", "mercearia"),
                    item("requeijao", "Requeijão culinário", 150, "g", "laticinios"),
                    gosto("cheiro", "Cheiro-verde", "hortifruti"),
                ],
            ),
            _recheio(
                "calabresa",
                "Calabresa (7 abertas)",
                [
                    item("calabresa", "Linguiça calabresa", 400, "g", "acougue"),
                    item("cebola", "Cebola", 1, "unidade", "hortifruti"),
                    item("requeijao", "Requeijão culinário", 100, "g", "laticinios"),
                ],
            ),
            _recheio(
                "brocolis",
                "Brócolis com queijo (7 fechadas)",
                [
                    item("brocolis", "Brócolis", 500, "g", "hortifruti"),
                    item("alho", "Alho", 2, "dente", "hortifruti"),
                    item("mucarela", "Queijo muçarela", 150, "g", "laticinios"),
                    gosto("azeite", "Azeite", "mercearia"),
                ],
            ),
        ],
    },
    "pastel": {
        "modo": "por_recheio",
        "rotulo_base": "Fornadas",
        "base": [item("discos_pastel", "Discos de pastel", 20, "unidade", "paes")],
        "recheios": [
            _recheio(
                "carne_azeitona",
                "Carne com azeitona",
                [
                    item("carne_moida", "Carne moída (patinho ou acém)", 150, "g", "acougue"),
                    item("tomate", "Tomate", 1, "unidade", "hortifruti"),
                    item("azeitona", "Azeitona", 30, "g", "mercearia"),
                ],
            ),
            _recheio(
                "carne_cheddar",
                "Carne com cheddar",
                [
                    item("carne_moida", "Carne moída (patinho ou acém)", 150, "g", "acougue"),
                    item("cheddar", "Queijo cheddar", 100, "g", "laticinios"),
                    item("cebola", "Cebola", 1, "unidade", "hortifruti"),
                ],
            ),
            _recheio(
                "frango_milho",
                "Frango com milho",
                [
                    item("frango", "Frango desfiado", 150, "g", "acougue"),
                    item("milho", "Milho verde", 0.5, "lata", "mercearia"),
                    item("requeijao", "Requeijão culinário", 80, "g", "laticinios"),
                ],
            ),
            _recheio(
                "presunto_queijo",
                "Presunto e queijo",
                [
                    item("presunto", "Presunto", 100, "g", "acougue"),
                    item("mucarela", "Queijo muçarela", 100, "g", "laticinios"),
                    gosto("oregano", "Orégano", "mercearia"),
                ],
            ),
            _recheio(
                "palmito",
                "Palmito",
                [
                    item("palmito", "Palmito", 300, "g", "mercearia"),
                    item("alho", "Alho", 1, "dente", "hortifruti"),
                    item("cebola", "Cebola", 1, "unidade", "hortifruti"),
                    item("molho_tomate", "Molho ou extrato de tomate", 0.5, "sachê", "mercearia"),
                    item("requeijao", "Requeijão culinário", 80, "g", "laticinios"),
                ],
            ),
        ],
    },
    "pizza": {
        "modo": "compartilhada",
        "rotulo_base": "Fornadas dos discos",
        "base": [
            item("discos_pizza", "Discos de mini pizza pré-assados", 8, "unidade", "paes"),
            item("molho_tomate", "Molho ou extrato de tomate", 0.5, "sachê", "mercearia"),
            item("tomate", "Tomate", 1, "unidade", "hortifruti"),
            gosto("milho", "Milho verde", "mercearia"),
            gosto("oregano", "Orégano", "mercearia"),
        ],
        "recheios": [
            _recheio(
                "presunto",
                "Presunto e muçarela",
                [
                    item("presunto", "Presunto", 100, "g", "acougue"),
                    item("mucarela", "Queijo muçarela", 150, "g", "laticinios"),
                ],
            ),
            _recheio(
                "frango",
                "Frango com requeijão",
                [
                    item("frango", "Frango desfiado", 150, "g", "acougue"),
                    item("requeijao", "Requeijão culinário", 150, "g", "laticinios"),
                ],
            ),
        ],
    },
    "bandas": {
        "modo": "compartilhada",
        "rotulo_base": "Fornadas dos pães",
        "base": [item("pao", "Pão francês", 15, "unidade", "paes")],
        "recheios": [
            _recheio(
                "louca",
                "Carne louca (10 bandas)",
                [
                    item("lagarto", "Lagarto ou fraldinha", 1500, "g", "acougue"),
                    item("cebola", "Cebola", 2, "unidade", "hortifruti"),
                    item("tomate", "Tomate", 2, "unidade", "hortifruti"),
                    item("molho_tomate", "Molho ou extrato de tomate", 1, "sachê", "mercearia"),
                ],
            ),
            _recheio(
                "pernil",
                "Pernil barbecue (8 bandas)",
                [
                    item("pernil", "Pernil suíno", 1200, "g", "acougue"),
                    item("cebola", "Cebola", 1, "unidade", "hortifruti"),
                    item("alho", "Alho", 2, "dente", "hortifruti"),
                    item("barbecue", "Molho barbecue", 150, "ml", "mercearia"),
                    item("shoyu", "Molho shoyu", 50, "ml", "mercearia"),
                ],
            ),
            _recheio(
                "misto",
                "Misto (6 bandas)",
                [
                    item("presunto", "Presunto", 150, "g", "acougue"),
                    item("mucarela", "Queijo muçarela", 150, "g", "laticinios"),
                    item("tomate", "Tomate", 1, "unidade", "hortifruti"),
                    gosto("oregano", "Orégano", "mercearia"),
                ],
            ),
            _recheio(
                "peru",
                "Peito de peru (6 bandas)",
                [
                    item("peru", "Peito de peru", 200, "g", "acougue"),
                    item("cream", "Cream cheese", 200, "g", "laticinios"),
                    item("azeitona", "Azeitona", 50, "g", "mercearia"),
                ],
            ),
        ],
    },
    "hamburguer": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("carne_moida", "Carne moída (patinho ou acém)", 1000, "g", "acougue"),
            gosto("sal", "Sal", "mercearia"),
            gosto("pimenta", "Pimenta-do-reino", "mercearia"),
            gosto("azeite", "Azeite", "mercearia"),
        ],
        "recheios": [],
    },
    "almondega": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("carne_moida", "Carne moída (patinho ou acém)", 500, "g", "acougue"),
            item("mucarela", "Queijo muçarela", 100, "g", "laticinios"),
            item("cebola", "Cebola", 0.5, "unidade", "hortifruti"),
            item("alho", "Alho", 1, "dente", "hortifruti"),
            gosto("cheiro", "Cheiro-verde", "hortifruti"),
            gosto("sal", "Sal", "mercearia"),
        ],
        "recheios": [],
    },
    "bolo_cenoura": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("cenoura", "Cenoura", 150, "g", "hortifruti"),
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("oleo", "Óleo", 80, "ml", "mercearia"),
            item("acucar", "Açúcar", 200, "g", "mercearia"),
            item("farinha", "Farinha de trigo", 150, "g", "mercearia"),
            item("fermento_po", "Fermento em pó", 8, "g", "mercearia"),
            item("cacau", "Cacau ou achocolatado", 100, "g", "mercearia"),
            item("manteiga", "Manteiga", 20, "g", "laticinios"),
            item("leite", "Leite integral", 30, "ml", "laticinios"),
        ],
        "recheios": [],
    },
    "bolo_banana": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("banana", "Banana madura", 300, "g", "hortifruti"),
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("oleo", "Óleo", 50, "ml", "mercearia"),
            item("acucar_mascavo", "Açúcar mascavo", 50, "g", "mercearia"),
            item("aveia", "Aveia em flocos finos", 100, "g", "mercearia"),
            item("canela", "Canela em pó", 5, "g", "mercearia"),
            item("fermento_po", "Fermento em pó", 8, "g", "mercearia"),
        ],
        "recheios": [],
    },
    "bolo_nega": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("oleo", "Óleo", 100, "ml", "mercearia"),
            item("acucar", "Açúcar", 150, "g", "mercearia"),
            item("cacau", "Cacau ou achocolatado", 80, "g", "mercearia"),
            item("farinha", "Farinha de trigo", 150, "g", "mercearia"),
            item("agua", "Água", 100, "ml", "mercearia"),
            item("fermento_po", "Fermento em pó", 8, "g", "mercearia"),
        ],
        "recheios": [],
    },
    "bolo_laranja": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("laranja", "Laranja pera", 2, "unidade", "hortifruti"),
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("oleo", "Óleo", 80, "ml", "mercearia"),
            item("acucar", "Açúcar", 200, "g", "mercearia"),
            item("farinha", "Farinha de trigo", 150, "g", "mercearia"),
            item("fermento_po", "Fermento em pó", 8, "g", "mercearia"),
        ],
        "recheios": [],
    },
    "bolo_coco": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("ovos", "Ovos", 2, "unidade", "laticinios"),
            item("acucar", "Açúcar", 120, "g", "mercearia"),
            item("farinha", "Farinha de trigo", 100, "g", "mercearia"),
            item("leite", "Leite integral", 100, "ml", "laticinios"),
            item("fermento_po", "Fermento em pó", 5, "g", "mercearia"),
            item("condensado", "Leite condensado", 0.4, "lata", "paes"),
            item("leite_coco", "Leite de coco", 100, "ml", "mercearia"),
            item("coco", "Coco ralado", 50, "g", "mercearia"),
        ],
        "recheios": [],
    },
    "palha": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("condensado", "Leite condensado", 1, "lata", "paes"),
            item("creme", "Creme de leite", 1, "caixinha", "paes"),
            item("cacau", "Cacau ou achocolatado", 24, "g", "mercearia"),
            item("manteiga", "Manteiga", 15, "g", "laticinios"),
            item("biscoito", "Biscoito maisena", 150, "g", "mercearia"),
        ],
        "recheios": [],
    },
    "pudim": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("condensado", "Leite condensado", 1, "lata", "paes"),
            item("leite", "Leite integral", 395, "ml", "laticinios"),
            item("ovos", "Ovos", 3, "unidade", "laticinios"),
            item("acucar", "Açúcar", 180, "g", "mercearia"),
            item("agua", "Água", 120, "ml", "mercearia"),
        ],
        "recheios": [],
    },
    "brigadeiro": {
        "modo": "so",
        "rotulo_base": "Fornadas",
        "base": [
            item("condensado", "Leite condensado", 1, "lata", "paes"),
            item("creme", "Creme de leite", 0.5, "caixinha", "paes"),
            item("cacau", "Cacau ou achocolatado", 24, "g", "mercearia"),
            item("manteiga", "Manteiga", 15, "g", "laticinios"),
            item("granulado", "Granulado", 100, "g", "mercearia"),
        ],
        "recheios": [],
    },
}

def apelido(receita_id: str) -> str:
    return APELIDOS.get(receita_id, receita_id)


def nome_recheio(receita_id: str, recheio_id: str) -> str:
    for recheio in FICHAS[receita_id]["recheios"]:
        if recheio["id"] == recheio_id:
            return recheio["nome"]
    return ""


def recheio_valido(receita_id: str, recheio_id: str) -> str:
    opcoes = [recheio["id"] for recheio in FICHAS[receita_id]["recheios"]]
    if recheio_id in opcoes:
        return recheio_id
    return opcoes[0] if opcoes else ""


def _numero(valor: float) -> str:
    if abs(valor - round(valor)) < 0.05:
        return str(int(round(valor)))
    if abs(valor - int(valor) - 0.5) < 0.05:
        inteiro = int(valor)
        return "1/2" if inteiro == 0 else f"{inteiro} e 1/2"
    texto = f"{valor:.1f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")


def _plural(qtd: float, unidade: str) -> str:
    if unidade == "colher":
        return "colher (sopa)" if qtd <= 1.001 else "colheres (sopa)"
    if qtd <= 1.001:
        return unidade
    return {
        "unidade": "unidades",
        "dente": "dentes",
        "maço": "maços",
        "lata": "latas",
        "caixinha": "caixinhas",
        "pacote": "pacotes",
        "sachê": "sachês",
    }.get(unidade, unidade)


def formatar_qtd(qtd: float | None, unidade: str) -> str:
    if qtd is None:
        return "a gosto"
    if unidade == "g":
        if qtd >= 1000:
            return f"{_numero(qtd / 1000)} kg"
        return f"{_numero(qtd)} g"
    if unidade == "ml":
        if qtd >= 1000:
            return f"{_numero(qtd / 1000)} L"
        return f"{_numero(qtd)} ml"
    return f"{_numero(qtd)} {_plural(qtd, unidade)}"


def _escala(brutos: list[dict], vezes: int) -> list[dict]:
    if vezes <= 0:
        return []
    saida = []
    for bruto in brutos:
        qtd = None if bruto["qtd"] is None else bruto["qtd"] * vezes
        saida.append({**bruto, "qtd": qtd})
    return saida


def itens_da_escolha(escolha: dict) -> list[dict]:
    ficha = FICHAS[escolha["id"]]
    recheios = escolha.get("recheios") or {}
    if ficha["modo"] == "por_recheio":
        saida = []
        for recheio in ficha["recheios"]:
            vezes = int(recheios.get(recheio["id"]) or 0)
            saida.extend(_escala(ficha["base"], vezes))
            saida.extend(_escala(recheio["itens"], vezes))
        return saida
    saida = _escala(ficha["base"], int(escolha.get("fornadas") or 1))
    for recheio in ficha["recheios"]:
        vezes = int(recheios.get(recheio["id"]) or 0)
        saida.extend(_escala(recheio["itens"], vezes))
    return saida


def montar(escolhas: list[dict]) -> list[dict]:
    totais: dict[str, dict] = {}
    for escolha in escolhas:
        if escolha["id"] not in FICHAS:
            continue
        for bruto in itens_da_escolha(escolha):
            atual = totais.get(bruto["id"])
            if atual is None:
                totais[bruto["id"]] = dict(bruto)
                continue
            if atual["qtd"] is None and bruto["qtd"] is not None:
                atual["qtd"] = bruto["qtd"]
                atual["unidade"] = bruto["unidade"]
            elif bruto["qtd"] is not None and atual["qtd"] is not None:
                atual["qtd"] += bruto["qtd"]
    ordem = {categoria["id"]: indice for indice, categoria in enumerate(CATEGORIAS)}
    return sorted(totais.values(), key=lambda atual: (ordem.get(atual["categoria"], 99), atual["nome"]))


def resumir_escolha(escolha: dict) -> str:
    ficha = FICHAS[escolha["id"]]
    ativos = [
        f"{nome_recheio(escolha['id'], rid)} × {qtd}"
        for rid, qtd in (escolha.get("recheios") or {}).items()
        if int(qtd) > 0
    ]
    if ficha["modo"] == "por_recheio":
        if not ativos:
            return f"{apelido(escolha['id'])} sem recheio"
        return f"{apelido(escolha['id'])}: {', '.join(ativos)}"
    fornadas = int(escolha.get("fornadas") or 1)
    texto = f"{fornadas} fornada" if fornadas == 1 else f"{fornadas} fornadas"
    texto += f" de {apelido(escolha['id'])}"
    if ativos:
        texto += f" ({', '.join(ativos)})"
    return texto


def parse_plano(texto: str) -> list[dict]:
    if not texto:
        return []
    saida = []
    for parte in texto.split("|"):
        pedacos = parte.split(":")
        if not pedacos or pedacos[0] not in FICHAS:
            continue
        receita_id = pedacos[0]
        fornadas = int(pedacos[1]) if len(pedacos) > 1 and pedacos[1].isdigit() else 1
        fornadas = min(12, max(1, fornadas))
        terceiro = pedacos[2] if len(pedacos) > 2 else ""
        conhecidos = {recheio["id"] for recheio in FICHAS[receita_id]["recheios"]}
        recheios: dict[str, int] = {}
        if terceiro and "*" not in terceiro and "," not in terceiro:
            if terceiro in conhecidos:
                recheios[terceiro] = fornadas
        else:
            for par in terceiro.split(","):
                if "*" not in par:
                    continue
                rid, qtd = par.split("*", 1)
                if rid in conhecidos and qtd.isdigit():
                    recheios[rid] = min(12, max(0, int(qtd)))
        saida.append({"id": receita_id, "fornadas": fornadas, "recheios": recheios})
    return saida


def serializar_plano(escolhas: list[dict]) -> str:
    partes = []
    for escolha in escolhas:
        pares = ",".join(
            f"{rid}*{int(qtd)}"
            for rid, qtd in (escolha.get("recheios") or {}).items()
            if int(qtd) > 0
        )
        partes.append(f"{escolha['id']}:{int(escolha['fornadas'])}:{pares}")
    return "|".join(partes)


def linhas_ficha(receita_id: str) -> list[str]:
    ficha = FICHAS[receita_id]
    if ficha["modo"] == "por_recheio":
        linhas = ["**Base de cada recheio**"]
    else:
        linhas = ["**Base de 1 fornada**"]
    linhas.extend(
        f"- {bruto['nome']}: {formatar_qtd(bruto['qtd'], bruto['unidade'])}" for bruto in ficha["base"]
    )
    for recheio in ficha["recheios"]:
        linhas.append(f"**{recheio['nome']}**")
        linhas.extend(
            f"- {bruto['nome']}: {formatar_qtd(bruto['qtd'], bruto['unidade'])}" for bruto in recheio["itens"]
        )
    return linhas


def texto_compra(lista: list[dict], tenho: set[str]) -> str:
    linhas = ["Para comprar no mercado", ""]
    for categoria in CATEGORIAS:
        grupo = [
            atual
            for atual in lista
            if atual["categoria"] == categoria["id"] and atual["id"] not in tenho
        ]
        if not grupo:
            continue
        linhas.append(categoria["titulo"])
        linhas.extend(
            f"[ ] {atual['nome']}: {formatar_qtd(atual['qtd'], atual['unidade'])}" for atual in grupo
        )
        linhas.append("")
    if len(linhas) == 2:
        return "Nada para comprar. Tudo desta lista já está marcado como em casa.\n"
    return "\n".join(linhas).rstrip() + "\n"


def html_lista(lista: list[dict], tenho: set[str], ate: int, resumo: str) -> str:
    blocos = []
    for categoria in CATEGORIAS:
        grupo = [atual for atual in lista if atual["categoria"] == categoria["id"]]
        if not grupo:
            continue
        linhas = [f"<h2>{escape(categoria['titulo'])}</h2>"]
        for atual in grupo:
            ja_tem = atual["id"] in tenho
            marcado = " checked" if ja_tem else ""
            classe = " tenho" if ja_tem else ""
            estado = "Já tenho" if ja_tem else "Comprar"
            qtd = formatar_qtd(atual["qtd"], atual["unidade"])
            linhas.append(
                f"<label class='{classe.strip()}'>"
                f"<input type='checkbox' id='{escape(atual['id'])}'{marcado}>"
                f"<span class='nome'><strong>{escape(atual['nome'])}</strong> — {escape(qtd)}</span>"
                f"<em>{estado}</em>"
                "</label>"
            )
        blocos.append(f"<section class='{escape(categoria['id'])}'>{''.join(linhas)}</section>")
    hora = time.strftime("%H:%M", time.localtime(ate)) if ate else ""
    aviso = f"Marcações feitas em casa valem até {hora}." if ate else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lista do mercado</title>
<style>
body {{
  margin: 0;
  color: #3d2c24;
  background: #f7c3d4;
  font-family: "Segoe UI", sans-serif;
}}
main {{
  width: 100%;
  max-width: none;
  margin: 0;
  padding: 16px 16px 32px;
  box-sizing: border-box;
}}
.folha {{
  background-color: #fff;
  background-image:
    linear-gradient(#fffefb, #fffefb),
    linear-gradient(90deg, rgba(226, 92, 130, 0.42) 50%, transparent 50%),
    linear-gradient(rgba(226, 92, 130, 0.42) 50%, transparent 50%);
  background-size: auto, 8px 8px, 8px 8px;
  background-repeat: no-repeat, repeat, repeat;
  background-origin: padding-box, border-box, border-box;
  background-clip: padding-box, border-box, border-box;
  border: 22px solid transparent;
  border-radius: 18px;
  padding: 18px 16px 22px;
  box-shadow: 0 12px 28px rgba(190, 110, 130, 0.16);
}}
h1 {{
  margin: 0 0 8px;
  font-family: "Segoe Script", "Comic Sans MS", cursive;
  font-size: 2.3rem;
  font-weight: 400;
  color: #c2185b;
}}
h2 {{
  margin: 18px 0 6px;
  color: #123a9c;
  font-size: 1.35rem;
}}
.paes h2, .mercearia h2 {{ color: #c2185b; }}
.acougue h2 {{ color: #e10600; }}
.hortifruti h2 {{ color: #009c3b; }}
label {{
  display: flex;
  gap: 12px;
  align-items: center;
  min-height: 52px;
  margin: 0;
  padding: 6px 0;
  font-size: 1.2rem;
}}
input {{
  width: 1.6rem;
  height: 1.6rem;
  accent-color: #c2185b;
  flex: 0 0 auto;
}}
.nome {{ flex: 1; }}
em {{
  font-style: normal;
  font-weight: 700;
  color: #e10600;
  min-width: 5.5rem;
  text-align: right;
}}
label.tenho em {{ color: #009c3b; }}
label.tenho .nome {{ text-decoration: line-through; opacity: 0.72; }}
#aviso {{ font-weight: 700; }}
</style>
</head>
<body>
<main>
<div class="folha">
<h1>Lista do mercado</h1>
<p>{escape(resumo)}</p>
<p id="aviso">{escape(aviso)} Toque na caixinha. Verde, “já tenho”. Vermelho, “comprar”.</p>
{''.join(blocos)}
</div>
</main>
<script>
const ate = {int(ate or 0)};
const chave = "receitinhas-" + ate;
function pintar(el) {{
  const linha = el.closest("label");
  linha.classList.toggle("tenho", el.checked);
  linha.querySelector("em").textContent = el.checked ? "Já tenho" : "Comprar";
}}
document.querySelectorAll("input").forEach((el) => {{
  if (ate && Date.now() / 1000 > ate) {{
    el.checked = false;
  }} else {{
    const salvo = localStorage.getItem(chave + el.id);
    if (salvo !== null) el.checked = salvo === "1";
  }}
  pintar(el);
  el.addEventListener("change", () => {{
    localStorage.setItem(chave + el.id, el.checked ? "1" : "0");
    pintar(el);
  }});
}});
if (ate && Date.now() / 1000 > ate) {{
  document.getElementById("aviso").textContent = "Passaram {HORAS} horas. A marcação de casa foi apagada. Toque de novo no que você ainda tem.";
}}
</script>
</body>
</html>
"""


def titulo_com_numero(receita_id: str) -> str:
    try:
        return titulo_receita(receita_id)
    except KeyError:
        return apelido(receita_id)
