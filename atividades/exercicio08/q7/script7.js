let t = document.getElementById("t1");
let b = document.getElementById("mudar");
let s = document.getElementById("selecionar");


b.addEventListener('click', () => {
    let option = document.createElement("option");
    option.value = t.value;
    option.text = t.value;
    s.appendChild(option);
})
