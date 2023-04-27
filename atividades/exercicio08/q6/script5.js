let t = document.getElementById("texto1");
let s = document.getElementById("escolha");
let b = document.getElementById("converter");
let r = document.getElementById("resultado");

function converte(texto, opcao){
    if(opcao === 'maiusculo'){
        return texto.toUpperCase();
    } else if(opcao === 'minusculo'){
        return texto.toLowerCase();
    }
}

b.addEventListener('click', () => {
    let texto = t.value;
    let opcao = s.value;
    let b = converte(texto, opcao);
    r.textContent = b;
});
