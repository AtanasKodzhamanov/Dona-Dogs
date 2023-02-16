// Add virtual adoption and gender filters to the dog gallery page

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
    if (!vaName) {
      vaName = "None";
    }
    var gender = dog.getAttribute("gender");

    // Check if the dog matches both selected options
    if (
      (selectedVa == "all" ||
        (selectedVa == "va" && vaName != "None") ||
        (selectedVa == "no" && vaName == "None")) &&
      (selectedGender == "all" ||
        (selectedGender == "male" && gender == "M") ||
        (selectedGender == "female" && gender == "F"))
    ) {
      // If the dog matches both selected options, show the dog
      dog.style.display = "";
    } else {
      // Otherwise, hide the dog
      dog.style.display = "none";
    }
  }
}
