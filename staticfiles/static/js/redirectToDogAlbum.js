const dogCards = document.querySelectorAll('#Dog')

dogCards.forEach((card) => {
  card.addEventListener('click', () => {
    card.style.cursor = 'pointer'
    const pk = card.getAttribute('pk')
    window.location.href = `/dogGallery/${pk}`
  })
})