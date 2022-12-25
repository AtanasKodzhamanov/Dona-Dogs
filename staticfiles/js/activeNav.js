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



// Footer subscribe form
document.getElementById('footerSubscribeForm').addEventListener('submit', function(event) {
  document.getElementById('footerSubscribeForm').style.display = 'none';
  document.getElementById('success-message').style.display = 'block';
});


