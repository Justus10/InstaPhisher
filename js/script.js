document.forms["HmktE"].addEventListener("submit", function(e) {

  var error1;
  var error2;

  var user = document.getElementById("username").value;
  var pass = document.getElementById("password").value;


  if ((user.length <= 0) || (pass.length < 6)) {
    error1 = "Votre mot de passe est incorrect.";
    error2 = "Veuillez le vérifier.";
    e.preventDefault();
    document.getElementById("error1").innerHTML = error1;
    document.getElementById("error2").innerHTML = error2;
    return false;
  }
});
