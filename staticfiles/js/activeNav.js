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


let showAllDogsBtn = document.getElementById('showAllDogs');
if (showAllDogsBtn) {
  showAllDogsBtn.addEventListener('click', function (event) {
    event.preventDefault();
    window.location.href = '/dogGallery';
  });
}

let showAllAdoptionsBtn = document.getElementById('showAllAdoptions');
if (showAllAdoptionsBtn) {
  showAllAdoptionsBtn.addEventListener('click', function (event) {
    event.preventDefault();
    window.location.href = '/adoptions';
  });
}


