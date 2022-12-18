function setActiveNavItem(item) {
    // Get all nav items
    const navItems = document.querySelectorAll('li.w3-bar-item');
    
    // Remove the 'w3-bottombar' class from all nav items
    navItems.forEach(navItem => navItem.classList.remove('w3-bottombar'));
    
    // Add the 'w3-bottombar' class to the clicked nav item
    item.classList.add('w3-bottombar');
  }
  
  const navItems = document.querySelectorAll('li.w3-bar-item');
  navItems.forEach(navItem => navItem.addEventListener('click', () => setActiveNavItem(navItem)));
  

// Footer subscribe form
  document.getElementById('footerSubscribeForm').addEventListener('submit', function(event) {
    document.getElementById('footerSubscribeForm').style.display = 'none';
    document.getElementById('success-message').style.display = 'block';
  });

