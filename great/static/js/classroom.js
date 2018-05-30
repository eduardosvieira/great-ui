var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $(".modal").modal();

  $("#btnCreateClass").on("click", function(event) {
    var name = $("#name").val();
    var description = $("#description").val();

    $.ajax({
      url: URL + "/classroom/classes/",
      type: "POST",
      data: {"name": name, "description": description, "createdAt": Date()},
      success: function(data) {
        window.location.replace("/classroom/");
      },
      error: function(data) {

      }
    });
  });

});
