"""
caminho_a.py
------------
As 3 rotas que fazem o Caminho A funcionar de ponta a ponta:

  GET  /ingredientes         -> lista pra montar a tela de seleção
  POST /match                -> recebe o que o usuário marcou, devolve o ranking
  GET  /experiencias/<id>    -> detalhes completos pra tela de sessão
"""

from flask import Blueprint, jsonify, request
from app.models import database

caminho_a_bp = Blueprint("caminho_a", __name__)


@caminho_a_bp.route("/ingredientes", methods=["GET"])
def get_ingredientes():
    """Devolve todos os ingredientes cadastrados no banco."""
    ingredientes = database.listar_ingredientes()
    return jsonify(ingredientes)


@caminho_a_bp.route("/match", methods=["POST"])
def post_match():
    """
    Espera receber um JSON assim:
        { "ingredientes_ids": [1, 2, 5] }
    """
    dados_recebidos = request.get_json(silent=True)

    if not dados_recebidos or "ingredientes_ids" not in dados_recebidos:
        return jsonify({"erro": "Envie um JSON com a chave 'ingredientes_ids'."}), 400

    ingredientes_ids = set(dados_recebidos["ingredientes_ids"])
    resultado = database.calcular_match(ingredientes_ids)
    return jsonify(resultado)


@caminho_a_bp.route("/experiencias/<int:experiencia_id>", methods=["GET"])
def get_experiencia(experiencia_id):
    """Devolve os detalhes completos de uma experiência (tela de sessão)."""
    experiencia = database.buscar_experiencia_completa(experiencia_id)

    if experiencia is None:
        return jsonify({"erro": "Experiência não encontrada."}), 404

    return jsonify(experiencia)
