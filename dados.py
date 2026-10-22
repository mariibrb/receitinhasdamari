"""Fichas e lista de compras do livro de congelados."""

from __future__ import annotations

import unicodedata

SECOES = [
    {
        "id": "pratos",
        "titulo": "Refeições principais",
        "icon": ":material/skillet:",
    },
    {
        "id": "lanches",
        "titulo": "Salgados e lanches",
        "icon": ":material/lunch_dining:",
    },
    {
        "id": "doces",
        "titulo": "Doces e lancheira",
        "icon": ":material/cookie:",
        "resumo": "Bolos, docinhos e porções para congelar.",
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
        "titulo": "Vulcãozinhos de carne moída com purê de batata",
        "secao": "pratos",
        "rendimento": "8 unidades",
        "aparencia": "Copinhos de carne assada com purê de batata e muçarela gratinada.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "700 g de carne moída (patinho ou acém)",
                    "800 g de batata inglesa",
                    "150 g de queijo muçarela ralado",
                    "1/2 cebola e 2 dentes de alho",
                    "1 e 1/2 colher (sopa) de manteiga",
                    "50 ml de leite integral",
                    "2 colheres (sopa) de cheiro-verde, sal e pimenta-do-reino a gosto",
                ],
            }
        ],
        "passos": [
            "Cozinhe 800 g de batatas em água e sal até ficarem macias. Esprema ainda quentes, misture a manteiga e o leite até formar um purê bem firme. Reserve.",
            "Tempere 700 g de carne moída crua com alho, cebola, sal, pimenta e cheiro-verde.",
            "Modele 8 copinhos com a carne direto em uma assadeira.",
            "Preencha o centro de cada copinho com o purê e cubra com a muçarela.",
            "Asse em forno preaquecido a 200°C por 25 minutos, até a carne assar e o queijo gratinar.",
        ],
        "congelar": "Deixe esfriar completamente antes de embalar.",
    },
    {
        "id": "panqueca",
        "numero": 2,
        "titulo": "Panquecas funcionais de espinafre",
        "secao": "pratos",
        "rendimento": "8 a 10 unidades",
        "aparencia": "Discos verdes recheados com frango ou carne e legumes ralados.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "1 maço de espinafre fresco (cerca de 300 g)",
                    "1 xícara de leite integral",
                    "1 xícara de farinha de trigo",
                    "2 ovos",
                    "1/2 cebola, 2 dentes de alho, azeite, sal e pimenta-do-reino a gosto",
                ],
            },
            {
                "nome": "Recheio, escolha um ou os dois",
                "itens": [
                    "400 g de frango desfiado",
                    "ou 400 g de carne moída refogada",
                    "200 g de refogado de legumes (cenoura, abobrinha e chuchu ralados)",
                ],
            },
        ],
        "passos": [
            "Bata no liquidificador o espinafre, o leite, a farinha, os ovos e o sal até obter uma massa lisa e verde.",
            "Aqueça uma frigideira antiaderente levemente untada e faça os discos finos.",
            "Refogue o alho, a cebola e o frango ou a carne moída. Misture o refogado de legumes.",
            "Recheie cada disco, enrole e monte em marmitinhas individuais.",
        ],
        "congelar": "Deixe esfriar antes de congelar as marmitinhas.",
    },
    {
        "id": "escondidinho",
        "numero": 3,
        "titulo": "Escondidinho de batata com frango ou carne",
        "secao": "pratos",
        "rendimento": "4 marmitinhas",
        "aparencia": "Purê de batata com recheio cremoso e muçarela por cima.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "700 g de batata inglesa",
                    "400 g de frango desfiado ou carne moída",
                    "150 g de refogado de legumes (cenoura, abobrinha e chuchu)",
                    "150 g de queijo muçarela ralado",
                    "100 g de requeijão culinário",
                    "50 g de azeitonas fatiadas",
                    "1/2 sachê de molho ou extrato de tomate",
                    "1 colher (sopa) de manteiga e 50 ml de leite integral",
                    "Sal a gosto",
                ],
            }
        ],
        "passos": [
            "Prepare o purê amassando as batatas cozidas com manteiga, leite e sal.",
            "Refogue o frango ou a carne moída com o refogado de legumes, azeitonas, requeijão e extrato de tomate.",
            "Nas marmitinhas, faça uma camada de purê, o recheio e feche com outra camada de purê.",
            "Cubra com a muçarela e leve ao forno por 15 minutos para derreter o queijo.",
        ],
        "congelar": "Deixe gelar e só então congele.",
    },
    {
        "id": "esfirras",
        "numero": 4,
        "titulo": "Esfirras abertas e fechadas",
        "secao": "lanches",
        "rendimento": "30 unidades",
        "aparencia": "Massa caseira com carne, frango, calabresa ou brócolis. Dá para marcar mais de um recheio.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "500 g de farinha de trigo",
                    "10 g de fermento biológico seco (1 sachê)",
                    "1 colher (sopa) de açúcar",
                    "1 colher (chá) de sal",
                    "3 colheres (sopa) de óleo",
                    "Cerca de 250 ml de água morna",
                ],
            },
            {
                "nome": "Recheios desta fornada",
                "itens": [
                    "Carne, 8 abertas: 300 g de carne moída crua, 1 tomate picado, 1/2 cebola, sal, pimenta e limão",
                    "Frango cremoso, 8 fechadas: 300 g de frango desfiado, 1/2 lata de milho, 150 g de requeijão, cheiro-verde e sal",
                    "Calabresa, 7 abertas: 400 g de linguiça calabresa, 1 cebola grande e 100 g de requeijão",
                    "Brócolis com queijo, 7 fechadas: 500 g de brócolis picado cozido, 2 dentes de alho, 150 g de muçarela, azeite e sal",
                ],
            },
        ],
        "passos": [
            "Misture a farinha, o fermento, o açúcar e o sal. Adicione o óleo e a água morna aos poucos, sovando por 8 a 10 minutos até a massa ficar lisa. Deixe descansar coberta por 30 minutos.",
            "Divida a massa em 30 bolinhas iguais.",
            "Abertas (carne ou calabresa): abra a bolinha pressionando o centro para formar uma borda elevada e preencha.",
            "Fechadas (frango ou brócolis): abra o disco, coloque o recheio no centro e dobre as três pontas, selando bem.",
            "Asse a 200°C em assadeira untada por 15 a 20 minutos, até dourar.",
        ],
        "congelar": "Deixe esfriar antes de embalar.",
    },
    {
        "id": "pastel",
        "numero": 5,
        "titulo": "Pastéis de feira em discos redondos",
        "secao": "lanches",
        "rendimento": "20 unidades por recheio",
        "aparencia": "Discos prontos, fechados em meia-lua. Cada recheio é uma fornada.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": ["20 a 24 discos prontos de pastel (cerca de 500 g a 600 g)"],
            },
            {
                "nome": "Um recheio por fornada",
                "itens": [
                    "Carne com azeitona: 150 g de carne moída refogada com tomate e 30 g de azeitona picada",
                    "Carne com cheddar: 150 g de carne moída refogada, 100 g de cheddar e 1 cebola caramelizada",
                    "Frango com milho: 150 g de frango desfiado, 1/2 lata de milho e 80 g de requeijão",
                    "Presunto e queijo: 100 g de presunto, 100 g de muçarela e orégano",
                    "Palmito: 300 g de palmito refogado com alho, cebola, 1/2 sachê de molho de tomate e 80 g de requeijão",
                ],
            },
        ],
        "passos": [
            "Coloque 1 colher bem servida do recheio frio no centro do disco.",
            "Pincele um pouco de água em meia borda, dobre em meia-lua e aperte com um garfo.",
            "Passe levemente no trigo.",
        ],
        "congelar": "Disponha sem encostar por 2 horas no freezer. Depois de durinhos, passe para sacos plásticos.",
    },
    {
        "id": "pizza",
        "numero": 6,
        "titulo": "Mini pizzas pré-assadas",
        "secao": "lanches",
        "rendimento": "8 unidades",
        "aparencia": "Discos pré-assados com presunto e muçarela ou frango com requeijão.",
        "grupos": [
            {
                "nome": "Base",
                "itens": [
                    "1 pacote de discos de mini pizza pré-assados (8 discos)",
                    "1/2 sachê de molho de tomate",
                    "1 tomate em rodelas, milho verde e orégano a gosto",
                ],
            },
            {
                "nome": "Coberturas, pode marcar as duas",
                "itens": [
                    "Presunto e muçarela: 100 g de presunto e 150 g de muçarela",
                    "Frango com requeijão: 150 g de frango desfiado e 150 g de requeijão ou catupiry",
                ],
            },
        ],
        "passos": [
            "Espalhe uma camada leve de molho de tomate em cada disco.",
            "Distribua a cobertura escolhida.",
            "Salpique orégano por cima.",
        ],
        "congelar": "Embale individualmente ou em duplas no plástico filme.",
    },
    {
        "id": "bandas",
        "numero": 7,
        "titulo": "Bandas de pão francês recheadas",
        "secao": "lanches",
        "rendimento": "30 mini lanches em 15 pães",
        "aparencia": "Pães em canoa com carne louca, pernil, misto ou peito de peru.",
        "grupos": [
            {
                "nome": "Pão",
                "itens": ["15 pães franceses, cortados ao meio"],
            },
            {
                "nome": "Recheios desta fornada",
                "itens": [
                    "Carne louca, 10 bandas: 1,5 kg de lagarto ou fraldinha, 2 cebolas, 2 tomates e 1 sachê de molho de tomate",
                    "Pernil barbecue, 8 bandas: 1,2 kg de pernil suíno, 1 cebola, 2 dentes de alho, 150 ml de barbecue e 50 ml de shoyu",
                    "Misto, 6 bandas: 150 g de presunto, 150 g de muçarela, 1 tomate e orégano",
                    "Peito de peru, 6 bandas: 200 g de peito de peru, 200 g de cream cheese e 50 g de azeitonas picadas",
                ],
            },
        ],
        "passos": [
            "Corte os pães ao meio no sentido do comprimento.",
            "Retire um pouco do miolo do centro, formando uma canoa.",
            "Preencha cada metade com o recheio.",
            "Embale cada banda em papel-alumínio.",
        ],
        "congelar": "As bandas embaladas vão direto para o freezer.",
    },
    {
        "id": "hamburguer",
        "numero": 8,
        "titulo": "Hambúrgueres caseiros de 100 g",
        "secao": "lanches",
        "rendimento": "10 unidades",
        "aparencia": "Discos de 100 g, temperados só com sal, pimenta e azeite.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 kg de carne moída crua (patinho ou acém)",
                    "1 colher (chá) de sal",
                    "Pimenta-do-reino e 1 fio de azeite a gosto",
                ],
            }
        ],
        "passos": [
            "Misture a carne crua com o sal, a pimenta e um fio de azeite. Não ponha cebola nem alho frescos na massa, para não soltar água.",
            "Divida em 10 porções de 100 g e modele os discos.",
            "Embale cada um em plástico próprio para hambúrguer.",
        ],
        "congelar": "Congele crus.",
    },
    {
        "id": "almondega",
        "numero": 9,
        "titulo": "Almôndegas recheadas com queijo",
        "secao": "lanches",
        "rendimento": "10 unidades",
        "aparencia": "Bolinhas de carne com um cubo de muçarela no centro.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "500 g de carne moída crua",
                    "100 g de queijo muçarela em 10 cubinhos",
                    "1/2 cebola ralada e 1 dente de alho amassado",
                    "Cheiro-verde e sal a gosto",
                ],
            }
        ],
        "passos": [
            "Tempere a carne com alho, cebola ralada, sal e cheiro-verde.",
            "Divida em 10 porções, abra na palma da mão e coloque 1 cubo de muçarela no centro.",
            "Feche bem, para o queijo não vazar.",
        ],
        "congelar": "Congele cruas, abertas na assadeira, e só depois ensacar.",
    },
    {
        "id": "bolo_cenoura",
        "numero": 10,
        "titulo": "Bolo de cenoura com vulcão de chocolate",
        "secao": "doces",
        "rendimento": "6 marmitinhas",
        "aparencia": "Marmitinhas de bolo de cenoura com calda de chocolate quente.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "1 cenoura média (cerca de 150 g)",
                    "2 ovos",
                    "80 ml de óleo",
                    "150 g de açúcar",
                    "150 g de farinha de trigo",
                    "8 g de fermento em pó",
                ],
            },
            {
                "nome": "Calda",
                "itens": ["100 g de achocolatado ou cacau, 50 g de açúcar, 20 g de manteiga e 30 ml de leite"],
            },
        ],
        "passos": [
            "Bata no liquidificador a cenoura, os ovos, o óleo e o açúcar até ficar homogêneo.",
            "Transfira para uma tigela e incorpore a farinha e o fermento.",
            "Distribua em 6 marmitinhas e asse a 180°C por 20 minutos.",
            "Ferva a calda até encorpar e despeje quente sobre os bolos.",
        ],
        "congelar": "Deixe esfriar antes de embalar as marmitinhas.",
    },
    {
        "id": "bolo_banana",
        "numero": 11,
        "titulo": "Bolo de banana com aveia e canela",
        "secao": "doces",
        "rendimento": "6 quadrados",
        "aparencia": "Bolo úmido de banana, aveia e canela, cortado em quadrados.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "3 bananas maduras (cerca de 300 g)",
                    "2 ovos",
                    "50 ml de óleo",
                    "50 g de açúcar mascavo",
                    "100 g de aveia em flocos finos",
                    "5 g de canela em pó",
                    "8 g de fermento em pó",
                ],
            }
        ],
        "passos": [
            "Amasse as bananas e misture com os ovos, o óleo, o açúcar mascavo e a canela.",
            "Adicione a aveia e o fermento.",
            "Despeje em forma retangular de 20×30 cm untada e asse a 180°C por 25 minutos.",
            "Deixe esfriar, corte em 6 quadrados e embale no plástico filme.",
        ],
        "congelar": "Embale os quadrados depois de frios.",
    },
    {
        "id": "bolo_nega",
        "numero": 12,
        "titulo": "Bolo de chocolate nega maluca",
        "secao": "doces",
        "rendimento": "6 quadrados",
        "aparencia": "Bolo de chocolate com cacau e água fervente, cortado em 6 porções.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "2 ovos",
                    "100 ml de óleo",
                    "150 g de açúcar",
                    "80 g de cacau em pó 50%",
                    "150 g de farinha de trigo",
                    "100 ml de água fervente",
                    "8 g de fermento em pó",
                ],
            }
        ],
        "passos": [
            "Bata os ovos com o açúcar e o óleo.",
            "Adicione o cacau e a farinha. Por último, misture a água fervente e o fermento.",
            "Asse a 180°C por 25 minutos.",
            "Deixe esfriar, corte em 6 porções e embale em papel-alumínio.",
        ],
        "congelar": "Embale as porções depois de frias.",
    },
    {
        "id": "bolo_laranja",
        "numero": 13,
        "titulo": "Bolo de laranja com calda cítrica",
        "secao": "doces",
        "rendimento": "6 fatias",
        "aparencia": "Bolo de laranja inteira, regado com calda ainda quente.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "1 laranja pera inteira, sem sementes e sem o miolo branco",
                    "2 ovos",
                    "80 ml de óleo",
                    "150 g de açúcar",
                    "150 g de farinha de trigo",
                    "8 g de fermento em pó",
                ],
            },
            {
                "nome": "Calda",
                "itens": ["Suco de 1 laranja e 50 g de açúcar"],
            },
        ],
        "passos": [
            "Bata no liquidificador a laranja inteira com casca, os ovos, o óleo e o açúcar.",
            "Misture a farinha e o fermento à mão.",
            "Asse a 180°C por 25 minutos e regue ainda quente com o suco de laranja fervido com açúcar.",
        ],
        "congelar": "Deixe esfriar antes de fatiar e embalar.",
    },
    {
        "id": "bolo_coco",
        "numero": 14,
        "titulo": "Bolo de coco gelado",
        "secao": "doces",
        "rendimento": "6 quadrados",
        "aparencia": "Quadrados molhados na calda de coco e passados no coco ralado.",
        "grupos": [
            {
                "nome": "Massa",
                "itens": [
                    "2 claras e 2 gemas",
                    "120 g de açúcar",
                    "100 g de farinha de trigo",
                    "50 ml de leite",
                    "5 g de fermento em pó",
                ],
            },
            {
                "nome": "Calda e cobertura",
                "itens": [
                    "150 ml de leite condensado",
                    "100 ml de leite de coco",
                    "50 ml de leite integral",
                    "50 g de coco ralado sem açúcar",
                ],
            },
        ],
        "passos": [
            "Bata as claras em neve. À parte, bata as gemas com o açúcar, junte a farinha intercalada com o leite e, por último, as claras e o fermento.",
            "Asse a 180°C por 20 minutos.",
            "Misture o leite condensado, o leite de coco e o leite. Banhe os quadrados, passe no coco ralado e embale em papel-alumínio.",
        ],
        "congelar": "Embale cada quadrado depois de frio.",
    },
    {
        "id": "palha",
        "numero": 15,
        "titulo": "Palha italiana caseira",
        "secao": "doces",
        "rendimento": "12 a 15 quadradinhos",
        "aparencia": "Quadradinhos de brigadeiro com biscoito maisena.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado (395 g)",
                    "1 caixa de creme de leite (200 g)",
                    "3 colheres (sopa) de cacau em pó",
                    "1 colher (sopa) de manteiga",
                    "1 pacote de biscoito maisena picado (cerca de 150 g)",
                ],
            }
        ],
        "passos": [
            "Em fogo baixo, cozinhe o leite condensado, o creme de leite, o cacau e a manteiga até o ponto de brigadeiro mole.",
            "Desligue o fogo e misture o biscoito picado.",
            "Despeje em uma travessa forrada com plástico, leve à geladeira por 2 horas, corte em quadradinhos e embale.",
        ],
        "congelar": "Para comer, tire do freezer cerca de 10 minutos antes.",
    },
    {
        "id": "pudim",
        "numero": 16,
        "titulo": "Mini pudim de leite condensado",
        "secao": "doces",
        "rendimento": "6 a 8 unidades",
        "aparencia": "Mini pudins com calda de caramelo no fundo da forminha.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado (395 g)",
                    "1 lata de leite integral, na mesma medida",
                    "3 ovos",
                    "1 xícara de açúcar e 1/2 xícara de água quente para o caramelo",
                ],
            }
        ],
        "passos": [
            "Derreta o açúcar até virar caramelo, adicione a água quente e forre o fundo das mini forminhas.",
            "Bata o leite condensado, o leite e os ovos no liquidificador por 2 minutos. Peneire ao despejar nas forminhas.",
            "Asse em banho-maria, cobertos com papel-alumínio, a 180°C por 45 minutos.",
        ],
        "congelar": "Deixe gelar antes de congelar na própria forminha.",
    },
    {
        "id": "brigadeiro",
        "numero": 17,
        "titulo": "Brigadeiro tradicional enrolado",
        "secao": "doces",
        "rendimento": "25 a 30 docinhos",
        "aparencia": "Bolinhas no ponto de bloco, passadas no granulado.",
        "grupos": [
            {
                "nome": "Ingredientes",
                "itens": [
                    "1 lata de leite condensado (395 g)",
                    "1/2 caixa de creme de leite (100 g)",
                    "3 colheres (sopa) de cacau em pó",
                    "1 colher (sopa) de manteiga",
                    "100 g de granulado de chocolate",
                ],
            }
        ],
        "passos": [
            "Cozinhe em fogo baixo o leite condensado, o creme de leite, o cacau e a manteiga até o ponto de bloco, soltando do fundo da panela.",
            "Deixe esfriar por completo. Unte as mãos com manteiga, modele as bolinhas e passe no granulado.",
            "Leve ao freezer em assadeira por 2 horas e transfira para potinhos bem fechados.",
        ],
        "congelar": "Descongela em cerca de 15 minutos fora da geladeira.",
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
