from flask import Flask

from app.models.database import inicializar_banco
from app.routes.caminho_a import caminho_a_bp
from app.routes.admin import admin_bp


def create_app():
    app = Flask(__name__)

    @app.after_request
    def liberar_cors(resposta):
        resposta.headers["Access-Control-Allow-Origin"] = "*"
        resposta.headers["Access-Control-Allow-Headers"] = "Content-Type"
        resposta.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        return resposta

    inicializar_banco()

    app.register_blueprint(caminho_a_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def status():
        return {"status": "CineBites API rodando 🎬🍝"}

    return app
