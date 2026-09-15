-- ============================================================
-- CineBites — Schema do Banco de Dados (SQLite)
-- Fase 1 (MVP) — cobre o Caminho A (ingredientes → experiência)
-- ============================================================

-- Filmes: cache local dos dados vindos da API do TMDB
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY,           -- reaproveita o próprio ID do TMDB
    nome_filme TEXT NOT NULL,
    poster_url TEXT,
    sinopse TEXT,
    ano_lancamento INTEGER
);

-- Experiências: a entidade central (prato + cena + trivia), ligada a um filme
CREATE TABLE IF NOT EXISTS experiencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filme_id INTEGER NOT NULL,
    nome_prato TEXT NOT NULL,
    tipo_de_prato TEXT NOT NULL,  -- salgado, doce, bebida...
    cena_descricao TEXT,
    trivia TEXT,
    modo_preparo TEXT,
    FOREIGN KEY (filme_id) REFERENCES filmes(id)
);

-- Ingredientes: catálogo geral, reutilizado entre experiências
CREATE TABLE IF NOT EXISTS ingredientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    categoria TEXT
);

-- Tabela de ligação N:N entre experiências e ingredientes
CREATE TABLE IF NOT EXISTS experiencia_ingredientes (
    experiencia_id INTEGER NOT NULL,
    ingrediente_id INTEGER NOT NULL,
    quantidade REAL,
    unidade TEXT,
    PRIMARY KEY (experiencia_id, ingrediente_id),
    FOREIGN KEY (experiencia_id) REFERENCES experiencias(id),
    FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id)
);

-- Usuários (Fase 2 — login opcional, não usado ainda no Caminho A)
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL
);

-- Despensa do usuário logado (Fase 2)
CREATE TABLE IF NOT EXISTS despensa_usuario (
    usuario_id INTEGER NOT NULL,
    ingrediente_id INTEGER NOT NULL,
    PRIMARY KEY (usuario_id, ingrediente_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (ingrediente_id) REFERENCES ingredientes(id)
);
