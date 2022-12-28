document.addEventListener("DOMContentLoaded", function () {
    const triggers = document.querySelectorAll('#AdoptionExpand');
    triggers.forEach(trigger => {
        trigger.addEventListener('click', function () {
            const adoptionCards = this.querySelectorAll('#AdoptionCard');
            adoptionCards.forEach(adoptionCard => {
                if (adoptionCard.style.display === 'none') {
                    adoptionCard.style.display = 'block';
                } else {
                    adoptionCard.style.display = 'none';
                }
            });
        });
    });
});


