// function toggleFilters() {
//   var filtersContainer = document.getElementById("filtersContainer");
//   if (filtersContainer.classList.contains("hidden")) {
//     filtersContainer.classList.remove("hidden");
//   } else {
//     filtersContainer.classList.add("hidden");
//   }
// }

function findName() {
  // Get the submitted dog name from the form
  var dogName = document.getElementById('dogName').value;
  dogName = dogName.toLowerCase();
  // var showAllButton = document.getElementById('showAllButton');
  // if (dogName != ""){
  //  showAllButton.style.display = '';}
  // else{ showAllButton.style.display = 'None';}

  // Loop through all the dog elements and hide the ones that don't match the submitted dog name
  var dogs = document.querySelectorAll('#dogList #Dog h2');
  for (var i = 0; i < dogs.length; i++) {
    var dog = dogs[i];
    // Convert the dog's name to lowercase
    var dogNameLower = dog.textContent.toLowerCase();
    if (dogNameLower.indexOf(dogName) === -1) {
      dog.parentElement.style.display = 'none';
    } else {
      dog.parentElement.style.display = '';
    }
  }
}
document.getElementById('dogName').addEventListener('input', findName);


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
  // var showAllButton = document.getElementById('showAllButton');
  // showAllButton.style.display = 'None';
}

// Get a reference to the select element and the dog list div
var selectVa = document.querySelector("#adoptionStatus");
var selectGender = document.querySelector("#genderFilter");
var dogList = document.querySelector("#dogList");

// Add event listeners to both select elements that listen for when the user changes the selected option
selectVa.addEventListener("change", filterDogs);
selectGender.addEventListener("change", filterDogs);



function filterDogs() {
  // Get the values of both selected options
  var selectedVa = selectVa.value;
  var selectedGender = selectGender.value;

  // Loop through all of the dogs
  for (var i = 0; i < dogList.children.length; i++) {
    // Get the current dog
    var dog = dogList.children[i];
    //console.log(dog)
    var vaName = dog.getAttribute("vaName");
    if (!vaName){vaName="None"}
    var gender = dog.getAttribute("gender");

    // Check if the dog matches both selected options
    if ((selectedVa == "all" || (selectedVa == "va" && vaName != "None") || (selectedVa == "no" && vaName == "None")) &&
        (selectedGender == "all" || (selectedGender == "male" && gender == "M") || (selectedGender == "female" && gender == "F"))) {
      // If the dog matches both selected options, show the dog
      dog.style.display = "";
    } else {
      // Otherwise, hide the dog
      dog.style.display = "none";
    }
  }
}

