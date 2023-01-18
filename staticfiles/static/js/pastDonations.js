function createContainer() {
  const container = document.getElementById("pastDonations");
  let year = 2015;
  let month = 10;
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth();
  const currentYear = currentDate.getFullYear();
  while (year < currentYear || (year == currentYear && month < currentMonth)) {
    //create new div container for each year
    const yearContainer = document.createElement("div");
    yearContainer.classList.add("parent");
    yearContainer.classList.add("year-heading");
    container.appendChild(yearContainer);

    const yearHeading = document.createElement("h2");
    yearHeading.innerText = year;
    yearContainer.appendChild(yearHeading);

    //create new grid container for months within each year
    const gridContainer = document.createElement("div");
    gridContainer.classList.add("grid-container");
    gridContainer.style.display = "none";
    yearContainer.appendChild(gridContainer);

    while (
      (year == currentYear && month <= currentMonth) ||
      year < currentYear
    ) {
      const monthName = new Date(year, month, 1).toLocaleString("default", {
        month: "short",
      });
      const item = document.createElement("div");
      item.classList.add("grid-item");
      // add ID to each month

      const link = document.createElement("a");
      link.href = window.location.href + `history/${year}-${monthName}`;
      link.innerText = `${monthName} ${year}`;
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
    yearHeading.addEventListener("click", function () {
      if (gridContainer.style.display === "none") {
        gridContainer.style.display = "grid";
      } else {
        gridContainer.style.display = "none";
      }
    });
  }
}

createContainer();
