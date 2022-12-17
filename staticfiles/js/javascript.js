function myFunction1(element) {
  var popup = element.querySelector('#myPopup');
  popup.classList.toggle("show", true);

}

function myFunction2(element) {
  var popup = element.querySelector('#myPopup');
  popup.classList.toggle("show", false);

}

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
}


function filterDogs() {
  // Get the submitted dog name from the form
  var dogName = document.getElementById('dogName').value;

  // Loop through all the dog elements and hide the ones that don't match the submitted dog name
  var dogs = document.querySelectorAll('#dogList #Dog h2');
  for (var i = 0; i < dogs.length; i++) {
    var dog = dogs[i];
    if (dog.textContent.indexOf(dogName) === -1) {
      dog.parentElement.style.display = 'none';
    } else {
      dog.parentElement.style.display = '';
    }
  }
}

function showAllDogs() {
  // Reset the form by clearing the dog name input field
  document.getElementById('dogName').value = '';

  // Loop through all the dog elements and remove the `display: none` style
  var dogs = document.querySelectorAll('#dogList #Dog h2');
  for (var i = 0; i < dogs.length; i++) {
    var dog = dogs[i];
    dog.parentElement.style.display = '';
  }
}
