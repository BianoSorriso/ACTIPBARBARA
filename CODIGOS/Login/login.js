const senha = document.getElementById("isenha");
const olho = document.getElementById("versenha");

        olho.addEventListener("click", function() {
            if (senha.type === "password") {
                senha.type = "text";
                olho.textContent = "🙈";
            } else {
                senha.type = "password";
                olho.textContent = "👁";
            }
        });

        document.getElementById("loginForm").addEventListener("submit", function(e) {
            e.preventDefault();
            alert("Login realizado com sucesso! (Simulação)");
        });