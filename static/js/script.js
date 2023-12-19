document.addEventListener("DOMContentLoaded", function() {
    console.log('DOM fully loaded and parsed');
    window.onscroll = function() {myFunction()};

    var navbar = document.getElementById("navbar");
    console.log('navbar:', navbar);

    var sidebar = document.querySelector('.sidebar');
    console.log('sidebar:', sidebar);

    var sticky = navbar.offsetTop;

    function myFunction() {
        console.log('onscroll event fired');
        if (window.pageYOffset >= sticky) {
            console.log('Adding sticky class to navbar');
            navbar.classList.add("sticky");
            sidebar.style.top = "50px"; /* Move the sidebar down */
        } else {
            console.log('Removing sticky class from navbar');
            navbar.classList.remove("sticky");
            sidebar.style.top = "0"; /* Move the sidebar up */
        }
    }
});
