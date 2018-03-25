document.addEventListener('DOMContentLoaded', function () {
      document.querySelector('button').addEventListener('click', checkForm);
});

function checkForm() {
    var username = document.getElementById("nuser").value;
    var pass =  document.getElementById("npass").value;
    //parse database to see if valid
    if (username != "") {
        window.location.href = "landing.html";
        return false;
    }
}
