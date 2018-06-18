var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $(".modal").modal();

  $("#btnCreateNotice").on("click", function(event) {
    var classId = $("#classId").val();
    var title = $("#modal-notice-title").val();
    var description = $("#modal-notice-description").val();

    $.ajax({
      url: URL + "/classroom/notices/",
      type: "POST",
      data: {"title": title, "description": description, "createdAt": Date(), "classId": classId},
      success: function(data) {
        window.location.replace("/classroom/classes/" + classId + "/");
      },
      error: function(data) {

      }
    });
  });

  $("#btnEditNotice").on("click", function(event) {
    var classId = $("#classId").val();
    var noticeId = $("#modal-edit-notice-id").val();
    var title = $("#modal-edit-notice-title").val();
    var description = $("#modal-edit-notice-description").val();

    $.ajax({
      url: URL + "/classroom/notices/" + noticeId + "/",
      type: "PUT",
      data: {"title": title, "description": description},
      success: function(data) {
        window.location.replace(URL + "/classroom/classes/" + classId + "/");
      }
    });
  });

  $(".callModalEditNotice").on("click", function(event) {
    var noticeId = $(this).parent().siblings(".noticeId").text();

    $("#modal-edit-notice-id").attr("value", noticeId);
  });
});
