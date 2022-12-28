const navLinks = document.querySelectorAll('nav li a');

navLinks.forEach(link => {
  let href = link.getAttribute('href');
  if (!href.startsWith('http')) {
    href = window.location.origin + href;
  }
  if (href === window.location.href) {
    link.parentElement.classList.add('active');
  }
});

document.getElementById('showAllDogs').addEventListener('click', function (event) {
  event.preventDefault();
  window.location.href = '/dogs';
});

document.getElementById('showAllAdoptions').addEventListener('click', function (event) {
  event.preventDefault();
  window.location.href = '/adoptions';
});

