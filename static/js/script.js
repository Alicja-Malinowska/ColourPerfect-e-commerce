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


/**
 * Allows increment and decrement product amount in range 0-99
 */
$(".quantity-button").on("click", function () {

    var $button = $(this);
    var oldValue = $button.parent().find("#quantity").val();

    if ($button.text() == "+") {
        if (oldValue < 99) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            newVal = 99;
        }

    } else {
        if (oldValue > 0) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }

    $button.parent().find("#quantity").val(newVal);

});