"""
admin.py
--------
Um painel de administração simples, feito com o próprio Flask —
sem precisar instalar nenhum programa externo. Só funciona
localmente (http://127.0.0.1:5000/admin).

Rotas:
  GET  /admin                          -> menu com as tabelas editáveis
  GET  /admin/<tabela>                 -> lista os registros da tabela
  GET  /admin/<tabela>/editar/<id>     -> formulário de edição
  POST /admin/<tabela>/editar/<id>     -> salva as alterações
"""

from flask import Blueprint, request, redirect
from app.models.database import conectar

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

TABELAS_EDITAVEIS = {
    "filmes": ["id", "nome_filme", "poster_url", "sinopse", "ano_lancamento"],
    "experiencias": ["id", "filme_id", "nome_prato", "tipo_de_prato", "cena_descricao", "trivia", "modo_preparo"],
    "ingredientes": ["id", "nome", "categoria"],
}

CAMPOS_LONGOS = {"cena_descricao", "trivia", "modo_preparo", "sinopse"}


def pagina_base(titulo, conteudo_html):
    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>CineBites Admin — {titulo}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 2rem auto; max-width: 900px;
                    background: #faf7f2; color: #1c1c1e; }}
            h1 {{ color: #8B1E3F; }}
            table {{ border-collapse: collapse; width: 100%; background: white; margin-top: 1rem; }}
            th, td {{ border: 1px solid #ddd; padding: 8px 10px; text-align: left; font-size: 14px; vertical-align: top; }}
            th {{ background: #8B1E3F; color: white; }}
            tr:nth-child(even) {{ background: #f2f2f2; }}
            a {{ color: #8B1E3F; text-decoration: none; font-weight: bold; }}
            a:hover {{ text-decoration: underline; }}
            label {{ display: block; margin-top: 12px; font-weight: bold; font-size: 14px; }}
            input, textarea {{ width: 100%; padding: 8px; margin-top: 4px; box-sizing: border-box;
                                font-family: inherit; font-size: 14px; }}
            button {{ background: #8B1E3F; color: white; border: none; padding: 10px 20px;
                      margin-top: 16px; cursor: pointer; border-radius: 4px; font-size: 14px; }}
            button:hover {{ background: #6e1830; }}
            .voltar {{ display: inline-block; margin-bottom: 1rem; }}
        </style>
    </head>
    <body>
        <h1>🎬🍝 CineBites — Painel (uso local)</h1>
        <a class="voltar" href="/admin">← Voltar ao menu</a>
        {conteudo_html}
    </body>
    </html>
    """


@admin_bp.route("/")
def menu():
    itens = "".join(
        f'<li><a href="/admin/{tabela}">{tabela}</a></li>' for tabela in TABELAS_EDITAVEIS
    )
    return pagina_base("Menu", f"<ul>{itens}</ul>")


@admin_bp.route("/<tabela>")
def listar(tabela):
    if tabela not in TABELAS_EDITAVEIS:
        return "Tabela não encontrada.", 404

    colunas = TABELAS_EDITAVEIS[tabela]

    with conectar() as conexao:
        linhas = conexao.execute(
            f"SELECT {', '.join(colunas)} FROM {tabela}"
        ).fetchall()

    cabecalho = "".join(f"<th>{coluna}</th>" for coluna in colunas) + "<th>Ação</th>"

    corpo = ""
    for linha in linhas:
        celulas = "".join(
            f"<td>{linha[coluna] if linha[coluna] is not None else ''}</td>" for coluna in colunas
        )
        corpo += f"<tr>{celulas}<td><a href='/admin/{tabela}/editar/{linha['id']}'>Editar</a></td></tr>"

    tabela_html = f"<table><tr>{cabecalho}</tr>{corpo}</table>"
    return pagina_base(tabela, f"<h2>{tabela}</h2>{tabela_html}")


@admin_bp.route("/<tabela>/editar/<int:item_id>", methods=["GET", "POST"])
def editar(tabela, item_id):
    if tabela not in TABELAS_EDITAVEIS:
        return "Tabela não encontrada.", 404

    colunas = TABELAS_EDITAVEIS[tabela]
    colunas_editaveis = [coluna for coluna in colunas if coluna != "id"]

    with conectar() as conexao:
        if request.method == "POST":
            novos_valores = [request.form.get(coluna, "") for coluna in colunas_editaveis]
            set_clause = ", ".join(f"{coluna} = ?" for coluna in colunas_editaveis)
            conexao.execute(
                f"UPDATE {tabela} SET {set_clause} WHERE id = ?",
                (*novos_valores, item_id),
            )
            conexao.commit()
            return redirect(f"/admin/{tabela}")

        linha = conexao.execute(
            f"SELECT {', '.join(colunas)} FROM {tabela} WHERE id = ?", (item_id,)
        ).fetchone()

    if linha is None:
        return "Registro não encontrado.", 404

    campos_html = f"<p><strong>ID:</strong> {linha['id']} (não pode ser alterado)</p>"
    for coluna in colunas_editaveis:
        valor = linha[coluna] if linha[coluna] is not None else ""
        if coluna in CAMPOS_LONGOS:
            campos_html += f"<label>{coluna}</label><textarea name='{coluna}' rows='4'>{valor}</textarea>"
        else:
            campos_html += f"<label>{coluna}</label><input name='{coluna}' value='{valor}'>"

    formulario = f"<form method='POST'>{campos_html}<button type='submit'>Salvar alterações</button></form>"
    return pagina_base(f"Editar {tabela}", f"<h2>Editar {tabela} #{item_id}</h2>{formulario}")
