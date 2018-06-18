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
        window.location.replace(URL + "/classroom/classes/" + classId + "/");
      },
      error: function(data) {

      }
    });
  });


  $(".btnDeleteTask").on("click", function(event) {
    var classId = $("#classId").val();
    var taskId = $(this).parent().siblings(".taskId").text();

    $.ajax({
      url: URL + "/classroom/tasks/" + taskId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/classroom/classes/" + classId + "/");
      },
      error: function(data) {

      }
    });
  });


  $(".callModalEditTask").on("click", function(event) {
    var taskId = $(this).parent().siblings(".taskId").text();

    $("#modal-edit-task-id").attr("value", taskId);
  });

  $("#btnEditTask").on("click", function(event) {
    var classId = $("#classId").val();
    var taskId = $("#modal-edit-task-id").val();
    var title = $("#modal-edit-task-title").val();
    var description = $("#modal-edit-task-description").val();
    var deadline = $("#modal-edit-task-deadline").val();

    $.ajax({
      url: URL + "/classroom/tasks/" + taskId + "/",
      type: "PUT",
      data: {"title": title, "description": description, "deadline": deadline},
      success: function(data) {
        window.location.replace(URL + "/classroom/classes/" + classId + "/");
      }
    });
  });
});
