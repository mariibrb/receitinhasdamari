"""Fichas e lista de compras do livro de congelados."""

from __future__ import annotations

import unicodedata

SECOES = [
    {
        "id": "pratos",
        "titulo": "Pratos principais e marmitinhas",
        "icon": ":material/skillet:",
    },
    {
        "id": "lanches",
        "titulo": "Lanches e salgados práticos",
        "icon": ":material/lunch_dining:",
    },
    {
        "id": "doces",
        "titulo": "Lanches e sobremesas doces",
        "icon": ":material/cookie:",
        "resumo": "Porções individuais doces e fáceis de congelar.",
    },
]

CATEGORIAS = [
    {"id": "paes", "titulo": "Pães, massas e mercearia doce", "atalho": "Pães"},
    {"id": "acougue", "titulo": "Açougue, frios e embutidos", "atalho": "Açougue"},
    {"id": "laticinios", "titulo": "Laticínios, ovos e batata", "atalho": "Laticínios"},
    {"id": "hortifruti", "titulo": "Hortifrúti", "atalho": "Hortifrúti"},
    {"id": "mercearia", "titulo": "Mercearia geral e conservas", "atalho": "Mercearia"},
]

RECEITAS = [
    {
        "id": "vulcao",
        "numero": 1,
        "titulo": "Vulcãozinho de carne moída com purê de batata",
        "secao": "pratos",
        "rendimento": "6 a 8 unidades",
        "aparencia": (
            "Copinhos dourados de carne moída bem assada e suculenta, "
            "recheados até o topo com um purê de batata ultracremoso e "
            "cobertos com muçarela gratinada e salpicada de cheiro-verde."
        ),
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1,2 kg de carne moída (patinho ou acém)",
                    "2,5 kg de batata inglesa",
                    "1/2 xícara de leite integral",
                    "2 colheres (sopa) de manteiga",
                    "1 cebola picadinha e 3 dentes de alho amassados",
                    "200 g de queijo muçarela ralado",
                    "Sal, pimenta-do-reino e cheiro-verde a gosto",
                ],
            }
        ],
        "passos": [
            "Cozinhe as batatas em água e sal até ficarem bem macias. Esprema-as ainda quentes e misture a manteiga e o leite até formar um purê bem firme. Reserve.",
            "Tempere a carne moída crua com o alho, cebola, sal, pimenta e cheiro-verde.",
            "Modele cumbucas ou copinhos com a carne. Dá para usar forminhas de empada como apoio na assadeira.",
            "Preencha o centro de cada copinho de carne com o purê de batata e finalize com muçarela por cima.",
            "Asse em forno preaquecido a 200°C por 25 minutos, até a carne assar e o queijo gratinar.",
        ],
        "congelar": "Deixe esfriar para congelar.",
    },
    {
        "id": "panqueca",
        "numero": 2,
        "titulo": "Panqueca de espinafre com recheio funcional",
        "secao": "pratos",
        "rendimento": "8 a 10 unidades",
        "aparencia": (
            "Panquecas de cor verde-vibrante alinhadas em uma travessa, "
            "recheadas com frango e um refogado de cenoura, abobrinha e "
            "chuchu, cobertas por um fio leve de molho de tomate."
        ),
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "0,4 kg de espinafre fresco (1 a 2 maços)",
                    "1 xícara de leite integral",
                    "1 xícara de farinha de trigo",
                    "2 ovos",
                    "1 pitada de sal e azeite para untar",
                ],
            },
            {
                "nome": "Recheio",
                "itens": [
                    "Frango desfiado ou carne moída",
                    "Cenoura, abobrinha e chuchu ralados e refogados bem sequinhos no azeite com alho",
                ],
            },
        ],
        "passos": [
            "Bata no liquidificador o espinafre, o leite, a farinha, os ovos e o sal até obter uma massa lisa e verde.",
            "Aqueça uma frigideira antiaderente levemente untada e faça os discos finos de panqueca.",
            "Misture o refogado dos legumes ralados com a proteína escolhida.",
            "Recheie cada disco, enrole e acomode nas marmitinhas.",
        ],
        "congelar": None,
        "ja_tem": "Cenoura, abobrinha e chuchu já estão em casa.",
    },
    {
        "id": "esfirras",
        "numero": 3,
        "titulo": "Esfirras abertas e fechadas (massa curinga)",
        "secao": "lanches",
        "rendimento": "30 unidades",
        "aparencia": (
            "Esfirras abertas de carne temperada e calabresa acebolada, "
            "ao lado de esfirras fechadas em formato triangular, douradas, "
            "recheadas com frango cremoso e brócolis com queijo."
        ),
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "500 g de farinha de trigo",
                    "1 sachê de fermento biológico seco (10 g)",
                    "1 colher (sopa) de açúcar e 1 colher (chá) de sal",
                    "3 colheres (sopa) de óleo",
                    "Cerca de 250 ml de água morna",
                ],
            },
            {
                "nome": "Recheios citados na ficha",
                "itens": [
                    "Abertas: carne temperada ou calabresa acebolada",
                    "Fechadas: frango cremoso ou brócolis com queijo",
                ],
            },
        ],
        "passos": [
            "Misture os ingredientes secos, adicione o óleo e vá colocando a água morna aos poucos até dar o ponto de sova. Sove por 8 minutos até a massa ficar lisa e deixe descansar por 30 minutos.",
            "Divida em 30 bolinhas iguais.",
            "Abertas (carne ou calabresa): abra os discos pressionando o centro para formar uma borda elevada e coloque o recheio no meio.",
            "Fechadas (frango ou brócolis): abra o disco plano, recheie o centro e dobre as 3 pontas formando um triângulo, selando bem.",
            "Asse a 200°C por 15 a 20 minutos, até dourar a base e as bordas.",
        ],
        "congelar": None,
    },
    {
        "id": "bandas",
        "numero": 4,
        "titulo": "Bandas de pão francês recheadas (estilo canoa)",
        "secao": "lanches",
        "rendimento": "30 mini lanches (em 15 pães)",
        "aparencia": (
            "Metades de pão francês crocantes, recheadas até a borda com "
            "carne louca e pernil ao molho barbecue, embaladas para ir direto ao freezer."
        ),
        "grupos": [
            {
                "nome": "Recheios",
                "itens": [
                    "Carne louca: lagarto desfiado com pimentões, tomate, cebola e molho encorpado",
                    "Pernil barbecue: pernil assado e desfiado envolvido em molho barbecue e shoyu",
                    "Misto especial: presunto, muçarela, tomate picado sem semente e orégano",
                    "Peito de peru cremoso: peito de peru picado com cream cheese e azeitonas",
                ],
            }
        ],
        "passos": [
            "Corte os pães franceses ao meio no sentido do comprimento.",
            "Retire um pouco do excesso do miolo, formando uma canoa, para caber mais recheio.",
            "Preencha com o recheio desejado.",
            "Embale cada metade individualmente em papel-alumínio.",
        ],
        "congelar": "Embaladas em papel-alumínio, as metades vão direto para o freezer.",
    },
    {
        "id": "palha",
        "numero": 5,
        "titulo": "Palha italiana caseira em porções",
        "secao": "doces",
        "rendimento": "12 a 15 quadradinhos",
        "aparencia": (
            "Quadradinhos macios de brigadeiro com pedaços crocantes de "
            "biscoito, polvilhados com leite em pó e embalados individualmente."
        ),
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado",
                    "1 caixinha de creme de leite",
                    "3 colheres (sopa) de cacau em pó (ou chocolate em pó)",
                    "1 colher (sopa) de manteiga",
                    "1 pacote de biscoito maisena picado grosseiramente",
                ],
            }
        ],
        "passos": [
            "Leve o leite condensado, o creme de leite, o cacau e a manteiga ao fogo baixo, mexendo sempre, até dar o ponto de brigadeiro mole (soltando do fundo da panela).",
            "Desligue o fogo e misture os biscoitos picados.",
            "Despeje em uma travessa forrada com plástico ou papel-manteiga, alise e leve à geladeira por 2 horas.",
            "Corte em quadradinhos individuais e embale em insulfilm.",
        ],
        "congelar": "Para consumir, tire do freezer 10 minutos antes.",
    },
    {
        "id": "pudim",
        "numero": 6,
        "titulo": "Mini pudim de leite condensado (sem furinhos)",
        "secao": "doces",
        "rendimento": "6 a 8 mini forminhas",
        "aparencia": (
            "Mini pudins individuais lisinhos e brilhantes, servidos com "
            "uma calda de caramelo dourada e aveludada."
        ),
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado",
                    "1 lata de leite integral (use a mesma medida da lata)",
                    "3 ovos inteiros",
                    "1 xícara de açúcar para a calda e 1/2 xícara de água quente",
                ],
            }
        ],
        "passos": [
            "Derreta o açúcar na panela até virar caramelo, acrescente a água quente com cuidado e deixe dissolver. Forre o fundo das mini forminhas com a calda.",
            "Bata o leite condensado, o leite e os ovos no liquidificador por 2 minutos. Passe a mistura por uma peneira ao despejar nas forminhas, para ficar sem furinhos.",
            "Asse em banho-maria no forno, cobertos com papel-alumínio, a 180°C por cerca de 40 a 50 minutos.",
            "Deixe gelar completamente antes de desenformar ou congelar na própria forminha.",
        ],
        "congelar": "Deixe gelar por completo antes de desenformar ou congele na própria forminha.",
    },
    {
        "id": "brigadeiro",
        "numero": 7,
        "titulo": "Brigadeiro tradicional enrolado para congelar",
        "secao": "doces",
        "rendimento": "25 a 30 docinhos",
        "aparencia": (
            "Brigadeiros cremosos boleados e passados no granulado, "
            "dispostos em forminhas e organizados em marmitinhas seladas."
        ),
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado",
                    "1/2 caixinha de creme de leite",
                    "3 colheres (sopa) de chocolate em pó 50%",
                    "1 colher (sopa) de manteiga",
                    "Granulado ou granulado de chocolate nobre para confeitar",
                ],
            }
        ],
        "passos": [
            "Cozinhe os ingredientes no fogo baixo até dar o ponto de bloco: a massa cai em pedaços da colher e solta completamente do fundo.",
            "Deixe esfriar por completo em prato untado.",
            "Unte as mãos com manteiga, modele as bolinhas e passe no granulado.",
            "Coloque os brigadeiros em uma assadeira e leve ao freezer por 2 horas. Depois de firmes, transfira para potinhos herméticos.",
        ],
        "congelar": "Descongela em 15 minutos em temperatura ambiente, mantendo a textura.",
    },
]

