/**
 * app.js
 * ------
 * Lógica do frontend do CineBites.
 */

const API_BASE_URL = "http://127.0.0.1:5000";

const ingredientesSelecionados = new Set();

const NOMES_CATEGORIA = {
  "proteína": "Açougue & Proteínas",
  "vegetal": "Horta & Vegetais",
  "laticínio": "Laticínios & Queijos",
  "tempero": "Temperos & Especiarias",
  "doce": "Doces & Açúcares",
  "bebida": "Adega & Bebidas",
  "fruta": "Pomar & Frutas",
  "grão/farinha": "Grãos & Massas",
  "outro": "Outros"
};

const EMOJIS_CATEGORIA = {
  "proteína": "🥩",
  "vegetal": "🥬",
  "laticínio": "🧀",
  "tempero": "🌿",
  "doce": "🍯",
  "bebida": "🥤",
  "fruta": "🍎",
  "grão/farinha": "🌾",
  "outro": "🥫"
};

// Dicionário específico para os seus ingredientes ganharem vida!
const EMOJIS_INGREDIENTES = {
  // Pomar & Frutas
  "abacate": "🥑",
  "banana": "🍌",
  "limão siciliano": "🍋",
  "manga": "🥭",
  "morango": "🍓",
  "raspas de limão": "🍋",
  "suco de lima": "🍈",
  "suco de limão": "🍋",

  // Doces & Açúcares
  "achocolatado granulado": "🍫",
  "açúcar": "🍬",
  "açúcar cristal": "🍬",
  "açúcar de confeiteiro": "🧁",
  "açúcar demerara": "🍬",
  "açúcar mascavo": "🍮",
  "açúcar refinado": "🍬",
  "cacau em pó": "🍫",
  "chocolate ao leite": "🍫",
  "chocolate branco": "🥛",
  "chocolate em pó": "🍫",
  "chocolate semiamargo": "🍫",
  "extrato de baunilha": "🌼",
  "frosting de queijo creme": "🧁",
  "gotas de chocolate": "🍪",
  "gotas de chocolate branco": "🍪",
  "leite condensado": "🥫",
  "sorvete de baunilha": "🍨",
  "sorvete de chocolate": "🍨",
  "sorvete de creme": "🍨",
  "xarope de melancia": "🍉",

  // Horta & Vegetais
  "aipo": "🥬",
  "alface": "🥬",
  "alho-poró": "🧅",
  "batata": "🥔",
  "cebola": "🧅",
  "cebola roxa": "🧅",
  "cenoura": "🥕",
  "cogumelos": "🍄",
  "picles": "🥒",
  "pimentão verde": "🫑",
  "salsão": "🥬",
  "tomate": "🍅",
  "tomate pelado": "🍅",

  // Temperos & Especiarias
  "alho": "🧄",
  "canela em pó": "🍂",
  "coentro": "🌿",
  "cravo em pó": "🍂",
  "cúrcuma": "🟡",
  "erva doce": "🌿",
  "folha de louro": "🍃",
  "gengibre em pó": "🫚",
  "hortelã": "🌿",
  "louro": "🍃",
  "manjericão": "🌿",
  "noz-moscada": "🌰",
  "pimenta calabresa": "🌶️",
  "pimenta do reino": "⚫",
  "sal": "🧂",
  "tempero cajun": "🌶️",
  "tomilho": "🌿",

  // Adega & Bebidas
  "amaretto": "🥃",
  "cachaça": "🥃",
  "café": "☕",
  "espumante": "🥂",
  "refrigerante de cereja": "🍒",
  "refrigerante de creme": "🥤",
  "refrigerante de limão": "🥤",
  "uísque escocês": "🥃",
  "vinho marsala": "🍷",
  "vinho branco seco": "🥂",
  "vinho tinto": "🍷",
  "vinho tinto seco": "🍷",

  // Grãos & Massas
  "amido de milho": "🌽",
  "arroz branco": "🍚",
  "farinha de fermentação": "🌾",
  "farinha de trigo": "🌾",
  "pão de hambúrguer": "🍔",

  // Açougue & Proteínas
  "bacon": "🥓",
  "carne de gado": "🥩",
  "carne moída": "🥩",
  "clara de ovo": "🥚",
  "frango": "🍗",
  "linguiça calabresa": "🌭",
  "linguiça defumada": "🌭",
  "linguiça toscana": "🌭",
  "ovo": "🥚",
  "ovos": "🥚",
  "rins de cordeiro": "🥩",

  // Laticínios & Queijos
  "cream cheese": "🧀",
  "creme de leite": "🥣",
  "creme para bater": "🥣",
  "iogurte natural": "🍨",
  "leite": "🥛",
  "leite de vaca": "🥛",
  "manteiga": "🧈",
  "margarina": "🧈",
  "queijo cheddar": "🧀",
  "ricota fresca": "🧀",

  // Outros
  "azeite": "🫒",
  "banha de porco": "🥓",
  "bicarbonato de sódio": "🥄",
  "caldo de carne": "🫕",
  "caldo de galinha": "🫕",
  "castanha-do-pará granulado": "🌰",
  "corante alimentício azul": "🔵",
  "corante alimentício violeta": "🟣",
  "corante amarelo": "🟡",
  "corante gel rosa": "🩷",
  "corante gel verde": "🟢",
  "corante rosa": "🩷",
  "corante vermelho": "🔴",
  "fermento": "🫧",
  "fermento biológico seco": "🫧",
  "fermento químico": "🫧",
  "gordura vegetal": "🧈",
  "ketchup": "🍅",
  "leite de coco": "🥥",
  "molho worcestershire": "🍾",
  "mostarda": "🌭",
  "vinagre": "🍾",
  "água": "💧",
  "óleo": "🌻",
  "óleo de oliva": "🫒",
  "óleo para fritura": "🌻",
  "óleo suave": "🌻",
  "óleo vegetal": "🌻"
};

