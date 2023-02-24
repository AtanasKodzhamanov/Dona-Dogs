//to clean up

function goToMonth(delta) {
  const url = window.location.pathname;
  const urlParts = url.split("/");
  const thisDate = urlParts[urlParts.length - 2];
  const [year, monthName] = thisDate.split("-");
  const monthNames = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const monthIndex = monthNames.indexOf(monthName);
  const nextDate = new Date(year, monthIndex, 1);
  nextDate.setMonth(nextDate.getMonth() + delta);

  const formattedMonthName = monthNames[nextDate.getMonth()];
  const formattedDate = nextDate.getFullYear() + "-" + formattedMonthName;
  const nextUrl = window.location.href.replace(thisDate, formattedDate);
  window.location.href = nextUrl;
}

function hideButtons() {
  const url = window.location.pathname;
  const urlParts = url.split("/");
  const thisDate = urlParts[urlParts.length - 2];
  const [year, monthName] = thisDate.split("-");
  const monthNames = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const monthIndex = monthNames.indexOf(monthName);
  const nextDate = new Date(year, monthIndex, 1);
  nextDate.setMonth(nextDate.getMonth() + 1);

  if (
    new Date().getFullYear() === nextDate.getFullYear() &&
    new Date().getMonth() === nextDate.getMonth()
  ) {
    const nextMonthButton = document.getElementById("next-month-button");
    nextMonthButton.style.display = "none";
  }

  if (year === "2022" && monthName === "Nov") {
    const prevMonthButton = document.getElementById("prev-month-button");
    prevMonthButton.style.display = "none";
  }
}

hideButtons();

const nextMonthButton = document.getElementById("next-month-button");
nextMonthButton.addEventListener("click", () => goToMonth(1));

const prevMonthButton = document.getElementById("prev-month-button");
prevMonthButton.addEventListener("click", () => goToMonth(-1));
