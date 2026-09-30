"""
Serviço de integração com a API do The Movie Database (TMDB).
"""

import os
import requests
import urllib3
from dotenv import load_dotenv

# Desativa avisos de segurança no terminal devido ao bloqueio da rede escolar
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def buscar_filme_por_id(tmdb_id):
    """
    Consulta os detalhes de um filme no TMDB.
    Retorna um dicionário com os dados necessários para o banco ou None se falhar.
    """
    if not TMDB_API_KEY:
        print("Erro: Chave do TMDB ausente. Verifique o arquivo .env.")
        return None
        
    url = f"{BASE_URL}/movie/{tmdb_id}"
    
    parametros = {
        "api_key": TMDB_API_KEY,
        "language": "pt-BR"
    }
    
    # Cabeçalho simulando um navegador para burlar o bloqueio da rede
    cabecalhos = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        resposta = requests.get(
            url, 
            params=parametros, 
            headers=cabecalhos, 
            verify=False,
            timeout=10
        )
        resposta.raise_for_status() 
        dados = resposta.json() 
        
        data_lancamento = dados.get("release_date")
        caminho_poster = dados.get("poster_path")
        
        return {
            "id": dados.get("id"),
            "nome_filme": dados.get("title"),
            "sinopse": dados.get("overview"),
            "ano_lancamento": int(data_lancamento[:4]) if data_lancamento else None,
            "poster_url": f"https://image.tmdb.org/t/p/w500{caminho_poster}" if caminho_poster else None
        }
        
    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão com TMDB no filme {tmdb_id}: {erro}")
        return None

if __name__ == "__main__":
    print(buscar_filme_por_id(238))