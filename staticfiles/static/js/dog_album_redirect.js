// Redirects to the dog album page when the dog card is clicked

const dogCards = document.querySelectorAll(".dog");

dogCards.forEach((card) => {
  card.addEventListener("click", () => {
    card.style.cursor = "pointer";
    const pk = card.getAttribute("pk");
    window.location.href = `/dogGallery/${pk}`;
  });
});
