/*
$(function () {
    $('[data-toggle="popover"]').popover()
})

$("#menu-toggle").click(function (e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});
*/

var toggled = false;
function toggle(){
    console.log("active");
    if (toggled === true){
        console.log("contracting");
        document.getElementById("sidebar-wrapper").style.width = "0";
        document.getElementById("wrapper").style.marginLeft= "0";
        toggled = !toggled;
    }else if (toggled === false){
        console.log("expanding");
        document.getElementById("sidebar-wrapper").style.width = "250px";
        document.getElementById("wrapper").style.marginLeft = "250px";
        toggled = !toggled;
    }
}