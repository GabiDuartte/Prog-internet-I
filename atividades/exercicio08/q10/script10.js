let esc = ["Frutas", "Animais"];
let frutas = ["Maça", "Uva", "Ameixa"];
let animais = ["Cachorro", "gato", "coelho"];

let s1 = document.getElementById("s1");
let s2 = document.getElementById("s2");

esc.forEach(function addEsc(item) {
    let option = document.createElement("option");
    option.text = item;
    option.value = item;
    s1.appendChild(option);
});

s1.onchange = function () {
    s2.innerHTML = "<option></option>";
    if(this.value == "Frutas"){
        addToS2(frutas);
    }
    if(this.value == "Animais"){
        addToS2(animais);
    }
}

function addToS2(arr){
    arr.forEach(function (item){
        let option = document.createElement("option");
        option.text = item;
        option.value = item;
        s2.appendChild(option);
    });
}
