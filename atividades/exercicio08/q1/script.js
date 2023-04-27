document.addEventListener('DOMContentLoaded', function () {
    var botaoExibir = document.getElementById('botaoExibir');
    botaoExibir.addEventListener('click', exibirConteudo);
    });
    function exibirConteudo() {
    var conteudo = document.getElementById('caixaDeTexto').value;
    document.getElementById('conteudo').innerHTML = conteudo;

    if(!document.getElementById('caixaDeTexto').value){
        alert("Informe um texto");
        return false;
    }
    }
