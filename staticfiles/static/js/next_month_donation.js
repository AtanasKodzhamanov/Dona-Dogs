function goToNextMonth() {
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
  if (monthIndex === -1) {
    console.error("Invalid month name:", monthName);
    return;
  }
  const nextDate = new Date(year, monthIndex, 1);
  nextDate.setMonth(nextDate.getMonth() + 1);
  const formattedMonthName = monthNames[nextDate.getMonth()];
  const formattedDate = nextDate.getFullYear() + "-" + formattedMonthName;
  const nextUrl = window.location.href.replace(thisDate, formattedDate);
  window.location.href = nextUrl;
}

const nextMonthButton = document.getElementById("next-month-button"); // get the button element
nextMonthButton.addEventListener("click", goToNextMonth); // attach the event listener to the button

function goToPrevMonth() {
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
  if (monthIndex === -1) {
    console.error("Invalid month name:", monthName);
    return;
  }
  const nextDate = new Date(year, monthIndex, 1);
  nextDate.setMonth(nextDate.getMonth() - 1);
  const formattedMonthName = monthNames[nextDate.getMonth()];
  const formattedDate = nextDate.getFullYear() + "-" + formattedMonthName;
  const nextUrl = window.location.href.replace(thisDate, formattedDate);
  window.location.href = nextUrl;
}

const prevMonthButton = document.getElementById("prev-month-button"); // get the button element
prevMonthButton.addEventListener("click", goToPrevMonth); // attach the event listener to the button
