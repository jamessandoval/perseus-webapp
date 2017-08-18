
window.onsvgload = function() {
  $('svg').mouseover(function(){ onEnter(this); });
}

function onEnter(obj) {
  alert($(obj).attr("id"));
}