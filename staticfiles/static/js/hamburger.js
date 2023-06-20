let hamburger_toggle = document.querySelector('#menu-toggle');
let sidebar = document.querySelector('#sidebar');
let navContainerMobile = document.querySelector('#reduced-form-nav');

hamburger_toggle.addEventListener('click', function (e) {
    sidebar.classList.toggle('active');
    if (sidebar.classList.contains('active')) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
});
