// Get all card elements on the page
const dogCards = document.querySelectorAll('#Dog');

// Add a click event listener to each card
dogCards.forEach((card) => {
  card.addEventListener('click', () => {
    // Have cursor change to a pointer when hovering over a card
    card.style.cursor = 'pointer';
    // Get the primary key value from the card's "pk" attribute
    const pk = card.getAttribute('pk');
    // Redirect to the /dogs/pk URL

    window.location.href = `/dogs/${pk}`;
  });
});