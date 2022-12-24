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

 // Get the slideshow element
 var slideshow = document.getElementById("slideshow");

 // Get the slides in the slideshow
 var slides = slideshow.getElementsByClassName("slide");

 // Keep track of the current slide index
 var slideIndex = 0;

 // Function to change the slide
 function changeSlide() {
   // Hide all the slides
   for (var i = 0; i < slides.length; i++) {
     slides[i].style.display = "none";
   }

   // Show the current slide
   slides[slideIndex].style.display = "block";

   // Increment the slide index
   slideIndex++;

   // If we've reached the end of the slides, start over
   if (slideIndex >= slides.length) {
     slideIndex = 0;
   }
 }

 // Change the slide every 3 seconds
 setInterval(changeSlide, 3000);