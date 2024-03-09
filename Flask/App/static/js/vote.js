function openPopup() {
    document.getElementById("votePopup").style.display = "block";
}
function closePopup() {
    document.getElementById("votePopup").style.display = "none";
}

// Récupération du chemin de la page actuelle
var currentPage = window.location.pathname;
// Mise en surbrillance du lien correspondant à la page actuelle
if (currentPage === "/MyElectorSpace") {
    document.getElementById("personalInfo").classList.add("active");
} else if (currentPage === "/elections") {
    document.getElementById("elections").classList.add("active");
}
