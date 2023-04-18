var botao = document.getElementById("botao");

botao.addEventListener("click", function(){
    var paragrafo = document.getElementById("paragrafo");

    paragrafo.textContent = "O texto deste parágrafo foi alterado";
})

function clearcontent(elementID) {
    document.getElementById(elementID).innerHTML = "";
}
