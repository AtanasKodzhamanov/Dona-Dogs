// This script is used to change the language of the website when the language buttons are clicked.

function toggleLanguageButtons() {
  // Get the current language
  var currentLanguage = document.documentElement.lang;
  console.log(currentLanguage);
  // If the current language is Bulgarian, hide the Bulgarian button and show the English button
  if (currentLanguage == "bg") {
    document.getElementById("bg").style.display = "none";
    console.log("test bg");
    document.getElementById("en").style.display = "inline-block";
  }
  // If the current language is English, hide the English button and show the Bulgarian button
  else if (currentLanguage == "en") {
    console.log("test en");
    document.getElementById("en").style.display = "none";
    document.getElementById("bg").style.display = "inline-block";
  }
}

// Call the toggleLanguageButtons function when the page loads to set the initial visibility of the language buttons
toggleLanguageButtons();
