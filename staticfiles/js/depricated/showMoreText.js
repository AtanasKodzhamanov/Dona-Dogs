// Get the notice div, notice text, and show more button
const noticeDiv = document.getElementById('noticeDiv');
const noticeText = document.getElementById('noticeText');
const showMoreButton = document.getElementById('showMoreButton');

// Set the maximum height of the notice div
const maxHeight = 250;

// Check if the notice div is taller than the maximum height
if (noticeDiv.offsetHeight > maxHeight) {
  // If it is, show the show more button
  showMoreButton.style.display = 'block';

  // Set the notice div's height to the maximum height
  noticeDiv.style.height = maxHeight + 'px';
  noticeDiv.style.overflow = 'hidden';

  // Add an event listener to the show more button
  showMoreButton.addEventListener('click', () => {
    // When the button is clicked, set the notice div's height to 'auto'
    // and hide the show more button
    noticeDiv.style.height = 'auto';
    showMoreButton.style.display = 'none';
  });

  // Truncate the text to fit within the maximum height
  let truncatedText = noticeText.innerHTML;
  while (noticeDiv.offsetHeight > maxHeight) {
    // Remove the last character from the text
    truncatedText = truncatedText.substring(0, truncatedText.length - 1);
  }
}


