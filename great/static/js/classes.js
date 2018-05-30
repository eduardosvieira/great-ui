var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $(".modal").modal();

  $("#btnUpdateClass").on("click", function(event) {
    var classId = $("#classId").val();
    var name = $("#name").val();
    var description = $("#description").val();

    $.ajax({
      url: URL + "/classroom/classes/" + classId + "/",
      type: "PUT",
      data: {"name": name, "description": description},
      success: function(data) {
        window.location.replace("/classroom/classes/" + classId + "/");
      },
      error: function(data) {

      }
    });
  });

  $("#btnDeleteClass").on("click", function(event) {
    var classId = $("#classId").val();

    $.ajax({
      url: URL + "/classroom/classes/" + classId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace("/classroom/");
      },
      error: function(data) {

      }
    });
  });

});
