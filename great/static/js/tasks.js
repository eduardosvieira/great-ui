var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event) {
  /*Evento para cliar uma nova tarefa*/
  $("#btnCreateTask").on("click", function(event) {
    var classId = $("#classId").val();
    var title = $("#title").val();
    var description = $("#description").val();
    var deadline = $("#deadline").val();
    var test = $("#test :checked").val();

    $.ajax({
      url: URL + "/classroom/tasks/",
      type: "POST",
      data: {"title": title, "description": description, "deadline": deadline, "classId": classId, "test": test},
      success: function(data) {
        window.location.replace(URL + "/classroom/classes/" + classId);
      },
      error: function(data) {

      }
    });
  });
});
