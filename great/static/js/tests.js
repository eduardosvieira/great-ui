var PROTOCOL = window.location.protocol;
var HOSTNAME = window.location.hostname;
var PORT = window.location.port;

var URL = PROTOCOL + "//" + HOSTNAME + ":" + PORT;

/*loading tests to modal to create new task*/
function loadTests(creatorCode) {
  $(document).ready(function(event) {
    $.ajax({
      url: URL + "/api/classroom/users/" + creatorCode + "/tests/",
      type: "GET",
      success: function(data) {
        $("#tests").empty();

        console.log(data);

        for(index in data) {
          $("#tests").append($("<option />").text(data[index]["name"]).attr("value", data[index]["_id"]));
        }

        /*Habilitando o uso de efeitos do Materialize nos selects*/
        $('select').material_select();
      }
    });
  });
}

$(document).ready(function(event) {
  var creatorCode = $("#creator_id").val();

  console.log("Carregando questionários...");

  loadTests(creatorCode);
});
