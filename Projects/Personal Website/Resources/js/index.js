const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.nav__link');
const checkbox = document.getElementById('checkbox');




navToggle.addEventListener('click', () => {
    // Opens the navigation hamburger
    document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    })
})

checkbox.addEventListener('change', () => {
    //change the theme of the website
    document.body.classList.toggle('dark');


})
