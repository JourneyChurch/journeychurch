$(document).ready(function () {
    $("#nav-icon").click(function() {
        $(".nav-mobile").fadeToggle(300);
        $("body").toggleClass("nav-visible");
    });
});
