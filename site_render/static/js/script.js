// Função para iniciar o spinner de carregamento

function mostrarCarregamento() {
    document.querySelector('.loading').style.display = 'block';
    document.getElementById('resultado').style.display = 'none';
}

// Função para ocultar o spinner de carregamento
function ocultarCarregamento() {
    document.querySelector('.loading').style.display = 'none';
}

// Evento para o botão de verificação
document.addEventListener('DOMContentLoaded', function() {
    const verificarBtn = document.getElementById('verificar-btn');
    verificarBtn.addEventListener('click', function() {
        const url = document.getElementById('url').value;

        if (!url) {
            alert('Por favor, insira uma URL válida.');
            return;
        }

        // Mostra o spinner de carregamento
        mostrarCarregamento();

        // Faz a requisição para o backend
        fetch('/verificar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        })
        .then(response => response.json())
        .then(data => {
            // Oculta o carregamento e mostra os resultados
            ocultarCarregamento();
            console.log(data);
            // Atualize a UI com os resultados aqui
        })
        .catch(error => {
            ocultarCarregamento();
            console.error('Erro:', error);
            alert('Erro ao verificar a notícia. Tente novamente mais tarde.');
        });
    });
});