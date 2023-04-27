document.addEventListener('DOMContentLoaded', function () {
    var exibir = document.getElementById('exibir');
    exibir.addEventListener('click', exibirConteudo);
    });

    function soma(){
        var n1 = parseInt(document.getElementById('caixaNum1').value, 10);
        var n2 = parseInt(document.getElementById('caixaNum2').value, 10);
        var resultado = document.getElementById('resultado').innerHTML = "A soma é " + String( n1 + n2); 
    };
