$(document).ready(function(){

  // Manage the display and handling of citations.
  $(".citation-generator").click(function(){
    $("#citation-container").hide(400);
    $("#citation-container").show(400);

    var source = $(this);
    var citation = "U.S.C.";
    citation += source.attr("data-target");
    $("#citation").text( citation );
  });

});
