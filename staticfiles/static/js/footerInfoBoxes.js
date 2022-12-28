
// Footer subscribe form
document.getElementById('footerSubscribeForm').addEventListener('submit', function (event) {
  document.getElementById('footerSubscribeForm').style.display = 'none';
  document.getElementById('success-message').style.display = 'block';
});


// Virtual adoption container
const hideVA = document.querySelector('.hideVA');
const hideSubscribeForm = document.querySelector('.hideSubscribeForm');
const hideDonations = document.querySelector('.hideDonationsBox');

hideVA.style.opacity = 0;
hideSubscribeForm.style.opacity = 0;
hideDonations.style.opacity = 0;

const box1 = document.querySelector('.box1');
box1.addEventListener('mouseover', function () {
  hideVA.style.display = 'block';
  hideSubscribeForm.style.display = 'none';
  hideDonations.style.display = 'none';

  hideSubscribeForm.style.opacity = 0;
  hideDonations.style.opacity = 0;
  setTimeout(function () {
    hideVA.style.opacity = 1;
  }, 100);
});

const box2 = document.querySelector('.box2');
box2.addEventListener('mouseover', function () {
  hideVA.style.display = 'none';
  hideSubscribeForm.style.display = 'block';
  hideDonations.style.display = 'none';

  hideVA.style.opacity = 0;
  hideDonations.style.opacity = 0;

  setTimeout(function () {
    hideSubscribeForm.style.opacity = 1;
  }, 100);

});

const box3 = document.querySelector('.box3');
box3.addEventListener('mouseover', function () {
  hideVA.style.display = 'none';
  hideSubscribeForm.style.display = 'none';
  hideDonations.style.display = 'flex';

  hideVA.style.opacity = 0;
  hideSubscribeForm.style.opacity = 0;

  setTimeout(function () {
    hideDonations.style.opacity = 1;
  }, 100);
});