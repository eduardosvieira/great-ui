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
    var testId = $("#test :checked").val();

    $.ajax({
      url: URL + "/classroom/tasks/",
      type: "POST",
      data: {"title": title, "description": description, "createdAt": Date(), "deadline": deadline, "classId": classId, "testId": testId},
      success: function(data) {
        window.location.replace(URL + "/classroom/");
      },
      error: function(data) {

      }
    });
  });
});
