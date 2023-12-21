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
            if (sidebar) { /* Check if sidebar exists */
                sidebar.style.top = "50px"; /* Move the sidebar down */
            }
        } else {
            console.log('Removing sticky class from navbar');
            navbar.classList.remove("sticky");
            if (sidebar) { /* Check if sidebar exists */
                sidebar.style.top = "0"; /* Move the sidebar up */
            }
        }
    }

});function toggleTopics(unit) {
  var topics = unit.getElementsByClassName('topic');
  var topicsVisible = false;
  for (var i = 0; i < topics.length; i++) {
    var display = topics[i].style.display;
    topics[i].style.display = display === 'none' ? 'block' : 'none';
    if (topics[i].style.display !== 'none') {
      topicsVisible = true;
    }
  }
  // Remove 'active' class from all divs
  var allDivs = document.getElementsByClassName('sidebar')[0].getElementsByTagName('div');
  for (var i = 0; i < allDivs.length; i++) {
    allDivs[i].classList.remove('active');
  }
  // Add 'active' class to the clicked div only if its topics are visible
  if (topicsVisible) {
    unit.classList.add('active');
  }
}


