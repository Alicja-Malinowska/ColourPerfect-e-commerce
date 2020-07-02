/**
 * Highlights current tab on the navbar
 * This solution comes from https://stackoverflow.com/questions/34394125/retain-selected-item-in-navbar-after-page-reload
 */
$(document).ready(function () {
    $(".navbar-collapse li a").click(function () {
        
        var id = $(this).attr("id");
        console.log(id)

        $('#' + id).siblings().find(".active").removeClass("active");
        $('#' + id).addClass("active");
        localStorage.setItem("selectedolditem", id);
    });

    var selectedolditem = localStorage.getItem('selectedolditem');

    if (selectedolditem != null) {
        $('#' + selectedolditem).siblings().find(".active").removeClass("active");
        $('#' + selectedolditem).addClass("active");
    }
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
        if (oldValue > 1) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 1;
        }
    }

    $button.parent().find("#quantity").val(newVal);

});

/**
 * Show toast messages
 */
$('.toast').toast('show');