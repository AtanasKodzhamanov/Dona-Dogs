// Create a section that displays all past donations with each year having as a parent container that contains months.
// Months would then link to the donation history page for that month.

function createContainer() {
  const container = document.getElementById("past-donations");
  let year = 2022;
  let month = 10;
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth();
  const currentYear = currentDate.getFullYear();

  // this is to get the translated month names
  const monthNames = [
    gettext("January"),
    gettext("February"),
    gettext("March"),
    gettext("April"),
    gettext("May"),
    gettext("June"),
    gettext("July"),
    gettext("August"),
    gettext("September"),
    gettext("October"),
    gettext("November"),
    gettext("December"),
  ];

  const monthNamez = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  // long to short month names
  const monthDict = {
    January: "Jan",
    February: "Feb",
    March: "Mar",
    April: "Apr",
    May: "May",
    June: "Jun",
    July: "Jul",
    August: "Aug",
    September: "Sep",
    October: "Oct",
    November: "Nov",
    December: "Dec",
  };

  while (year < currentYear || (year == currentYear && month < currentMonth)) {
    // create new div container for each year
    const yearContainer = document.createElement("div");
    const monthsContainer = document.createElement("div");
    yearContainer.classList.add("parent");
    yearContainer.classList.add("year-heading");
    yearContainer.classList.add("button");
    const firstChild = container.firstChild;
    container.insertBefore(yearContainer, firstChild);
    container.insertBefore(monthsContainer, firstChild);

    const yearHeading = document.createElement("h3");
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

      let monthName = monthDict[monthNamez[month]];
      let monthNameFull = monthNames[month];
      const item = document.createElement("div");
      item.classList.add("grid-item");
      item.classList.add("month-container");
      // add ID to each month

      const link = document.createElement("a");
      link.href = window.location.href + `history/${year}-${monthName}`;
      const h3 = document.createElement("h3");
      h3.innerText = `${monthNameFull}`;

      link.appendChild(h3);
      link.classList.add("hyperlink");
      item.appendChild(link);
      gridContainer.appendChild(item);

      item.addEventListener("click", function () {
        window.location.href = link.href;
      });

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
