<!DOCTYPE html>
<html lang="en">
<head>
  <link rel = "stylesheet" href = "inputStyle.css">
<title>AAL Patient Login</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div class = "login">
  <h1>Smart AAL PATIENT Login</h1>
  <form method = "post" action = "">
    <p><input type = "text" name = "emailAddress" value = "" placeholder = "Email Address"></p>
    <p><input type = "password" name = "password" value = "" placeholder = "Password"></p>
    <p class = "submit"><input type = "submit" name = "login" value = "Login"></p>
  </form>
</div>

<div class = "login-help">
  <p>Need to register your device? <a href = "registration.php">Click here</a>.</p>
  <p>Login as carer? <a href = "login.php">Click here</a>.</p>
</div>

<?php
include "config.php";

error_reporting(0);

$connection = OpenConnection();
$address = $_POST["emailAddress"];
$localPass = $_POST["password"];

if (isset($_POST["login"])) {
  $password = ReturnPatientDetails($connection, $address);

  if ($localPass == $password) {
    header("Location:patientMain.php");
  } 
}

CloseConnection($connection);
?>

</body>
</html>