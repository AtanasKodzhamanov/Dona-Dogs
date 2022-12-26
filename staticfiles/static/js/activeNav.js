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
const subscribeFormContainer = document.getElementById('subscribeFormContainer');
const hideSubscribeForm = document.querySelector('.hideSubscribeForm');

subscribeFormContainer.addEventListener('mouseover', function() {
  hideSubscribeForm.style.display = 'block';
});
// Footer subscribe form
document.getElementById('footerSubscribeForm').addEventListener('submit', function(event) {
  document.getElementById('footerSubscribeForm').style.display = 'none';
  document.getElementById('success-message').style.display = 'block';
});

// Donation container
const donationsContainer = document.getElementById('donationContainer');
const hideDonations = document.querySelector('.hideDonationsBox');

donationsContainer.addEventListener('mouseover', function() {
  hideDonations.style.display = 'block';
});


// Virtual adoption container
const vaContainer = document.getElementById('vaContainer');
const hideVA = document.querySelector('.hideVA');

vaContainer.addEventListener('mouseover', function() {
  hideVA.style.display = 'block';
});


document.getElementById('showAllDogs').addEventListener('click', function(event) {
  event.preventDefault();
  window.location.href = '/dogs';
});

document.getElementById('showAllAdoptions').addEventListener('click', function(event) {
  event.preventDefault();
  window.location.href = '/adoptions';
});