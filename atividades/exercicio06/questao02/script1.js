function tag() {
    var doc = document.getElementsByTagName("P");
    var i;
    for (i = 0; i < doc.length; i++) {
        doc[i].style.backgroundColor = "blue";
        doc[i].style.color = "white";
    }
    }

function mudarCor(novaCor) {
        var elemento = document.getElementById("para1");
        elemento.style.color = novaCor;
    }
