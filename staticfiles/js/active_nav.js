// Add the "active" class to the navigation bar link that matches the current page URL so that the user knows which page they are on.

// Select all links within the navigation bar
const navLinks = document.querySelectorAll("nav li a");

// Loop through each link to check its URL
navLinks.forEach((link) => {
  let href = link.getAttribute("href");

  if (!href.startsWith("http")) {
    href = window.location.origin + href;
  }

  // If the link URL matches the current page URL, add the "active" class to the parent element of the link
  if (href === window.location.href) {
    link.parentElement.classList.add("active");
  }
});
