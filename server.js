const express = require('express');
const cors = require('cors');

const app = express();
app.use(express.json()); // Habilita o recebimento de dados em JSON
app.use(cors());

// Simulação de um banco de dados em memória (pode ser substituído por MongoDB, PostgreSQL, etc.)
let cardapiosFilmes = [
  { id: 1, filme: "Ratatouille", prato: "Ratatouille provençal", tmdb_id: 2062 },
  { id: 2, filme: "A Princesa e o Sapo", prato: "Gumbo de camarão", tmdb_id: 10196 }
];

// 1. Rota GET: Listar todos os pratos/filmes cadastrados
app.get('/api/cardapios', (req, res) => {
  res.json(cardapiosFilmes);
});

// 2. Rota POST: Adicionar um novo filme e prato ao sistema
app.post('/api/cardapios', (req, res) => {
  const { filme, prato, tmdb_id } = req.body;
  
  const novoItem = {
    id: cardapiosFilmes.length + 1,
    filme,
    prato,
    tmdb_id
  };

  cardapiosFilmes.push(novoItem);
  res.status(201).json({ mensagem: "Menu cadastrado com sucesso!", novoItem });
});

// Iniciar o servidor na porta 3000
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`API do CineChef rodando na porta ${PORT} 🚀`);
});