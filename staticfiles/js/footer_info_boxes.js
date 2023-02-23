// This code is responsible for showing the footer info boxes on the home page when the mouse hovers over them.

// Footer subscribe form
document
  .getElementById("footer-subscribe-form")
  .addEventListener("submit", function (event) {
    document.getElementById("footer-subscribe-form").style.display = "none";
    document.getElementById("success-message").style.display = "block";
  });

// Virtual adoption container
const hideVA = document.querySelector(".hideVA");
const hideSubscribeForm = document.querySelector(".subscribe-form-hide");
const hideDonations = document.querySelector(".hide-donations-box");

hideVA.style.opacity = 0;
hideSubscribeForm.style.opacity = 0;
hideDonations.style.opacity = 0;

const box1 = document.querySelector(".box1");
box1.addEventListener("mouseover", function () {
  hideVA.style.display = "block";
  hideSubscribeForm.style.display = "none";
  hideDonations.style.display = "none";

  hideSubscribeForm.style.opacity = 0;
  hideDonations.style.opacity = 0;
  setTimeout(function () {
    hideVA.style.opacity = 1;
  }, 100);
});

const box2 = document.querySelector(".box2");
box2.addEventListener("mouseover", function () {
  hideVA.style.display = "none";
  hideSubscribeForm.style.display = "block";
  hideDonations.style.display = "none";

  hideVA.style.opacity = 0;
  hideDonations.style.opacity = 0;

  setTimeout(function () {
    hideSubscribeForm.style.opacity = 1;
  }, 100);
});

const box3 = document.querySelector(".box3");
box3.addEventListener("mouseover", function () {
  hideVA.style.display = "none";
  hideSubscribeForm.style.display = "none";
  if (window.innerWidth < 600) {
    hideDonations.style.display = "block";
  } else {
    hideDonations.style.display = "flex";
  }

  hideVA.style.opacity = 0;
  hideSubscribeForm.style.opacity = 0;

  setTimeout(function () {
    hideDonations.style.opacity = 1;
  }, 100);
});
