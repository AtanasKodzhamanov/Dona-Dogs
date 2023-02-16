// Implement the donations slide show on the front page

// Initialize the slide index to 1 and set flag to false to track manual slide control
let slideIndex = 1;
let manualControl = false;

// Function to show a specific slide when a thumbnail is clicked
function currentSlide(n) {
  showSlides((slideIndex = n));
  manualControl = true; // Set flag to true when dot is clicked
}

// Function to show the current slide and hide all others
function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("slides-donations");
  let dots = document.getElementsByClassName("dot");

  // If the index is out of range, set it to the first or last slide
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }

  // Hide all slides and remove the "active" class from all dots
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" activeslide", "");
  }

  // Show the current slide and add the "active" class to the corresponding dot
  slides[slideIndex - 1].style = "display: flex; justify-content: center;";
  dots[slideIndex - 1].className += " activeslide";
}

// Select the dots container and create a dot for each slide
let dotsContainer = document.getElementById("dots-container");
let slides = document.getElementsByClassName("slides-donations");

for (let i = 0; i < slides.length; i++) {
  if (slides.length > 1) {
    let dot = document.createElement("span");
    dot.className = "dot";
    dot.onclick = function () {
      currentSlide(i + 1);
    };
    dotsContainer.appendChild(dot);
  }
}

// Initialize the slide show
showSlides(slideIndex);

let intervalId; // Declare a variable to store the interval ID

// Set timeout to start interval after 2 seconds
setTimeout(function () {
  // Set interval to call showSlides function every 7 seconds
  intervalId = setInterval(function () {
    if (!manualControl) {
      // Only change slides if manualControl flag is false
      showSlides((slideIndex += 1));
    }
  }, 7000);
}, 2000);
