<!DOCTYPE html>
<html>
<head>
  <link rel = "stylesheet" href = "inputStyle.css">
</head>
<body>

<div class = "login">
  <h1>Smart Ambient Assisted Living Carer Login</h1>
  <form method = "post" action = "">
    <p><input type = "text" name = "emailAddress" value = "" placeholder = "Email Address"></p>
    <p><input type = "password" name = "password" value = "" placeholder = "Password"></p>
    <p class = "submit"><input type = "submit" name = "login" value = "Login"></p>
  </form>
</div>

<div class = "login-help">
  <p>Need to register your device? <a href = "registration.php">Click here</a>.</p>
</div>

<?php
include "config.php";

$connection = OpenConnection();
$address = $_POST["emailAddress"];
$localPass = $_POST["password"];

if (isset($_POST["login"])) {
  $password = ReturnDetails($connection, $address);

  if ($localPass == $password) {
    header("Location:main.php");
  } 
}

CloseConnection($connection);
?>

</body>
</html>