// ------------------------------------------------------------------
// Navegação entre telas
// ------------------------------------------------------------------
function mostrarTela(nomeTela) {
  document.querySelectorAll(".screen").forEach((secao) => {
    secao.hidden = secao.dataset.screen !== nomeTela;
  });
  window.scrollTo({ top: 0, behavior: "instant" });
}

document.querySelectorAll("[data-voltar-para]").forEach((botao) => {
  botao.addEventListener("click", () => mostrarTela(botao.dataset.voltarPara));
});

// ------------------------------------------------------------------
// TELA 1 — Despensa
// ------------------------------------------------------------------
async function carregarIngredientes() {
  const status = document.getElementById("ingredientes-status");
  
  try {
    const resposta = await fetch(`${API_BASE_URL}/ingredientes`);
    if (!resposta.ok) throw new Error("Resposta não OK");
    const ingredientes = await resposta.json();

    if (ingredientes.length === 0) {
      status.hidden = false;
      status.textContent = "Ainda não há ingredientes cadastrados no catálogo.";
      return;
    }

    renderizarIngredientes(ingredientes);
  } catch (erro) {
    status.hidden = false;
    status.textContent = "Não foi possível carregar os ingredientes. Confira se o servidor Flask está rodando.";
    console.error(erro);
  }
}

