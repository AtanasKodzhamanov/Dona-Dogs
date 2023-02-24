// This code is responsible for adding filters to the dog gallery page.

function findName() {
  // Get the submitted dog name from the form
  var dogName = document.getElementById("dogName").value;
  dogName = dogName.toLowerCase();
  // Loop through all the dog elements and hide the ones that don't match the submitted dog name
  var dogs = document.querySelectorAll("#dog-list .dog h1");

  for (var i = 0; i < dogs.length; i++) {
    var dog = dogs[i];
    // Convert the dog's name to lowercase
    var dogNameLower = dog.textContent.toLowerCase();
    if (dogNameLower.indexOf(dogName) === -1) {
      dog.parentElement.style.display = "none";
    } else {
      dog.parentElement.style.display = "";
    }
  }
}
document.getElementById("dogName").addEventListener("input", findName);
