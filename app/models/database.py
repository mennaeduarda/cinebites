"""
database.py
------------
Este arquivo cuida de TUDO que envolve falar com o banco SQLite.
As rotas (em app/routes/) nunca escrevem SQL diretamente — elas
chamam as funções daqui. Isso mantém as duas responsabilidades
separadas: "rotas" decidem o QUE responder, "database" decide COMO
buscar os dados.
"""

import sqlite3
import os

# Caminho do arquivo do banco. Fica na pasta database/, um nível acima.
CAMINHO_BANCO = os.path.join(
    os.path.dirname(__file__), "..", "..", "database", "cinebites.db"
)
CAMINHO_SCHEMA = os.path.join(
    os.path.dirname(__file__), "..", "..", "database", "schema.sql"
)


def conectar():
    """
    Abre uma conexão com o banco SQLite.

    row_factory = sqlite3.Row faz com que cada linha retornada se
    comporte como um dicionário (dá pra acessar por nome de coluna,
    tipo linha["nome"], em vez de só por índice numérico).
    """
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    """
    Cria as tabelas (se ainda não existirem) executando o schema.sql.
    Chamado uma vez quando o servidor Flask liga.
    """
    with conectar() as conexao:
        with open(CAMINHO_SCHEMA, "r", encoding="utf-8") as arquivo:
            conexao.executescript(arquivo.read())


# ------------------------------------------------------------------
# Funções usadas pelas rotas do Caminho A
# ------------------------------------------------------------------

def listar_ingredientes():
    """Retorna todos os ingredientes cadastrados, ordenados por nome."""
    with conectar() as conexao:
        linhas = conexao.execute(
            "SELECT id, nome, categoria FROM ingredientes ORDER BY nome"
        ).fetchall()
        return [dict(linha) for linha in linhas]


def calcular_match(ingredientes_ids_usuario):
    """
    O coração do Caminho A.

    Recebe uma lista de IDs de ingredientes que o usuário marcou como
    "tenho em casa" e devolve todas as experiências ORDENADAS da que
    tem mais ingredientes em comum para a que tem menos.

    Para cada experiência, calculamos:
      - quantos ingredientes ELA PEDE no total
      - quantos desses o usuário TEM
      - score = tem / total (ex: 4/5 = 0.8)
    """
    with conectar() as conexao:
        experiencias = conexao.execute(
            "SELECT id, nome_prato FROM experiencias"
        ).fetchall()

        resultado = []

        for experiencia in experiencias:
            ingredientes_da_experiencia = conexao.execute(
                """
                SELECT ingrediente_id
                FROM experiencia_ingredientes
                WHERE experiencia_id = ?
                """,
                (experiencia["id"],),
            ).fetchall()

            ids_necessarios = {linha["ingrediente_id"] for linha in ingredientes_da_experiencia}
            total_necessario = len(ids_necessarios)

            if total_necessario == 0:
                continue  # experiência sem ingredientes cadastrados, ignora

            ids_que_usuario_tem = ids_necessarios.intersection(ingredientes_ids_usuario)
            quantidade_tem = len(ids_que_usuario_tem)

            resultado.append({
                "experiencia_id": experiencia["id"],
                "nome_prato": experiencia["nome_prato"],
                "ingredientes_tem": quantidade_tem,
                "ingredientes_total": total_necessario,
                "score": round(quantidade_tem / total_necessario, 2),
            })

        # Ordena da melhor compatibilidade para a pior
        resultado.sort(key=lambda item: item["score"], reverse=True)
        return resultado


def buscar_experiencia_completa(experiencia_id):
    """
    Retorna todos os detalhes de UMA experiência: dados do prato, do
    filme associado, e a lista de ingredientes com quantidade/unidade.
    Usado na tela de sessão (o resultado final que o usuário vê).

    Devolve None se a experiência não existir.
    """
    with conectar() as conexao:
        experiencia = conexao.execute(
            """
            SELECT e.id, e.nome_prato, e.tipo_de_prato, e.cena_descricao,
                   e.trivia, e.modo_preparo,
                   f.id AS filme_id, f.nome_filme, f.poster_url, f.sinopse, f.ano_lancamento
            FROM experiencias e
            JOIN filmes f ON f.id = e.filme_id
            WHERE e.id = ?
            """,
            (experiencia_id,),
        ).fetchone()

        if experiencia is None:
            return None

        ingredientes = conexao.execute(
            """
            SELECT i.nome, ei.quantidade, ei.unidade
            FROM experiencia_ingredientes ei
            JOIN ingredientes i ON i.id = ei.ingrediente_id
            WHERE ei.experiencia_id = ?
            """,
            (experiencia_id,),
        ).fetchall()

        return {
            "id": experiencia["id"],
            "nome_prato": experiencia["nome_prato"],
            "tipo_de_prato": experiencia["tipo_de_prato"],
            "cena_descricao": experiencia["cena_descricao"],
            "trivia": experiencia["trivia"],
            "modo_preparo": experiencia["modo_preparo"],
            "filme": {
                "id": experiencia["filme_id"],
                "nome_filme": experiencia["nome_filme"],
                "poster_url": experiencia["poster_url"],
                "sinopse": experiencia["sinopse"],
                "ano_lancamento": experiencia["ano_lancamento"],
            },
            "ingredientes": [dict(ingrediente) for ingrediente in ingredientes],
        }
