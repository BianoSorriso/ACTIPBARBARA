const eventos = [
    { titulo: "Feira de Adoção de Animais", descricao: "Venha conhecer e adotar um novo amigo! Contaremos com mais de 30 animais resgatados esperando por um lar.", imagem: "#d9d9d9" },
    { titulo: "Dia da Solidariedade", descricao: "Distribuição de cestas básicas e roupas para famílias em vulnerabilidade na região de Belford Roxo.", imagem: "#d9d9d9" },
    { titulo: "Workshop de Educação Ambiental", descricao: "Aprenda como reduzir o impacto ambiental no dia a dia com palestras e atividades práticas.", imagem: "#d9d9d9" },
    { titulo: "Bazar Beneficente", descricao: "Todo o valor arrecadado será revertido para a compra de medicamentos e alimentos para as famílias assistidas.", imagem: "#d9d9d9" },
    { titulo: "Caminhada pela Inclusão", descricao: "Participe da grande caminhada em prol da inclusão social e direitos das pessoas com deficiência.", imagem: "#d9d9d9" },
    { titulo: "Natal Solidário 2025", descricao: "Ajude a fazer o Natal de mais de 200 crianças mais brilhante com doações de brinquedos e alimentos.", imagem: "#d9d9d9" }
];

let eventosCarregados = 0;
const eventosPorVez = 2;
const container = document.getElementById('eventos-container');
const loader = document.getElementById('loader');

function criarEvento(evento, index) {
    const row = document.createElement('div');
    row.className = `evento-row ${index % 2 === 1 ? 'reverse' : ''}`;
    row.innerHTML = `
        <div class="evento-text">
            <h2>${evento.titulo}</h2>
            <p>${evento.descricao}</p>
        </div>
        <div class="evento-img" style="background: ${evento.imagem};"></div>
    `;
    return row;
}

function carregarMaisEventos() {
    if (eventosCarregados >= eventos.length) return;
    
    loader.style.display = 'block';

    setTimeout(() => {
        const start = eventosCarregados;
        const end = Math.min(start + eventosPorVez, eventos.length);

        for (let i = start; i < end; i++) {
            const eventoHTML = criarEvento(eventos[i], i);
            container.appendChild(eventoHTML);
        }

        eventosCarregados = end;
        loader.style.display = 'none';

        if (eventosCarregados >= eventos.length) {
            window.removeEventListener('scroll', handleScroll);
        }
    }, 700);
}

function handleScroll() {
    const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
    if (scrollTop + clientHeight >= scrollHeight - 350) {
        carregarMaisEventos();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    carregarMaisEventos();
    window.addEventListener('scroll', handleScroll);
});