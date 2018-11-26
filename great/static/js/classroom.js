var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

$(document).ready(function(event){
  $(".modal").modal();


  $(".btnDeleteInvite").on("click", function(event) {
    var inviteId = $(this).parent().siblings(".inviteId").text();

    $.ajax({
      url: URL + "/classroom/invites/" + inviteId + "/",
      type: "DELETE",
      success: function(data) {
        window.location.replace(URL + "/classsroom/")
      }
    });
  });
});
