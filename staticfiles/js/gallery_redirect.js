// Select the "Show All Dogs" button and add an event listener to redirect to the dog gallery page
let showAllDogsBtn = document.getElementById("showAllDogs");
if (showAllDogsBtn) {
  showAllDogsBtn.addEventListener("click", function (event) {
    event.preventDefault();
    window.location.href = "/dogGallery";
  });
}
