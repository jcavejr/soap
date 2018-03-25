document.addEventListener('DOMContentLoaded', function () {
      document.querySelector('button').addEventListener('click', checkForm);
});

function checkForm() {
    var username = document.getElementById("user").value;
    var pass =  document.getElementById("pass").value;
    //parse database to see if valid
    if (username != "") {
        window.location.href = "landing.html";
        return false;
    }
}
