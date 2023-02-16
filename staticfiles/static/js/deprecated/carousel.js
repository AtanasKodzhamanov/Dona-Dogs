// This code implements a slide show on the home page.

// Set the initial slide index to 1 and show the first slide
let slideIndex = 1;
showSlides(slideIndex);

// Increase or decrease the slide index by n and show the corresponding slide
function plusSlides(n) {
  showSlides((slideIndex += n));
}

// Set the slide index to n and show the corresponding slide
function currentSlide(n) {
  showSlides((slideIndex = n));
}

// Show the slide with the index n
function showSlides(n) {
  // Get all elements with the class "mySlides"
  let slides = document.getElementsByClassName("mySlides");

  // If n is greater than the number of slides, set the slide index to 1
  if (n > slides.length) {
    slideIndex = 1;
  }

  // If n is less than 1, set the slide index to the last slide
  if (n < 1) {
    slideIndex = slides.length;
  }

  // Hide all slides
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  // Show the slide with the index slideIndex - 1 (because arrays are 0-indexed)
  slides[slideIndex - 1].style.display = "block";
}
