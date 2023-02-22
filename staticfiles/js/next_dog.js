function goToNextDog(isNext) {
  const url = window.location.pathname;
  const urlParts = url.split("/");
  const currentDogId = urlParts[urlParts.length - 2];

  const currentIndex = activeDogIds.indexOf(parseInt(currentDogId));
  let nextIndex = isNext ? currentIndex + 1 : currentIndex - 1; // calculate the index of the next or previous dog
  if (nextIndex < 0) {
    nextIndex = activeDogIds.length - 1; // go to the last dog if we're at the first one
  } else if (nextIndex >= activeDogIds.length) {
    nextIndex = 0; // go back to the first dog if we're at the last one
  }

  const nextDogId = activeDogIds[nextIndex];
  const nextUrl = `/dogGallery/${nextDogId}/`;

  return nextUrl;
}

const nextDogButton = document.getElementById("next-dog-button");
const prevDogButton = document.getElementById("prev-dog-button");

nextDogButton.addEventListener("click", function () {
  window.location.href = goToNextDog(true);
});

prevDogButton.addEventListener("click", function () {
  window.location.href = goToNextDog(false);
});
