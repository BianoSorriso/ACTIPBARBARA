const PIX_EMAIL = "acitp2010@gmail.com";

function copiarPix() {
  navigator.clipboard
    .writeText(PIX_EMAIL)
    .then(() => marcarBotaoCopiado())
    .catch(() => alert(`Não foi possível copiar automaticamente. Copie manualmente: ${PIX_EMAIL}`));
}

function marcarBotaoCopiado() {
  const botao = document.querySelector(".copy-email-btn");
  if (!botao) return;

  botao.classList.add("copied");
  setTimeout(() => botao.classList.remove("copied"), 1200);
}

function adicionarClasseComDelay(elementos, classe, intervalo = 120) {
  elementos.forEach((elemento, index) => {
    setTimeout(() => elemento.classList.add(classe), index * intervalo);
  });
}

function observarElemento(seletor, aoAparecer, threshold = 0.25) {
  const elemento = document.querySelector(seletor);
  if (!elemento) return;

  const observer = new IntersectionObserver((entries) => {
    if (!entries.some((entry) => entry.isIntersecting)) return;

    aoAparecer();
    observer.unobserve(elemento);
  }, { threshold });

  observer.observe(elemento);
}

function iniciarAnimacoes() {
  observarElemento(".history-section", () => {
    document.querySelector(".history-header .section-title")?.classList.add("title-visible");
    document.querySelector(".history-desc")?.classList.add("typing-active");
    document.querySelectorAll(".history-pop-item").forEach((item) => item.classList.add("pop-visible"));
  });

  observarElemento(".services-header", () => {
    adicionarClasseComDelay(document.querySelectorAll(".services-animate-title"), "title-visible");
    document.querySelector(".services-desc")?.classList.add("typing-active");
  }, 0.45);

  observarElemento(".services-grid", () => {
    document.querySelectorAll(".services-pop-item").forEach((item) => item.classList.add("pop-visible"));
  });

  observarElemento(".events-header", () => {
    adicionarClasseComDelay(document.querySelectorAll(".events-animate-title"), "title-visible");
  }, 0.45);

  observarElemento(".events-grid", () => {
    document.querySelectorAll(".events-pop-item").forEach((item) => item.classList.add("pop-visible"));
  });

  observarElemento(".involve-section", () => {
    adicionarClasseComDelay(document.querySelectorAll(".involve-animate-title"), "title-visible");
    document.querySelector(".involve-desc")?.classList.add("typing-active");

    setTimeout(() => {
      document.querySelectorAll(".involve-slide-left, .involve-slide-right").forEach((item) => item.classList.add("slide-visible"));
      document.querySelectorAll(".involve-pop-item").forEach((item) => item.classList.add("pop-visible"));
    }, 350);
  });

  observarElemento(".testimonials-section", () => {
    adicionarClasseComDelay(document.querySelectorAll(".testimonials-animate-title"), "title-visible");

    setTimeout(() => {
      document.querySelectorAll(".testimonials-slide-item").forEach((item) => item.classList.add("slide-visible"));
      document.querySelectorAll(".testimonials-pop-item").forEach((item) => item.classList.add("pop-visible"));
    }, 350);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".copy-email-btn, .copy-pix-btn").forEach((botao) => {
    botao.addEventListener("click", copiarPix);
  });

  iniciarAnimacoes();
});
