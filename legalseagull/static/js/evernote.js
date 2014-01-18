$(document).ready(function(){

  // Evernote-tab expander.
  $(".evernote-expander").click(function(){
    $("#evernote-tab").toggle(400);
  });

  // Evernote submitter.
  $("#evernote-submit").click(function(){
    // grab contents of the textarea
    var annotation = $("#evernote-textarea").val();
    console.log( annotation );

    var client = new Evernote.Client({token: 'S=s1:U=8dbad:E=14afebcbfc4:C=143a70b93c7:P=1cd:A=en-devtoken:V=2:H=3d264cfb27f8fe7deb504b6e05229d5d'});
    var noteStore = client.getNoteStore();
    notebooks = noteStore.listNotebooks(function(err, notebooks){
      console.log( notebooks );
    });

    // clear the textarea
    $("#evernote-textarea").val('');
    // alert success
    alert("Success!");
  });


});

