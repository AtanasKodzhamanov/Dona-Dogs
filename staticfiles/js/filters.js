

function filterDogs() {
  // Get the submitted dog name from the form
  var dogName = document.getElementById('dogName').value;
  var showAllButton = document.getElementById('showAllButton');
  if (dogName != ""){
    showAllButton.style.display = '';}
  else{ showAllButton.style.display = 'None';}

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

  // Hide the "Show all" button since all dogs are now visible
  var showAllButton = document.getElementById('showAllButton');
  showAllButton.style.display = 'None';
}

// Get a reference to the select element and the dog list div
// Get a reference to the select element and the dog list div
var select = document.querySelector("#adoptionStatus");
console.log(select)
var dogList = document.querySelector("#dogList");
console.log(select)
  // Add an event listener to the select element that listens for when the user changes the selected option
  select.addEventListener("change", function() {
  // Get the value of the selected option
  var selectedOption = this.value;
  // Loop through all of the dogs
  for (var i = 0; i < dogList.children.length; i++) {
    // Get the current dog
    var dog = dogList.children[i];
    //console.log(dog)
    var vaName = dog.getAttribute("vaName");
    if (!vaName){vaName="None"}

    console.log(dog)
    
    // Check if the dog's adoption status matches the selected option
    if (selectedOption == "all") {
      // If the dog's adoption status matches the selected option, show the dog
      dog.style.display = "";
    } else if (selectedOption == "va" && vaName != "None") {
      // If the selected option is "va" and the dog has a vaName value, show the dog
      dog.style.display = "";
    } else if (selectedOption == "no" && vaName == "None") {
      // If the selected option is "no" and the dog does not have a vaName value, show the dog
      dog.style.display = "";
    } else {
      // Otherwise, hide the dog
      dog.style.display = "none";
    }
  }
  });

