// function openPopup() {
//     document.getElementById("votePopup").style.display = "block";
// }
// function closePopup() {
//     document.getElementById("votePopup").style.display = "none";
// }
let isTextVisible = true;
let initialText = toggleVisibility();
function toggleVisibility() {
    const pkElement = document.getElementById('private-key');
    const pkText = pkElement.innerText;
    console.log(pkText);
    const asterisks = '*'.repeat(pkText.length);
    pkElement.innerText = isTextVisible ? asterisks : pkText;
    isTextVisible = !isTextVisible;
    if (pkText != asterisks)
        return pkText;
}


function copyToClipboard(text) {
    const el = document.createElement('textarea');
    el.value = text;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    alert('Private key copied to clipboard');
}

// Récupération du chemin de la page actuelle
var currentPage = window.location.pathname;
// Mise en surbrillance du lien correspondant à la page actuelle
if (currentPage === "/MyElectorSpace") {
    document.getElementById("personalInfo").classList.add("active");
} else if (currentPage === "/elections") {
    document.getElementById("elections").classList.add("active");
}








function toggleInfo(id) {
    var info = document.getElementById(id);
    if (info) {
        if (info.style.display === "block") {
            info.style.display = "none";
        } else {
            info.style.display = "block";
        }
    }
}

// Ouvrir le popup
function openPopup() {
    var popup = document.getElementById("votingPopup");
    if (popup) {
        popup.style.display = "block";
    }
}

// Fermer le popup
function closePopup() {
    var popup = document.getElementById("votingPopup");
    if (popup) {
        popup.style.display = "none";
    }
}
function closePopup() {
    document.getElementById("votingPopup").style.display = "none";
}


function copyToClipboard(text) {

}









