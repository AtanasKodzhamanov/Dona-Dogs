// The code below is responsible for redirecting the user to the dog gallery and adoptions page.

// Select the "Show All Adoptions" button and add an event listener to redirect to the adoptions page
let showAllAdoptionsBtn = document.getElementById("show-all-adoptions-btn");
if (showAllAdoptionsBtn) {
  showAllAdoptionsBtn.addEventListener("click", function (event) {
    event.preventDefault();
    window.location.href = "/adoptions";
  });
}


function getLastMonth() {
  const date = new Date();
  date.setMonth(date.getMonth() - 1);

  const year = date.getFullYear();
  let month = date.toLocaleString('default', { month: 'short' });

  return `${year}-${month}`;
}

let showAllDonationsBtn = document.getElementById("show-all-donations-btn");
if (showAllDonationsBtn) {
  showAllDonationsBtn.addEventListener("click", function (event) {
    event.preventDefault();
    window.location.href = "/donations/history/" + getLastMonth();
  });
}