function check(){
    var c = document.createElement("input");
    c.setAttribute("type", "checkbox");
    c.setAttribute("id", "checar");
    document.body.appendChild(c);
}

function teste(){
    var checar = document.getElementById("checar").checked;
    document.getElementById("id1").innerHTML = checar;
}
