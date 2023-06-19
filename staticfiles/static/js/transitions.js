document.addEventListener("DOMContentLoaded", function () {
    let animatedElements = document.querySelectorAll(".will-animate");

    function animateOnScroll() {
        let windowTop = document.documentElement.scrollTop;
        let windowBottom = windowTop + window.innerHeight;

        animatedElements.forEach(function (element) {
            let elementTop = element.offsetTop;
            let elementBottom = elementTop + element.offsetHeight;

            if (elementTop < windowBottom && elementBottom > windowTop) {
                element.classList.add("animate");
            }
        });
    }
    console.log("transitions.js loaded")
    animateOnScroll();
    window.addEventListener("scroll", animateOnScroll);
});
