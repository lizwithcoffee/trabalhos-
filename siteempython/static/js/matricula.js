// Seleção dos elementos da página
var $tdTotalCursos = document.querySelector('.js-total-de-cursos');
var $tdTotalDeHoras = document.querySelector('.js-total-de-horas');
var $buttonConfirmar = document.querySelector('.js-botao-matricula');

// Variáveis de controle para o total de horas e total de cursos
var totalHoras = 0;
var totalCursos = 0;

// Função chamada ao selecionar ou desmarcar um curso
function adicionaCurso(checkbox) {
    // Verifica se o checkbox foi marcado ou desmarcado
    if (checkbox.checked) {
        totalCursos++;  // Aumenta o contador de cursos
        totalHoras += parseInt(checkbox.value);  // Adiciona as horas do curso
    } else {
        totalCursos--;  // Diminui o contador de cursos
        totalHoras -= parseInt(checkbox.value);  // Subtrai as horas do curso
    }

    // Atualiza os textos no DOM com os novos totais
    $tdTotalDeHoras.textContent = totalHoras + 'h';
    $tdTotalCursos.textContent = totalCursos + ' curso(s)';
}

// Atribui a função de confirmação para o botão de matrícula
$buttonConfirmar.onclick = confirmaMatriculas;

// Função chamada ao clicar no botão de confirmação de matrícula
function confirmaMatriculas() {
    // Verifica se nenhum curso foi selecionado
    if (totalCursos === 0) {
        alert('Nenhum curso selecionado');
    } else {
        alert('Matrícula confirmada nos cursos!');
        window.location.href = 'index.html';  // Redireciona para a página principal
    }
}