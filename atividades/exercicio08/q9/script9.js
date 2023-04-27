let botao = document.getElementById("remove");
let sl = document.getElementById("frutas");

botao.addEventListener("click", () => {
    let selectedOption = sl.selectedOptions[0];
    sl.removeChild(selectedOption);
});
