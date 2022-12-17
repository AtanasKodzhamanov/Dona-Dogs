

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
var selectVa = document.querySelector("#adoptionStatus");
var dogList = document.querySelector("#dogList");
  // Add an event listener to the select element that listens for when the user changes the selected option
  selectVa.addEventListener("change", function() {
  // Get the value of the selected option
  var selectedVa = this.value;
  // Loop through all of the dogs
  for (var i = 0; i < dogList.children.length; i++) {
    // Get the current dog
    var dog = dogList.children[i];
    //console.log(dog)
    var vaName = dog.getAttribute("vaName");
    if (!vaName){vaName="None"}

    console.log(dog)
    
    // Check if the dog's adoption status matches the selected option
    if (selectedVa == "all") {
      // If the dog's adoption status matches the selected option, show the dog
      dog.style.display = "";
    } else if (selectedVa == "va" && vaName != "None") {
      // If the selected option is "va" and the dog has a vaName value, show the dog
      dog.style.display = "";
    } else if (selectedVa == "no" && vaName == "None") {
      // If the selected option is "no" and the dog does not have a vaName value, show the dog
      dog.style.display = "";
    } else {
      // Otherwise, hide the dog
      dog.style.display = "none";
    }
  }
  });

  // Get a reference to the select element and the dog list div
  var selectGender = document.querySelector("#genderFilter");
  var dogList = document.querySelector("#dogList");
  // Add an event listener to the select element that listens for when the user changes the selected option
  selectGender.addEventListener("change", function() {
  // Get the value of the selected option
  var selectedGender = this.value;
  // Loop through all of the dogs
  for (var i = 0; i < dogList.children.length; i++) {
    // Get the current dog
    var dog = dogList.children[i];
    //console.log(dog)
    var gender = dog.getAttribute("gender");

    console.log(dog)
    
    // Check if the dog's adoption status matches the selected option
    if (selectedGender == "all") {
      // If the dog's adoption status matches the selected option, show the dog
      dog.style.display = "";
    } else if (selectedGender == "male" && gender == "M") {
      // If the selected option is "va" and the dog has a vaName value, show the dog
      dog.style.display = "";
    } else if (selectedGender == "female" && gender == "F") {
      // If the selected option is "no" and the dog does not have a vaName value, show the dog
      dog.style.display = "";
    } else {
      // Otherwise, hide the dog
      dog.style.display = "none";
    }
  }
  });
