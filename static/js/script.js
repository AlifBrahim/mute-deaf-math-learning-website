document.addEventListener("DOMContentLoaded", function() {
    window.onscroll = function() {myFunction()};

    var navbar = document.getElementById("navbar");

    var sticky = navbar.offsetTop;

    function myFunction() {
      if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        document.querySelector('.sidebar').style.marginTop = "60px"; /* Move the sidebar down */
      } else {
        navbar.classList.remove("sticky");
        document.querySelector('.sidebar').style.marginTop = "0"; /* Move the sidebar up */
      }
    }
});
