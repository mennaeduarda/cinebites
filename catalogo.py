"""
catalogo.py
-----------
Este é o SEU catálogo de curadoria — a lista de experiências que você
cadastra manualmente, exatamente como um curador de conteúdo (pense
na equipe de conteúdo da Netflix, não no usuário final).

Para adicionar uma NOVA experiência, copie um dos blocos abaixo,
cole no final da lista EXPERIENCIAS e preencha com os dados do novo
prato/filme. Você não precisa mexer em nenhuma outra parte do
projeto — o seed.py lê essa lista sozinho.

Se o filme já existir aqui embaixo (mesmo "id"), não repita o bloco
de filme — só adicione outra experiência com o mesmo "filme_id".

⚠️ NOTA SOBRE OS IDs DE FILME: os números abaixo (238, 14836, etc.)
são os IDs reais desses filmes no TMDB, usados como referência local.
Como a integração automática com a API do TMDB ainda é Fase 2, os
dados de sinopse/pôster foram preenchidos à mão por enquanto — quando
a integração estiver pronta, esses campos passam a ser buscados
automaticamente a partir do ID.

⚠️ NOTA SOBRE "SAGA": como cada Experiência pertence a UM filme
específico (não a uma franquia inteira), as receitas de Harry Potter
e Percy Jackson foram distribuídas entre os filmes onde aquela cena
específica aparece. Vale revisar se concorda com a escolha!
"""

FILMES = [
    {
        "id": 238,
        "nome_filme": "O Poderoso Chefão",
        "poster_url": None,
        "sinopse": "A saga da família Corleone, uma das mais poderosas famílias do crime em Nova York.",
        "ano_lancamento": 1972,
    },
    {
        "id": 14836,
        "nome_filme": "Coraline",
        "poster_url": None,
        "sinopse": "Uma menina descobre uma porta secreta que leva a uma versão alternativa e sombria de sua casa e família.",
        "ano_lancamento": 2009,
    },
    {
        "id": 671,
        "nome_filme": "Harry Potter e a Pedra Filosofal",
        "poster_url": None,
        "sinopse": "Um menino descobre que é um bruxo e ingressa na Escola de Magia e Bruxaria de Hogwarts.",
        "ano_lancamento": 2001,
    },
    {
        "id": 673,
        "nome_filme": "Harry Potter e o Prisioneiro de Azkaban",
        "poster_url": None,
        "sinopse": "Harry enfrenta a ameaça de um fugitivo perigoso enquanto descobre mais sobre seu passado.",
        "ano_lancamento": 2004,
    },
    {
        "id": 675,
        "nome_filme": "Harry Potter e a Ordem da Fênix",
        "poster_url": None,
        "sinopse": "Harry forma um grupo secreto de estudantes para se preparar contra o retorno das forças das trevas.",
        "ano_lancamento": 2007,
    },
    {
        "id": 32657,
        "nome_filme": "Percy Jackson e o Ladrão de Raios",
        "poster_url": None,
        "sinopse": "Um adolescente descobre ser filho de um deus grego e embarca em uma jornada para evitar uma guerra entre os deuses.",
        "ano_lancamento": 2010,
    },
    {
        "id": 12162,
        "nome_filme": "A Princesa e o Sapo",
        "poster_url": None,
        "sinopse": "Uma jovem de Nova Orleans que sonha em ter seu próprio restaurante se envolve com um príncipe transformado em sapo.",
        "ano_lancamento": 2009,
    },
    {
        "id": 621,
        "nome_filme": "Grease: Nos Tempos da Brilhantina",
        "poster_url": None,
        "sinopse": "Um casal de estudantes vive um romance de verão que é posto à prova quando os dois se reencontram na escola.",
        "ano_lancamento": 1978,
    },

]

