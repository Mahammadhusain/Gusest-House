var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})



$(document).ready(
  function() {
    setInterval(function() {
    $("#timerefresh").load(" #timerefresh");
  }, 1000); 
 });


