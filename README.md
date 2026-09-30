# 🎬🍝 CineBites

**Onde cada prato tem uma cena.**

CineBites é uma plataforma que transforma o improviso culinário em uma experiência imersiva de cinema. O sistema conecta os ingredientes que você já tem em casa a pratos icônicos do cinema e da TV.

> Projeto original desenvolvido como Trabalho de Conclusão de Curso Técnico, evoluído para peça de portfólio profissional.

## 💡 O conceito

- **Caminho A — Food First:** você marca os ingredientes que tem em casa, e o sistema calcula qual experiência tem a maior compatibilidade (match parcial).
- **Caminho B — Movie First** *(planejado para a Fase 2)*: você busca um filme, e o sistema retorna as experiências associadas a ele.

## 🚧 Status atual

✅ Backend completo do **Caminho A**, testado de ponta a ponta, com catálogo de 6 filmes e 12 experiências.

- [x] Modelagem do banco de dados (SQLite)
- [x] Rotas `GET /ingredientes`, `POST /match`, `GET /experiencias/<id>`
- [x] Painel de administração interno (`/admin`) para edição visual
- [ ] Frontend web (HTML/CSS/JS)
- [ ] Caminho B (busca por filme, via API do TMDB)
- [ ] Aplicativo Android nativo (Kotlin)

## ▶️ Como rodar

```bash
pip install -r requirements.txt
python seed.py
python run.py
```

Acesse `http://127.0.0.1:5000/ingredientes` ou `http://127.0.0.1:5000/admin`.

## 📡 Rotas (Caminho A)

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/ingredientes` | Lista todos os ingredientes |
| `POST` | `/match` | Recebe `{"ingredientes_ids": [1,2,3]}` e retorna experiências ordenadas por compatibilidade |
| `GET` | `/experiencias/<id>` | Detalhes completos de uma experiência |
| `GET` | `/admin` | Painel de administração (uso local) |

## 📁 Como adicionar conteúdo novo

Edite `catalogo.py` (siga os exemplos comentados) e rode `python seed.py` — o script só insere o que ainda não existe, nunca duplica.
