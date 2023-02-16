// This code is responsible for expanding the adoption cards on the adoptions page.

// Wait for the DOM to load before executing the code
document.addEventListener("DOMContentLoaded", function () {
  // Select all elements with the ID "AdoptionExpand"
  const triggers = document.querySelectorAll("#AdoptionExpand");

  // Loop through each element and add a click event listener
  triggers.forEach((trigger) => {
    trigger.addEventListener("click", function () {
      // Select all elements with the ID "AdoptionCard" that are descendants of the clicked element
      const adoptionCards = this.querySelectorAll("#AdoptionCard");

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
});
