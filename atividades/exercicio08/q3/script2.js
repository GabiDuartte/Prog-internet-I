function criaImagem(){
    const div = document.getElementById("imagens");
    
    const image = document.createElement("img");
    image.src = "img/OIP.png";
    
    div.appendChild(image);
}
