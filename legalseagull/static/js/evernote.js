$(document).ready(function(){

  // Evernote-tab expander.
  $(".evernote-expander").click(function(){
    $("#evernote-tab").toggle(400);
  });

  // Evernote triggers (always show, don't toggle).
  $(".evernote-trigger").click(function(){
    $("#evernote-tab").show(400);
  });


  // Evernote submitter.
  $("#evernote-submit").click(function(){

    // grab contents of the textarea
    var content = $("#evernote-textarea").val();
    var title = $("#evernote-title").val()

    // post the data to the LegalSeagull API
    $.post(
      "/api/evernote/create-note/",
      {
        title: title,
        content: content,
      }
    ).done(
      function( data ) {
        if( data.hasOwnProperty('result') ){
          if( data['result'] == 'success' ){
            // clear the textarea, but not the title
            $("#evernote-textarea").val('');
            // alert success
            alert("Success!");
          }
        }
      }
    );

  });

});
