let sl = document.getElementById("animal");
let imgs = document.getElementById("imagens");

function escolha(){
    let selectedOption = sl.selectedOptions[0];
    let imgUrl = selectedOption.value;
  
    let img = document.createElement("img");
    img.setAttribute("src", imgUrl);
    imgs.innerHTML = '';
    imgs.appendChild(img);
}

sl.addEventListener("change", escolha);
escolha();
