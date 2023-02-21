// Create a section that displays all past donations with each year having as a parent container that contains months.
// Months would then link to the donation history page for that month.

function createContainer() {
  const container = document.getElementById("pastDonations");
  let year = 2022;
  let month = 10;
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth();
  const currentYear = currentDate.getFullYear();

  while (year < currentYear || (year == currentYear && month < currentMonth)) {
    // create new div container for each year
    const yearContainer = document.createElement("div");
    const monthsContainer = document.createElement("div");
    yearContainer.classList.add("parent");
    yearContainer.classList.add("year-heading");
    yearContainer.classList.add("button-box");
    container.appendChild(yearContainer);
    container.appendChild(monthsContainer);

    const yearHeading = document.createElement("h2");
    yearHeading.innerText = year;
    yearContainer.appendChild(yearHeading);

    // create new grid container for months within each year
    const gridContainer = document.createElement("div");
    gridContainer.classList.add("grid-container");
    gridContainer.style.display = "none";
    monthsContainer.appendChild(gridContainer);

    while (
      (year == currentYear && month < currentMonth) ||
      year < currentYear
    ) {
      const monthName = new Date(year, month, 1).toLocaleString("default", {
        month: "short",
      });
      const monthNameFull = new Date(year, month, 1).toLocaleString("default", {
        month: "long",
      });
      const item = document.createElement("div");
      item.classList.add("grid-item");
      item.classList.add("month-container");
      // add ID to each month

      const link = document.createElement("a");
      link.href = window.location.href + `history/${year}-${monthName}`;
      const h3 = document.createElement("h3");
      // h3.innerText = `${monthNameFull}`;
      // Need to deal with translation of month names
      h3.innerText = `${year} / ${month + 1}`;
      link.appendChild(h3);
      link.classList.add("hyperlink");
      item.appendChild(link);
      gridContainer.appendChild(item);
      month += 1;
      if (month > 11) {
        month = 0;
        year += 1;
        break;
      }
    }
    yearContainer.addEventListener("click", function () {
      if (gridContainer.style.display === "none") {
        gridContainer.style.display = "grid";
      } else {
        gridContainer.style.display = "none";
      }
    });
  }
}

createContainer();
