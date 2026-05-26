const menuToggle = document.querySelector("[data-menu-toggle]");
const menu = document.querySelector("[data-menu]");

if (menuToggle && menu) {
    menuToggle.addEventListener("click", () => {
        menu.classList.toggle("is-open");
    });

    menu.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            menu.classList.remove("is-open");
        });
    });
}

// Reveal on Scroll
const revealElements = document.querySelectorAll(".info-card, .section-stack > *, .hero-copy > *");

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.1 });

revealElements.forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
    revealObserver.observe(el);
});

// Add a CSS rule for the revealed state
const style = document.createElement("style");
style.textContent = `
    .revealed {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

document.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
        const targetId = button.getAttribute("data-copy-target");
        const target = document.getElementById(targetId);
        if (!target) {
            return;
        }

        const originalText = button.textContent;
        try {
            await navigator.clipboard.writeText(target.textContent.trim());
            button.textContent = "Copiado";
        } catch (error) {
            button.textContent = "Copie manualmente";
        }

        setTimeout(() => {
            button.textContent = originalText;
        }, 1600);
    });
});
