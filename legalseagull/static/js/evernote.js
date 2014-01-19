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

    var noteStoreURL = "https://sandbox.evernote.com/michel585/shard/s1/notestore";
    var authenticationToken = "S=s1:U=8dbad:E=14afebcbfc4:C=143a70b93c7:P=1cd:A=en-devtoken:V=2:H=3d264cfb27f8fe7deb504b6e05229d5d";

    var noteStoreTransport = new Thrift.BinaryHttpTransport(noteStoreURL);
    var noteStoreProtocol = new Thrift.BinaryProtocol(noteStoreTransport);
    var noteStore = new NoteStoreClient(noteStoreProtocol);

    noteStore.listNotebooks(
      authenticationToken,
      function (notebooks) {
        console.log("success");
        console.log(notebooks);
      },
      function onerror(error) { 
        console.log("failure");
        console.log(error);
      }
    );

    var timestamp = $.now();
    var new_note = new Note();
    new_note.title = "LegalSeagull annotation " + timestamp;
    new_note.content = annotation;

    noteStore.createNote(
      authenticationToken,
      new_note,
      function( note ) {
        console.log(note);
      },
      function onerror(error) {
        console.log(error);
      }
    );



    // clear the textarea
    $("#evernote-textarea").val('');
    // alert success
    alert("Success!");
  });


});

