let slideIndex = 1;
let manualControl = false; // Flag to track whether slides are being manually controlled

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
  manualControl = true; // Set flag to true when dot is clicked
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("slides-donations");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" activeslide", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " activeslide";
}

let dotsContainer = document.getElementById("dots-container");

// Create a dot for each slide
let slides = document.getElementsByClassName("slides-donations");
console.log(slides)

for (let i = 0; i < slides.length; i++) {
  console.log("print dot")
  let dot = document.createElement("span");
  dot.className = "dot";
  dot.onclick = function () { currentSlide(i + 1) };
  dotsContainer.appendChild(dot);

}

// Initialize the slide show
showSlides(slideIndex);

let intervalId; // Declare a variable to store the interval ID

// Set timeout to start interval after 2 seconds
setTimeout(function() {
    // Set interval to call showSlides function every 5 seconds
    intervalId = setInterval(function() {
      if (!manualControl) { // Only change slides if manualControl flag is false
        showSlides(slideIndex += 1);
      }
    }, 7000);
  }, 2000);
