// Select all elements with the ID "adoption-expand-button"
const triggers = document.querySelectorAll("#adoption-expand-button");

// Loop through each element and add a click event listener
triggers.forEach((trigger) => {
  trigger.addEventListener("click", function () {
    // Select all elements with the ID "AdoptionCard" that are descendants of the parent element
    const adoptionCards = this.parentNode.querySelectorAll("#AdoptionCard");

    // Loop through each element and toggle its display style between "block" and "none"
    adoptionCards.forEach((adoptionCard) => {
      if (adoptionCard.style.display === "none") {
        adoptionCard.style.display = "block";
      } else {
        adoptionCard.style.display = "none";
      }
    });
  });
});
