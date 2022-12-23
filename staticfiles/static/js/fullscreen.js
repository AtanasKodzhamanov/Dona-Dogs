    // Fullscreen API functions
    function openFullscreen(element) {
        if (element.requestFullscreen) {
          element.requestFullscreen();
        } else if (element.mozRequestFullScreen) {
          element.mozRequestFullScreen();
        } else if (element.webkitRequestFullscreen) {
          element.webkitRequestFullscreen();
        } else if (element.msRequestFullscreen) {
          element.msRequestFullscreen();
        }
      }
    
      // Check screen size and apply events
      var mobileQuery = window.matchMedia("(max-width: 767px)");
      if (mobileQuery.matches) {
        // Add onclick event to the image
        var image = document.getElementById("fullscreen");
        image.onclick = function() {
          openFullscreen(this);
        };
      }