"""
seed.py
-------
Lê o catálogo em catalogo.py e insere no banco SÓ o que ainda não
existe. NÃO apaga dados antigos — é seguro rodar sempre que você
adicionar uma experiência nova no catalogo.py.

Se você EDITAR um valor que já existe no catalogo.py (ex: corrigir
um texto), o seed.py não atualiza automaticamente — ele só insere
coisas novas. Para that caso, apague o database/cinebites.db e rode
o seed.py de novo (ele recria tudo do zero, sem duplicar nada).
"""

from app.models.database import conectar, inicializar_banco
from catalogo import FILMES, EXPERIENCIAS

inicializar_banco()

total_filmes_novos = 0
total_experiencias_novas = 0
total_ingredientes_novos = 0

with conectar() as conexao:

    # --- Filmes ---
    for filme in FILMES:
        ja_existe = conexao.execute(
            "SELECT 1 FROM filmes WHERE id = ?", (filme["id"],)
        ).fetchone()

        if ja_existe:
            continue

        conexao.execute(
            """
            INSERT INTO filmes (id, nome_filme, poster_url, sinopse, ano_lancamento)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                filme["id"],
                filme["nome_filme"],
                filme["poster_url"],
                filme["sinopse"],
                filme["ano_lancamento"],
            ),
        )
        total_filmes_novos += 1

    # --- Experiências (e seus ingredientes) ---
    for experiencia in EXPERIENCIAS:
        ja_existe = conexao.execute(
            """
            SELECT 1 FROM experiencias
            WHERE filme_id = ? AND nome_prato = ?
            """,
            (experiencia["filme_id"], experiencia["nome_prato"]),
        ).fetchone()

        if ja_existe:
            continue

        cursor = conexao.execute(
            """
            INSERT INTO experiencias
                (filme_id, nome_prato, tipo_de_prato, cena_descricao, trivia, modo_preparo)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                experiencia["filme_id"],
                experiencia["nome_prato"],
                experiencia["tipo_de_prato"],
                experiencia["cena_descricao"],
                experiencia["trivia"],
                experiencia["modo_preparo"],
            ),
        )
        experiencia_id = cursor.lastrowid
        total_experiencias_novas += 1

        for nome_ingrediente, categoria, quantidade, unidade in experiencia["ingredientes"]:
            linha = conexao.execute(
                "SELECT id FROM ingredientes WHERE nome = ?", (nome_ingrediente,)
            ).fetchone()

            if linha:
                ingrediente_id = linha["id"]
            else:
                cursor_ingrediente = conexao.execute(
                    "INSERT INTO ingredientes (nome, categoria) VALUES (?, ?)",
                    (nome_ingrediente, categoria),
                )
                ingrediente_id = cursor_ingrediente.lastrowid
                total_ingredientes_novos += 1

            conexao.execute(
                """
                INSERT INTO experiencia_ingredientes
                    (experiencia_id, ingrediente_id, quantidade, unidade)
                VALUES (?, ?, ?, ?)
                """,
                (experiencia_id, ingrediente_id, quantidade, unidade),
            )

    conexao.commit()

print(
    f"Concluído! {total_filmes_novos} filme(s) novo(s), "
    f"{total_experiencias_novas} experiência(s) nova(s), "
    f"{total_ingredientes_novos} ingrediente(s) novo(s)."
)
print("Se tudo já existia, os números acima aparecem como 0 — e está tudo certo, nada foi duplicado.")