function renderizarIngredientes(ingredientes) {
  const lista = document.getElementById("ingredientes-lista");
  const grupos = {};
  
  for (const ingrediente of ingredientes) {
    const categoria = ingrediente.categoria || "outro";
    if (!grupos[categoria]) grupos[categoria] = [];
    grupos[categoria].push(ingrediente);
  }

  lista.innerHTML = "";

  for (const [categoria, itens] of Object.entries(grupos)) {
    const grupoEl = document.createElement("div");
    grupoEl.className = "grupo-categoria";

    const titulo = document.createElement("h3");
    titulo.className = "grupo-categoria__titulo";
    const emojiCategoria = EMOJIS_CATEGORIA[categoria] || "🥫";
    titulo.textContent = `${NOMES_CATEGORIA[categoria] || categoria}`;
    grupoEl.appendChild(titulo);

    const chipsWrap = document.createElement("div");
    chipsWrap.className = "chips-wrap";

    for (const ingrediente of itens) {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "chip";
      chip.setAttribute("aria-pressed", "false");
      
      // Procura o emoji específico, se não achar, usa o da categoria
      const nomeMinusculo = ingrediente.nome.toLowerCase();
      const emojiItem = EMOJIS_INGREDIENTES[nomeMinusculo] || emojiCategoria;
      
      chip.innerHTML = `
        <span class="chip-emoji">${emojiItem}</span>
        <span class="chip-nome">${escapeHtml(ingrediente.nome)}</span>
        <span class="chip-status">Adicionar</span>
      `;
      
      chip.addEventListener("click", () => alternarIngrediente(chip, ingrediente.id));
      chipsWrap.appendChild(chip);
    }

    grupoEl.appendChild(chipsWrap);
    lista.appendChild(grupoEl);
  }
}

function alternarIngrediente(chip, id) {
  const jaMarcado = ingredientesSelecionados.has(id);
  const statusSpan = chip.querySelector('.chip-status');

  if (jaMarcado) {
    ingredientesSelecionados.delete(id);
    chip.setAttribute("aria-pressed", "false");
    statusSpan.textContent = "Adicionar"; 
  } else {
    ingredientesSelecionados.add(id);
    chip.setAttribute("aria-pressed", "true");
    statusSpan.textContent = "Na despensa"; 
  }
  atualizarContadorSelecionados();
}

function atualizarContadorSelecionados() {
  const contador = document.getElementById("contagem-selecionados");
  const botaoBuscar = document.getElementById("btn-buscar-match");
  const quantidade = ingredientesSelecionados.size;

  contador.textContent = quantidade === 1 ? "1 item selecionado" : `${quantidade} itens selecionados`;
  botaoBuscar.disabled = quantidade === 0;
}

// ------------------------------------------------------------------
// TELA 2 — Resultados (ingressos)
// ------------------------------------------------------------------
document.getElementById("btn-buscar-match").addEventListener("click", buscarMatch);

async function buscarMatch() {
  const status = document.getElementById("resultados-status");
  const lista = document.getElementById("resultados-lista");
  status.hidden = true;
  lista.innerHTML = "";

  mostrarTela("resultados");

  try {
    const resposta = await fetch(`${API_BASE_URL}/match`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ingredientes_ids: Array.from(ingredientesSelecionados) }),
    });

    if (!resposta.ok) throw new Error("Resposta não OK");
    const resultados = await resposta.json();

    const comCompatibilidade = resultados.filter((r) => r.ingredientes_tem > 0);

    if (comCompatibilidade.length === 0) {
      status.hidden = false;
      status.textContent = "Nenhuma experiência combina com esses ingredientes ainda.";
      return;
    }

    renderizarResultados(comCompatibilidade);
  } catch (erro) {
    status.hidden = false;
    status.textContent = "Erro ao buscar combinações.";
    console.error(erro);
  }
}

function renderizarResultados(resultados) {
  const lista = document.getElementById("resultados-lista");
  lista.innerHTML = "";

  for (const resultado of resultados) {
    const ingresso = document.createElement("div");
    ingresso.className = "ingresso";
    ingresso.addEventListener("click", () => abrirSessao(resultado.experiencia_id));

    ingresso.innerHTML = `
      <div class="ingresso__info">
        <span class="ingresso__prato">🍽️ ${escapeHtml(resultado.nome_prato)}</span>
        <span class="ingresso__filme">🎬 Baseado em sua despensa atual</span>
      </div>
      <div class="ingresso__canhoto">
        <span class="ingresso__score">${resultado.ingredientes_tem}/${resultado.ingredientes_total}</span>
      </div>
    `;

    lista.appendChild(ingresso);
  }
}

