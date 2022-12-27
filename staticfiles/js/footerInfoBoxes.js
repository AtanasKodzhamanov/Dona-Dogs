
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

const box1 = document.querySelector('.box1');
box1.addEventListener('mouseover', function() {
  hideVA.style.display = 'block';
  hideSubscribeForm.style.display = 'none';
  hideDonations.style.display = 'none';
});

const box2 = document.querySelector('.box2');
box2.addEventListener('mouseover', function() {
  hideVA.style.display = 'none';
  hideSubscribeForm.style.display = 'block';
  hideDonations.style.display = 'none';
});

const box3 = document.querySelector('.box3');
box3.addEventListener('mouseover', function() {
  hideVA.style.display = 'none';
  hideSubscribeForm.style.display = 'none';
  hideDonations.style.display = 'block';
});