EXPERIENCIAS = [

    # ============================================================
    # O PODEROSO CHEFÃO (id 238)
    # ============================================================
    {
        "filme_id": 238,
        "nome_prato": "Ragu de Linguiça",
        "tipo_de_prato": "salgado",
        "cena_descricao": 'A cena em que Clemenza ensina Michael Corleone a fazer o molho para "vinte ou trinta homens".',
        "trivia": 'A frase "deixa a linguiça inteira, depois tira" virou uma das falas mais citadas de filmes sobre comida.',
        "modo_preparo": (
            "1. Doure as linguiças inteiras no azeite. "
            "2. Refogue cebola roxa, alho-poró, alho, cenoura, salsão e aipo. "
            "3. Tempere com erva doce e pimenta calabresa. "
            "4. Adicione o tomate pelado, o vinho tinto (seco e comum) e a água. "
            "5. Finalize com louro, manjericão e pimenta do reino, e cozinhe em fogo baixo por 2 horas."
        ),
        "ingredientes": [
            ("Linguiça toscana", "proteína", 250, "g"),
            ("Linguiça calabresa", "proteína", 200, "g"),
            ("Cebola roxa", "vegetal", 1, "unidade"),
            ("Alho-poró", "vegetal", 2, "talos"),
            ("Erva doce", "tempero", 1, "colher (sopa)"),
            ("Pimenta calabresa", "tempero", 1, "colher (chá)"),
            ("Aipo", "vegetal", 1, "raiz"),
            ("Vinho tinto seco", "bebida", 100, "ml"),
            ("Tomate pelado", "vegetal", 700, "g"),
            ("Cenoura", "vegetal", 1, "unidade"),
            ("Salsão", "vegetal", 2, "talos"),
            ("Alho", "tempero", 4, "dentes"),
            ("Vinho tinto", "bebida", 40, "ml"),
            ("Água", "outro", 240, "ml"),
            ("Louro", "tempero", 1, "folha"),
            ("Manjericão", "tempero", 1, "ramo"),
            ("Azeite", "outro", 2, "colheres (sopa)"),
            ("Pimenta do reino", "tempero", 1, "colher (chá)"),
        ],
    },
    {
        "filme_id": 238,
        "nome_prato": "Cannoli",
        "tipo_de_prato": "doce",
        "cena_descricao": 'A cena em que Clemenza manda Rocco "deixar a arma, pegar o cannoli".',
        "trivia": "A fala sobre o cannoli é considerada uma das melhores deixas cômicas do filme, em meio a uma cena de assassinato.",
        "modo_preparo": (
            "1. Prepare a massa com farinha, açúcar, cacau, banha, ovo, vinho Marsala e vinagre; deixe descansar. "
            "2. Frite os tubos de massa até dourar e deixe esfriar. "
            "3. Misture a ricota com chocolate ao leite, raspas e suco de limão, cachaça e canela. "
            "4. Recheie os tubos já frios com o creme de ricota."
        ),
        "ingredientes": [
            ("Farinha de trigo", "grão/farinha", 200, "g"),
            ("Açúcar refinado", "doce", 20, "g"),
            ("Cacau em pó", "doce", 2, "g"),
            ("Banha de porco", "outro", 20, "g"),
            ("Ovo", "proteína", 0.5, "unidade"),
            ("Vinho Marsala", "bebida", 60, "ml"),
            ("Vinagre", "outro", 30, "ml"),
            ("Ricota fresca", "laticínio", 400, "g"),
            ("Chocolate ao leite", "doce", 60, "g"),
            ("Limão siciliano", "fruta", 0.5, "unidade"),
            ("Cachaça", "bebida", 30, "ml"),
            ("Canela em pó", "tempero", 1, "colher (chá)"),
            ("Gordura vegetal", "outro", 1, "colher (sopa)"),
            ("Vinho branco seco", "bebida", 30, "ml"),
            ("Clara de ovo", "proteína", 1, "unidade"),
            ("Suco de limão", "fruta", 1, "colher (sopa)"),
            ("Raspas de limão", "fruta", 1, "colher (sopa)"),
        ],
    },
    {
        "filme_id": 238,
        "nome_prato": "Drink Godfather",
        "tipo_de_prato": "bebida",
        "cena_descricao": "O coquetel clássico que leva o nome do filme, associado à elegância e ao mundo da família Corleone.",
        "trivia": "O Godfather é um drink real, criado nos anos 1970 (na mesma época do lançamento do filme), e não aparece literalmente em nenhuma cena — é uma homenagem popular ao clássico.",
        "modo_preparo": "1. Misture o uísque escocês e o Amaretto em um copo baixo com gelo. 2. Mexa suavemente e sirva.",
        "ingredientes": [
            ("Uísque escocês", "bebida", 30, "ml"),
            ("Amaretto", "bebida", 30, "ml"),
        ],
    },

    # ============================================================
    # CORALINE (id 14836)
    # ============================================================
    {
        "filme_id": 14836,
        "nome_prato": "Milkshake de Manga",
        "tipo_de_prato": "bebida",
        "cena_descricao": "Inspirado nas cores vibrantes e no clima lúdico (e levemente inquietante) do mundo alternativo que Coraline descobre atrás da porta secreta.",
        "trivia": "Coraline (2009) foi um dos primeiros longas em stop-motion filmados em 3D, técnica que reforça a sensação de um mundo tátil e artesanal.",
        "modo_preparo": "1. Bata a manga, a banana, o iogurte e o leite de coco no liquidificador. 2. Adoce com açúcar demerara. 3. Sirva decorado com folhas de hortelã.",
        "ingredientes": [
            ("Manga", "fruta", 150, "g"),
            ("Banana", "fruta", 1, "unidade"),
            ("Iogurte natural", "laticínio", 100, "g"),
            ("Leite de coco", "outro", 200, "ml"),
            ("Açúcar demerara", "doce", 50, "g"),
            ("Hortelã", "tempero", 5, "folhas"),
        ],
    },
    {
        "filme_id": 14836,
        "nome_prato": "Frango Assado com Purê de Batata",
        "tipo_de_prato": "salgado",
        "cena_descricao": 'A refeição farta e caseira preparada pela "Outra Mãe" no mundo espelhado — sedutoramente perfeita demais para ser verdade.',
        "trivia": "No filme, a comida do mundo alternativo é sempre visualmente exagerada — um sinal sutil, junto com os botões no lugar dos olhos, de que algo ali não é real.",
        "modo_preparo": (
            "1. Tempere o frango com sal, pimenta e alho, e asse até dourar. "
            "2. Cozinhe as batatas e amasse com manteiga, creme de leite e leite. "
            "3. Refogue a cebola na margarina e sirva por cima do purê."
        ),
        "ingredientes": [
            ("Frango", "proteína", 1.5, "kg"),
            ("Batata", "vegetal", 1, "kg"),
            ("Manteiga", "laticínio", 50, "g"),
            ("Creme de leite", "laticínio", 100, "ml"),
            ("Sal", "tempero", 1, "colher (sopa)"),
            ("Pimenta do reino", "tempero", 1, "colher (chá)"),
            ("Alho", "tempero", 3, "dentes"),
            ("Cebola", "vegetal", 1, "unidade"),
            ("Leite", "laticínio", 1, "caixinha"),
            ("Margarina", "laticínio", 1, "colher (sopa)"),
        ],
    },
    {
        "filme_id": 14836,
        "nome_prato": "Bolo Welcome Home",
        "tipo_de_prato": "doce",
        "cena_descricao": "Um bolo colorido e chamativo, no estilo dos exageros visuais e doces armadilhas do mundo paralelo de Coraline.",
        "trivia": "A estética \"doce demais para ser verdade\" é um recurso visual recorrente em filmes de Henry Selick, também diretor de O Estranho Mundo de Jack.",
        "modo_preparo": (
            "1. Prepare uma massa básica com açúcar, óleo e farinha com fermento. "
            "2. Derreta o chocolate semiamargo com o creme para bater para o recheio. "
            "3. Cubra com chocolate branco tingido nas cores desejadas. "
            "4. Finalize com o frosting de queijo creme."
        ),
        "ingredientes": [
            ("Açúcar", "doce", 200, "g"),
            ("Óleo suave", "outro", 120, "ml"),
            ("Farinha de fermentação", "grão/farinha", 2, "colheres (sopa)"),
            ("Chocolate semiamargo", "doce", 200, "g"),
            ("Creme para bater", "laticínio", 200, "ml"),
            ("Chocolate branco", "doce", 1, "barra"),
            ("Corante amarelo", "outro", 1, "pitada"),
            ("Corante rosa", "outro", 1, "pitada"),
            ("Corante vermelho", "outro", 1, "pitada"),
            ("Frosting de queijo creme", "doce", 1, "barra"),
        ],
    },

    # ============================================================
    # HARRY POTTER E O PRISIONEIRO DE AZKABAN (id 673)
    # ============================================================
    {
        "filme_id": 673,
        "nome_prato": "Cerveja Amanteigada",
        "tipo_de_prato": "bebida",
        "cena_descricao": "A bebida servida em Hogsmeade, vilarejo que os alunos de Hogwarts a partir do 3º ano podem visitar — introduzida nesse filme da saga.",
        "trivia": "Nos parques temáticos do Wizarding World, a Cerveja Amanteigada é vendida de verdade (sem álcool), inspirada diretamente nessa referência dos livros e filmes.",
        "modo_preparo": (
            "1. Misture o sorvete de creme com açúcar mascavo, manteiga e as especiarias (canela, cravo, noz-moscada, gengibre). "
            "2. Adicione o extrato de baunilha. "
            "3. Complete com o espumante e o refrigerante de creme na hora de servir."
        ),
        "ingredientes": [
            ("Sorvete de creme", "doce", 450, "ml"),
            ("Açúcar mascavo", "doce", 200, "g"),
            ("Manteiga", "laticínio", 4, "colheres (sopa)"),
            ("Canela em pó", "tempero", 1, "colher (chá)"),
            ("Cravo em pó", "tempero", 0.5, "colher (chá)"),
            ("Noz-moscada", "tempero", 0.5, "colher (chá)"),
            ("Gengibre em pó", "tempero", 1, "colher (chá)"),
            ("Espumante", "bebida", 1, "dose"),
            ("Refrigerante de creme", "bebida", 1, "dose"),
            ("Extrato de baunilha", "doce", 0.5, "colher (chá)"),
        ],
    },

    # ============================================================
    # HARRY POTTER E A ORDEM DA FÊNIX (id 675)
    # ============================================================
    {
        "filme_id": 675,
        "nome_prato": "Empadão de Carne (Steak and Kidney Pie)",
        "tipo_de_prato": "salgado",
        "cena_descricao": "Um clássico prato britânico do tipo servido nos banquetes e refeições do Salão Principal de Hogwarts.",
        "trivia": "Steak and Kidney Pie é um prato tradicional inglês do século XIX, presente no cardápio de refeições britânicas citado nos livros de Harry Potter.",
        "modo_preparo": (
            "1. Doure a carne e os rins em óleo vegetal com cebola, cogumelos e aipo. "
            "2. Adicione o caldo de carne, o molho Worcestershire, o tomilho e o louro, e cozinhe até engrossar com o amido de milho. "
            "3. Cubra com purê de batata (batata, manteiga, leite e sal) e leve ao forno até dourar."
        ),
        "ingredientes": [
            ("Carne de gado", "proteína", 1, "kg"),
            ("Rins de cordeiro", "proteína", 500, "g"),
            ("Cebola", "vegetal", 2, "unidades"),
            ("Cogumelos", "vegetal", 200, "g"),
            ("Aipo", "vegetal", 1, "raiz"),
            ("Caldo de carne", "outro", 300, "ml"),
            ("Amido de milho", "grão/farinha", 100, "ml"),
            ("Óleo vegetal", "outro", 2, "colheres (sopa)"),
            ("Batata", "vegetal", 1, "kg"),
            ("Manteiga", "laticínio", 100, "g"),
            ("Leite", "laticínio", 100, "ml"),
            ("Sal", "tempero", 1, "colher (chá)"),
            ("Molho Worcestershire", "outro", 1, "colher (sopa)"),
            ("Tomilho", "tempero", 1, "colher (chá)"),
            ("Folha de louro", "tempero", 2, "folhas"),
        ],
    },

    # ============================================================
    # HARRY POTTER E A PEDRA FILOSOFAL (id 671)
    # ============================================================
    {
        "filme_id": 671,
        "nome_prato": "Bolo Happee Birthdae",
        "tipo_de_prato": "doce",
        "cena_descricao": "O bolo desajeitado, com a cobertura escrita à mão, que Hagrid entrega a Harry ao buscá-lo na cabana no meio do mar.",
        "trivia": "É o primeiro presente de aniversário que Harry recebe na vida, já que os Dursley nunca comemoravam sua data.",
        "modo_preparo": (
            "1. Prepare uma massa de chocolate com ovos, farinha, fermento, bicarbonato, suco de limão, leite morno, ovo, óleo e café. "
            "2. Derreta o chocolate semiamargo e o branco separadamente para as coberturas. "
            "3. Misture o cream cheese com o creme de leite para o recheio. "
            "4. Monte, cubra e finalize com detalhes nas cores rosa e verde."
        ),
        "ingredientes": [
            ("Ovos", "proteína", 6, "unidades"),
            ("Chocolate em pó", "doce", 100, "g"),
            ("Farinha de trigo", "grão/farinha", 105, "g"),
            ("Fermento químico", "outro", 0.5, "colher (chá)"),
            ("Bicarbonato de sódio", "outro", 1, "colher (chá)"),
            ("Suco de limão", "fruta", 0.5, "colher (chá)"),
            ("Leite", "laticínio", 120, "ml"),
            ("Ovo", "proteína", 1, "unidade"),
            ("Óleo", "outro", 60, "ml"),
            ("Café", "bebida", 80, "ml"),
            ("Chocolate semiamargo", "doce", 250, "g"),
            ("Chocolate branco", "doce", 250, "g"),
            ("Cream cheese", "laticínio", 150, "g"),
            ("Creme de leite", "laticínio", 100, "ml"),
            ("Corante gel rosa", "outro", 1, "pitada"),
            ("Corante gel verde", "outro", 1, "pitada"),
        ],
    },

    # ============================================================
    # PERCY JACKSON E O LADRÃO DE RAIOS (id 32657)
    # ============================================================
    {
        "filme_id": 32657,
        "nome_prato": "Cookie Azul",
        "tipo_de_prato": "doce",
        "cena_descricao": "Referência à comida azul que a mãe de Percy, Sally Jackson, sempre preparava para ele — um símbolo de conforto e do vínculo entre os dois.",
        "trivia": "A comida azul é um detalhe carinhoso criado pelo autor Rick Riordan nos livros, representando a teimosia afetuosa de Sally em desafiar convenções.",
        "modo_preparo": (
            "1. Bata a manteiga com os açúcares até ficar cremoso. "
            "2. Adicione o ovo e o extrato de baunilha. "
            "3. Incorpore a farinha, o fermento, o bicarbonato, o amido de milho e o sal. "
            "4. Misture as gotas de chocolate e os corantes azul e violeta. "
            "5. Asse em porções até dourar as bordas."
        ),
        "ingredientes": [
            ("Manteiga", "laticínio", 200, "g"),
            ("Açúcar cristal", "doce", 1, "xícara"),
            ("Açúcar demerara", "doce", 1, "xícara"),
            ("Ovo", "proteína", 1, "unidade"),
            ("Extrato de baunilha", "doce", 2, "colheres (sopa)"),
            ("Farinha de trigo", "grão/farinha", 2.5, "xícaras"),
            ("Fermento", "outro", 1, "colher (chá)"),
            ("Gotas de chocolate", "doce", 1, "xícara"),
            ("Gotas de chocolate branco", "doce", 1, "xícara"),
            ("Corante alimentício azul", "outro", 1, "pitada"),
            ("Corante alimentício violeta", "outro", 1, "pitada"),
            ("Amido de milho", "grão/farinha", 3, "colheres (sopa)"),
            ("Sal", "tempero", 1, "pitada"),
            ("Bicarbonato de sódio", "outro", 0.5, "colher (chá)"),
        ],
    },
    {
        "filme_id": 32657,
        "nome_prato": "Chips de Tortilha Azuis com Dip",
        "tipo_de_prato": "salgado",
        "cena_descricao": "Um lanche no espírito da comida azul de Sally Jackson, reinventado aqui como guacamole para acompanhar as tortillas.",
        "trivia": "Assim como o Cookie Azul, essa é uma releitura livre do tema \"comida azul\" da saga — sinta-se à vontade para tingir as tortillas com corante alimentício azul.",
        "modo_preparo": (
            "1. Amasse o abacate com o tomate picado, o óleo de oliva, o coentro, a cebola e a cúrcuma para o guacamole. "
            "2. Sirva com tortillas (tingidas de azul, se quiser manter o tema)."
        ),
        "ingredientes": [
            ("Abacate", "fruta", 3, "unidades"),
            ("Tomate", "vegetal", 2, "unidades"),
            ("Óleo de oliva", "outro", 3, "colheres (sopa)"),
            ("Coentro", "tempero", 1, "colher (sopa)"),
            ("Cebola", "vegetal", 1, "unidade"),
            ("Cúrcuma", "tempero", 1, "colher (chá)"),
        ],
    },
    {
        "filme_id": 32657,
        "nome_prato": "Néctar dos Deuses",
        "tipo_de_prato": "bebida",
        "cena_descricao": "Inspirado no néctar mitológico consumido pelos deuses gregos no Olimpo, reimaginado aqui como uma bebida doce e cremosa.",
        "trivia": "Na mitologia grega original, o néctar (junto com a ambrosia) era o que dava imortalidade aos deuses — beber ou comer demais era perigoso até para eles.",
        "modo_preparo": "1. Bata no liquidificador o leite condensado, o leite de vaca, o achocolatado e a castanha-do-pará. 2. Sirva bem gelado.",
        "ingredientes": [
            ("Leite condensado", "doce", 200, "g"),
            ("Achocolatado granulado", "doce", 100, "g"),
            ("Castanha-do-pará granulado", "outro", 50, "g"),
            ("Leite de vaca", "laticínio", 1, "xícara"),
        ],
    },    # ============================================================
    # A PRINCESA E O SAPO (id 12162)
    # ============================================================
    {
        "filme_id": 12162,
        "nome_prato": "Gumbo",
        "tipo_de_prato": "salgado",
        "cena_descricao": "O ensopado crioulo que Tiana prepara ao longo do filme, receita herdada de seu pai James — o prato que representa seu sonho de ter o próprio restaurante.",
        "trivia": "O gumbo é um prato símbolo da culinária cajun/crioula da Louisiana, com influências francesas, africanas e indígenas — retratado com bastante autenticidade no filme.",
        "modo_preparo": (
            "1. Faça um roux dourando a farinha no óleo. "
            "2. Refogue cebola, pimentão e aipo. "
            "3. Adicione alho, tempero cajun e o caldo de galinha aos poucos. "
            "4. Junte a linguiça defumada e o frango, e cozinhe até apurar. "
            "5. Sirva sobre arroz branco."
        ),
        "ingredientes": [
            ("Farinha de trigo", "grão/farinha", 1, "xícara"),
            ("Óleo vegetal", "outro", 1, "xícara"),
            ("Salsão", "vegetal", 3, "talos"),
            ("Cebola", "vegetal", 2, "unidades"),
            ("Pimentão verde", "vegetal", 2, "unidades"),
            ("Alho", "tempero", 5, "dentes"),
            ("Tempero cajun", "tempero", 2, "colheres (chá)"),
            ("Caldo de galinha", "outro", 6, "xícaras"),
            ("Folha de louro", "tempero", 2, "folhas"),
            ("Tomilho", "tempero", 1, "colher (chá)"),
            ("Linguiça defumada", "proteína", 450, "g"),
            ("Frango", "proteína", 900, "g"),
            ("Sal", "tempero", 1, "colher (chá)"),
            ("Pimenta do reino", "tempero", 1, "colher (chá)"),
            ("Arroz branco", "grão/farinha", 2, "xícaras"),
        ],
    },
    {
        "filme_id": 12162,
        "nome_prato": "Beignets",
        "tipo_de_prato": "doce",
        "cena_descricao": 'A cena em que Charlotte pede a Tiana que faça beignets para o baile de máscaras, pagamento que ajuda Tiana a comprar o antigo moinho para seu restaurante — e o momento em que Big Daddy enfia um beignet na boca de Lottie.',
        "trivia": "O beignet é considerado o doce oficial do estado da Louisiana, tradicionalmente servido no Café du Monde, em Nova Orleans.",
        "modo_preparo": (
            "1. Dissolva o fermento no leite morno com o açúcar e deixe espumar. "
            "2. Misture com o ovo, a manteiga derretida e o sal. "
            "3. Incorpore a farinha aos poucos até formar uma massa lisa, e deixe descansar. "
            "4. Abra a massa, corte em quadrados e frite até dourar. "
            "5. Finalize com uma boa camada de açúcar de confeiteiro."
        ),
        "ingredientes": [
            ("Leite", "laticínio", 1, "xícara"),
            ("Açúcar", "doce", 0.33, "xícara"),
            ("Fermento biológico seco", "outro", 1.5, "colher (chá)"),
            ("Farinha de trigo", "grão/farinha", 3.5, "xícaras"),
            ("Ovo", "proteína", 1, "unidade"),
            ("Manteiga", "laticínio", 2, "colheres (sopa)"),
            ("Sal", "tempero", 0.5, "colher (chá)"),
            ("Óleo para fritura", "outro", 1, "litro"),
            ("Açúcar de confeiteiro", "doce", 0.5, "xícara"),
        ],
    },
    {
        "filme_id": 12162,
        "nome_prato": "Swamp Soda",
        "tipo_de_prato": "bebida",
        "cena_descricao": "⚠️ Esta bebida NÃO aparece no filme — é servida no Tiana's Bayou Lounge, bar temático a bordo do navio Disney Adventure, inspirado no pântano e nos vaga-lumes da cena de Ray com Tiana e Naveen.",
        "trivia": "A Disney não divulga a receita oficial dos drinks dos seus navios — esta é uma aproximação caseira, com a estética 'verde brilhante de pântano' que o drink original busca recriar.",
        "modo_preparo": "1. Misture o refrigerante de limão com o xarope de melancia e o suco de lima. 2. Adicione gelo e decore com folhas de hortelã e uma bala de gelatina em formato de sapo.",
        "ingredientes": [
            ("Refrigerante de limão", "bebida", 200, "ml"),
            ("Xarope de melancia", "doce", 30, "ml"),
            ("Suco de lima", "fruta", 15, "ml"),
            ("Hortelã", "tempero", 3, "folhas"),
        ],
    },

    # ============================================================
    # GREASE: NOS TEMPOS DA BRILHANTINA (id 621)
    # ============================================================
    {
        "filme_id": 621,
        "nome_prato": "Polar Burger com Tudo",
        "tipo_de_prato": "salgado",
        "cena_descricao": 'A cena na lanchonete Frosty Palace em que Danny pede um "Double Polar Burger com tudo" ao se reencontrar com a turma.',
        "trivia": 'No musical original da Broadway, a lanchonete se chamava "Burger Palace" — o nome foi trocado para "Frosty Palace" na versão do cinema.',
        "modo_preparo": (
            "1. Tempere e grelhe os hambúrgueres de carne. "
            "2. Monte no pão com queijo cheddar derretido, bacon, alface, tomate e cebola. "
            "3. Finalize com picles, ketchup e mostarda a gosto."
        ),
        "ingredientes": [
            ("Carne moída", "proteína", 300, "g"),
            ("Pão de hambúrguer", "grão/farinha", 2, "unidades"),
            ("Queijo cheddar", "laticínio", 2, "fatias"),
            ("Bacon", "proteína", 2, "fatias"),
            ("Alface", "vegetal", 2, "folhas"),
            ("Tomate", "vegetal", 2, "fatias"),
            ("Cebola", "vegetal", 2, "fatias"),
            ("Picles", "vegetal", 4, "fatias"),
            ("Ketchup", "outro", 1, "colher (sopa)"),
            ("Mostarda", "outro", 1, "colher (sopa)"),
        ],
    },
    {
        "filme_id": 621,
        "nome_prato": "Cherry Coke Float",
        "tipo_de_prato": "bebida",
        "cena_descricao": "O pedido de Danny na Frosty Palace, junto com o hambúrguer: um refrigerante de cereja com bola de sorvete.",
        "trivia": "Refrigerante com sorvete (o \"float\") era item clássico das lanchonetes americanas dos anos 1950, época retratada no filme.",
        "modo_preparo": "1. Coloque uma bola de sorvete de chocolate no copo. 2. Complete com refrigerante de cereja. 3. Sirva com canudo e colher.",
        "ingredientes": [
            ("Refrigerante de cereja", "bebida", 300, "ml"),
            ("Sorvete de chocolate", "doce", 2, "bolas"),
        ],
    },
    {
        "filme_id": 621,
        "nome_prato": "Milkshake de Morango",
        "tipo_de_prato": "bebida",
        "cena_descricao": "A cena em que Rizzo, irritada durante uma discussão com Kenickie na Frosty Palace, joga o milkshake de morango na cara dele.",
        "trivia": "Esse é o momento clássico de \"food slap\" (tapa com comida) do filme — um recurso cômico recorrente em comédias românticas da época.",
        "modo_preparo": "1. Bata no liquidificador o sorvete, o leite e os morangos até ficar cremoso. 2. Sirva bem gelado, decorado com um morango inteiro.",
        "ingredientes": [
            ("Sorvete de baunilha", "doce", 3, "bolas"),
            ("Leite", "laticínio", 150, "ml"),
            ("Morango", "fruta", 6, "unidades"),
            ("Açúcar", "doce", 1, "colher (sopa)"),
        ],
    },

]