ITENS = [
    {
        "id": "pao_frances",
        "categoria": "paes",
        "nome": "Pão francês",
        "quantidade": "15 unidades",
        "receitas": ["bandas"],
    },
    {
        "id": "discos_pizza",
        "categoria": "paes",
        "nome": "Discos de mini pizza pré-assados",
        "quantidade": "1 pacote (8 discos)",
        "receitas": [],
    },
    {
        "id": "massa_pastel",
        "categoria": "paes",
        "nome": "Massa pronta de pastel em rolo",
        "quantidade": "0,8 kg (2 rolos)",
        "receitas": [],
    },
    {
        "id": "biscoito_maisena",
        "categoria": "paes",
        "nome": "Biscoito maisena",
        "quantidade": "1 pacote (palha italiana)",
        "receitas": ["palha"],
    },
    {
        "id": "leite_condensado",
        "categoria": "paes",
        "nome": "Leite condensado",
        "quantidade": "3 latas ou caixas",
        "receitas": ["palha", "pudim", "brigadeiro"],
    },
    {
        "id": "creme_leite",
        "categoria": "paes",
        "nome": "Creme de leite",
        "quantidade": "3 caixinhas",
        "receitas": ["palha", "brigadeiro"],
    },
    {
        "id": "chocolate_cacau",
        "categoria": "paes",
        "nome": "Chocolate em pó ou cacau 50%",
        "quantidade": "1 pacote",
        "receitas": ["palha", "brigadeiro"],
    },
    {
        "id": "granulado",
        "categoria": "paes",
        "nome": "Granulado de chocolate",
        "quantidade": "1 pacote",
        "receitas": ["brigadeiro"],
    },
    {
        "id": "carne_moida",
        "categoria": "acougue",
        "nome": "Carne moída (patinho ou acém)",
        "quantidade": "3,2 kg",
        "receitas": ["vulcao", "panqueca", "esfirras"],
        "nota": "A ficha do vulcãozinho pede 1,2 kg. O restante da lista cobre panqueca e esfirras, que não fecham a medida na ficha.",
    },
    {
        "id": "peito_frango",
        "categoria": "acougue",
        "nome": "Peito de frango (sem osso)",
        "quantidade": "2,0 kg",
        "receitas": ["panqueca", "esfirras"],
    },
    {
        "id": "carne_louca",
        "categoria": "acougue",
        "nome": "Carne para carne louca (lagarto ou fraldinha)",
        "quantidade": "1,2 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "pernil",
        "categoria": "acougue",
        "nome": "Pernil ou lombo suíno",
        "quantidade": "1,0 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "calabresa",
        "categoria": "acougue",
        "nome": "Linguiça calabresa",
        "quantidade": "0,4 kg",
        "receitas": ["esfirras"],
    },
    {
        "id": "bacon",
        "categoria": "acougue",
        "nome": "Bacon em cubos",
        "quantidade": "0,2 kg",
        "receitas": [],
    },
    {
        "id": "presunto",
        "categoria": "acougue",
        "nome": "Presunto fatiado",
        "quantidade": "0,5 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "peito_peru",
        "categoria": "acougue",
        "nome": "Peito de peru fatiado",
        "quantidade": "0,3 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "batata",
        "categoria": "laticinios",
        "nome": "Batata inglesa",
        "quantidade": "2,5 kg",
        "receitas": ["vulcao"],
    },
    {
        "id": "ovos",
        "categoria": "laticinios",
        "nome": "Ovos",
        "quantidade": "2 dúzias",
        "receitas": ["panqueca", "pudim"],
    },
    {
        "id": "leite",
        "categoria": "laticinios",
        "nome": "Leite integral",
        "quantidade": "2 litros",
        "receitas": ["vulcao", "panqueca", "pudim"],
    },
    {
        "id": "mucarela",
        "categoria": "laticinios",
        "nome": "Queijo muçarela",
        "quantidade": "1,5 kg (1,0 kg fatiado + 0,5 kg em peça)",
        "receitas": ["vulcao", "esfirras", "bandas"],
    },
    {
        "id": "cheddar",
        "categoria": "laticinios",
        "nome": "Queijo cheddar",
        "quantidade": "0,35 kg (fatiado ou bisnaga)",
        "receitas": [],
    },
    {
        "id": "requeijao",
        "categoria": "laticinios",
        "nome": "Requeijão culinário ou catupiry",
        "quantidade": "1,0 kg (2 bisnagas)",
        "receitas": [],
    },
    {
        "id": "cream_cheese",
        "categoria": "laticinios",
        "nome": "Cream cheese",
        "quantidade": "0,3 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "manteiga",
        "categoria": "laticinios",
        "nome": "Manteiga",
        "quantidade": "0,4 kg (2 potes ou tabletes)",
        "receitas": ["vulcao", "palha", "brigadeiro"],
    },
    {
        "id": "espinafre",
        "categoria": "hortifruti",
        "nome": "Espinafre",
        "quantidade": "0,4 kg (1 a 2 maços)",
        "receitas": ["panqueca"],
    },
    {
        "id": "cebola",
        "categoria": "hortifruti",
        "nome": "Cebola",
        "quantidade": "2,5 kg",
        "receitas": ["vulcao", "esfirras", "bandas"],
    },
    {
        "id": "alho",
        "categoria": "hortifruti",
        "nome": "Alho",
        "quantidade": "0,2 kg (1 rede ou cabeça grande)",
        "receitas": ["vulcao", "panqueca"],
    },
    {
        "id": "tomate",
        "categoria": "hortifruti",
        "nome": "Tomate",
        "quantidade": "1,0 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "brocolis",
        "categoria": "hortifruti",
        "nome": "Brócolis",
        "quantidade": "0,5 kg (1 maço)",
        "receitas": ["esfirras"],
    },
    {
        "id": "cheiro_verde",
        "categoria": "hortifruti",
        "nome": "Cheiro-verde",
        "quantidade": "0,2 kg (2 maços)",
        "receitas": ["vulcao"],
    },
    {
        "id": "palmito",
        "categoria": "mercearia",
        "nome": "Palmito em conserva",
        "quantidade": "0,5 kg (2 vidros)",
        "receitas": [],
    },
    {
        "id": "azeitona",
        "categoria": "mercearia",
        "nome": "Azeitona fatiada sem caroço",
        "quantidade": "0,4 kg",
        "receitas": ["bandas"],
    },
    {
        "id": "milho",
        "categoria": "mercearia",
        "nome": "Milho verde em conserva",
        "quantidade": "0,34 kg (2 latas)",
        "receitas": [],
    },
    {
        "id": "molho_tomate",
        "categoria": "mercearia",
        "nome": "Molho ou extrato de tomate",
        "quantidade": "0,6 kg (2 sachês)",
        "receitas": ["panqueca"],
    },
    {
        "id": "farinha",
        "categoria": "mercearia",
        "nome": "Farinha de trigo",
        "quantidade": "2,0 kg",
        "receitas": ["panqueca", "esfirras"],
    },
    {
        "id": "fermento",
        "categoria": "mercearia",
        "nome": "Fermento biológico seco",
        "quantidade": "0,02 kg (2 sachês de 10 g)",
        "receitas": ["esfirras"],
        "nota": "A ficha das esfirras pede 1 sachê de 10 g. A lista de produção traz 2.",
    },
    {
        "id": "barbecue",
        "categoria": "mercearia",
        "nome": "Molho barbecue",
        "quantidade": "0,25 kg (1 frasco)",
        "receitas": ["bandas"],
    },
    {
        "id": "shoyu",
        "categoria": "mercearia",
        "nome": "Molho shoyu",
        "quantidade": "0,15 L (1 frasco)",
        "receitas": ["bandas"],
    },
]


