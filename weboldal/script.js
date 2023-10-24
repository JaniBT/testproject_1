var gombVissza = document.getElementById("gomb-vissza");

// Jelenítsük meg a gombot, ha az oldal lefelé görgetett
window.onscroll = function() {
    if (document.documentElement.scrollTop > 100) {
        gombVissza.style.display = "block";
    } else {
        gombVissza.style.display = "none";
    }
};

// Ugrás a tetejére, amikor a gombra kattintanak
gombVissza.onclick = function() {
    document.documentElement.scrollTop = 0; // Az oldal tetejére ugrás
};
