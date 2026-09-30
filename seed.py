"""
Script de população inicial do banco de dados (Seed).
Lê os dados de catalogo.py e busca informações complementares no TMDB.
"""

import time
from app.models.database import conectar, inicializar_banco
from app.services.tmdb import buscar_filme_por_id
from catalogo import FILMES, EXPERIENCIAS

def rodar_seed():
    print("Iniciando verificação e inserção de dados no banco...")
    inicializar_banco()

    filmes_novos = 0
    experiencias_novas = 0
    ingredientes_novos = 0

    with conectar() as conexao:
        
        # --- Processamento dos Filmes ---
        for filme in FILMES:
            ja_existe = conexao.execute(
                "SELECT 1 FROM filmes WHERE id = ?", (filme["id"],)
            ).fetchone()

            if ja_existe:
                continue

            print(f"Buscando metadados do filme: {filme['nome_filme']} (ID: {filme['id']})")
            dados_tmdb = buscar_filme_por_id(filme["id"])
            
            # Valores padrão caso a API do TMDB falhe
            if not dados_tmdb:
                dados_tmdb = {
                    "poster_url": None,
                    "sinopse": "Sinopse indisponível no momento.",
                    "ano_lancamento": None
                }
            
            conexao.execute(
                """
                INSERT INTO filmes (id, nome_filme, poster_url, sinopse, ano_lancamento)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    filme["id"],
                    filme["nome_filme"],
                    dados_tmdb.get("poster_url"),
                    dados_tmdb.get("sinopse"),
                    dados_tmdb.get("ano_lancamento"),
                ),
            )
            filmes_novos += 1
            time.sleep(0.5)  # Pausa para evitar bloqueio da API por excesso de requisições

        # --- Processamento das Experiências e Ingredientes ---
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
            experiencias_novas += 1

            for nome_ingred, categoria, qtde, unidade in experiencia["ingredientes"]:
                linha = conexao.execute(
                    "SELECT id FROM ingredientes WHERE nome = ?", (nome_ingred,)
                ).fetchone()

                if linha:
                    ingrediente_id = linha["id"]
                else:
                    cursor_ingred = conexao.execute(
                        "INSERT INTO ingredientes (nome, categoria) VALUES (?, ?)",
                        (nome_ingred, categoria),
                    )
                    ingrediente_id = cursor_ingred.lastrowid
                    ingredientes_novos += 1

                conexao.execute(
                    """
                    INSERT INTO experiencia_ingredientes
                        (experiencia_id, ingrediente_id, quantidade, unidade)
                    VALUES (?, ?, ?, ?)
                    """,
                    (experiencia_id, ingrediente_id, qtde, unidade),
                )

        conexao.commit()

    print("\nResumo da execução:")
    print(f"- Filmes adicionados: {filmes_novos}")
    print(f"- Experiências adicionadas: {experiencias_novas}")
    print(f"- Ingredientes cadastrados: {ingredientes_novos}")

if __name__ == "__main__":
    rodar_seed()