def normalizar(texto: str) -> str:
    """Minúsculas e sem acento, para a busca no celular."""
    sem_acento = "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caractere) != "Mn"
    )
    return sem_acento.casefold().strip()


def chave_item(item_id: str) -> str:
    return f"compra_{item_id}"


def receita_por_id(receita_id: str) -> dict:
    for receita in RECEITAS:
        if receita["id"] == receita_id:
            return receita
    raise KeyError(receita_id)


def secao_por_id(secao_id: str) -> dict:
    for secao in SECOES:
        if secao["id"] == secao_id:
            return secao
    raise KeyError(secao_id)


def titulo_receita(receita_id: str) -> str:
    receita = receita_por_id(receita_id)
    return f"{receita['numero']}. {receita['titulo']}"


def item_marcado(estado: dict, item_id: str) -> bool:
    return bool(estado.get(chave_item(item_id), False))


def resumo_compras(estado: dict) -> tuple[int, int]:
    marcados = sum(1 for item in ITENS if item_marcado(estado, item["id"]))
    return marcados, len(ITENS)


def filtrar_receitas(busca: str, secao_id: str | None) -> list[dict]:
    termo = normalizar(busca)
    visiveis = []
    for receita in RECEITAS:
        if secao_id and secao_id != "todas" and receita["secao"] != secao_id:
            continue
        if termo:
            textos = [receita["titulo"], receita["aparencia"], *receita["passos"]]
            for grupo in receita["grupos"]:
                textos.extend(grupo["itens"])
            if not any(termo in normalizar(texto) for texto in textos):
                continue
        visiveis.append(receita)
    return visiveis