// ------------------------------------------------------------------
// TELA 3 — Sessão (detalhe da experiência)
// ------------------------------------------------------------------
async function abrirSessao(experienciaId) {
  const container = document.getElementById("sessao-conteudo");
  container.innerHTML = `<p style="padding:40px; text-align:center;">Preparando sua sessão…</p>`;
  mostrarTela("sessao");

  try {
    const resposta = await fetch(`${API_BASE_URL}/experiencias/${experienciaId}`);
    if (!resposta.ok) throw new Error("Resposta não OK");
    const experiencia = await resposta.json();
    renderizarSessao(experiencia);
  } catch (erro) {
    container.innerHTML = `<p style="text-align:center;">Erro ao carregar sessão.</p>`;
    religarBotaoVoltar();
    console.error(erro);
  }
}

function renderizarSessao(experiencia) {
  const container = document.getElementById("sessao-conteudo");
  const passos = parseModoPreparo(experiencia.modo_preparo);
  const ingredientesHtml = experiencia.ingredientes
    .map(
      (ing) => `
        <li>
          <span>${escapeHtml(ing.nome)}</span>
          <span class="qtd">${formatarQuantidade(ing.quantidade)} ${escapeHtml(ing.unidade || "")}</span>
        </li>`
    )
    .join("");

  const passosHtml = passos.map((passo) => `<li>${escapeHtml(passo)}</li>`).join("");

  const filme = experiencia.filme;
  
  const posterHtml = filme.poster_url 
    ? `<img src="${escapeHtml(filme.poster_url)}" alt="Pôster" class="sessao-poster">` 
    : '';

  const sinopseHtml = filme.sinopse 
    ? `<div class="sessao-bloco">
         <p class="sessao-bloco__titulo">Sobre o Filme</p>
         <p class="sessao-sinopse">${escapeHtml(filme.sinopse)}</p>
       </div>` 
    : '';

  container.innerHTML = `
    <div class="sessao-hero">
      ${posterHtml}
      <div class="sessao-hero__inner">
        <h1 class="sessao-prato">${escapeHtml(experiencia.nome_prato)}</h1>
        <p class="sessao-filme">Filme: ${escapeHtml(filme.nome_filme)}${filme.ano_lancamento ? " (" + filme.ano_lancamento + ")" : ""}</p>
      </div>
    </div>

    <div class="sessao-corpo">
      ${sinopseHtml}

      ${experiencia.cena_descricao ? `<div class="sessao-bloco"><p class="sessao-bloco__titulo">A cena</p><p class="sessao-cena">${escapeHtml(experiencia.cena_descricao)}</p></div>` : ""}
      
      ${experiencia.trivia ? `<div class="sessao-bloco"><p class="sessao-bloco__titulo">Curiosidade</p><p class="sessao-cena">${escapeHtml(experiencia.trivia)}</p></div>` : ""}

      <div class="sessao-bloco">
        <p class="sessao-bloco__titulo">Ingredientes</p>
        <ul class="sessao-ingredientes">${ingredientesHtml}</ul>
      </div>

      <div class="sessao-bloco">
        <p class="sessao-bloco__titulo">Modo de preparo</p>
        <ol class="sessao-passos">${passosHtml}</ol>
      </div>
    </div>
  `;
}

function parseModoPreparo(texto) {
  if (!texto) return [];
  const partes = texto.split(/\d+\.\s+/).map((p) => p.trim()).filter((p) => p.length > 0);
  return partes.length > 0 ? partes : [texto];
}

function formatarQuantidade(numero) {
  if (numero === null || numero === undefined) return "";
  return Number.isInteger(numero) ? String(numero) : String(numero).replace(".", ",");
}

function religarBotaoVoltar() {
  document.querySelectorAll("[data-voltar-para]").forEach((botao) => {
    botao.addEventListener("click", () => mostrarTela(botao.dataset.voltarPara));
  });
}

function escapeHtml(texto) {
  const div = document.createElement("div");
  div.textContent = texto ?? "";
  return div.innerHTML;
}

// Inicia a aplicação carregando a despensa
carregarIngredientes();