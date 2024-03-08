function openPopup() {
    document.getElementById("votePopup").style.display = "block";
}
function closePopup() {
    document.getElementById("votePopup").style.display = "none";
}

// Récupération du chemin de la page actuelle
var currentPage = window.location.pathname;
// Mise en surbrillance du lien correspondant à la page actuelle
if (currentPage === "/html/elector.html") {
    document.getElementById("personalInfo").classList.add("active");
} else if (currentPage === "/html/elections.html") {
    document.getElementById("elections").classList.add("active");
}