def filtrar_itens(
    busca: str,
    categoria_id: str | None,
    receita_ids: list[str],
    esconder_comprados: bool,
    estado: dict,
) -> list[dict]:
    termo = normalizar(busca)
    escolhidas = set(receita_ids)
    visiveis = []
    for item in ITENS:
        if categoria_id and categoria_id != "tudo" and item["categoria"] != categoria_id:
            continue
        if escolhidas and not escolhidas.intersection(item["receitas"]):
            continue
        if esconder_comprados and item_marcado(estado, item["id"]):
            continue
        if termo and termo not in normalizar(f"{item['nome']} {item['quantidade']}"):
            continue
        visiveis.append(item)
    return visiveis


def texto_pendentes(estado: dict) -> str:
    linhas = ["Para comprar no mercado", ""]
    for categoria in CATEGORIAS:
        pendentes = [
            item
            for item in ITENS
            if item["categoria"] == categoria["id"] and not item_marcado(estado, item["id"])
        ]
        if not pendentes:
            continue
        linhas.append(categoria["titulo"])
        linhas.extend(f"[ ] {item['nome']}: {item['quantidade']}" for item in pendentes)
        linhas.append("")
    if len(linhas) == 2:
        return "Nada para comprar. Tudo da lista já está marcado como em casa.\n"
    return "\n".join(linhas).rstrip() + "\n"
