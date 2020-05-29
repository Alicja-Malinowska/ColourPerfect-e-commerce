/**
 * Highlights current tab on the navbar
 */
$(document).ready(function () {
    $(".nav-item").click(function () {
        console.log('dupa');
        $(this).addClass("active");
        $(".nav-item").not(this).removeClass("active");
    });

});

