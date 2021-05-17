<!DOCTYPE html>
<html>
<head>
  <link rel = "stylesheet" href = "inputStyle.css">
</head>
<body>

<div class = "login">
  <h1>Smart Ambient Assisted Living</h1>
  <h2>User Device Registration Form</h2>
  <form method = "post" action="">
    <p><input type = "text" name = "firstName" value = "" placeholder = "First Name"><input type = "text" name = "lastName" value = "" placeholder = "Last Name"></p>
    <p><input type = "text" name = "emailAddress" value = "" placeholder = "Email Address"><input type = "text" name = "contactNumber" value = "" placeholder = "Mobile / Emergency Number"></p>
    <p><input type = "password" name = "password" value = "" placeholder = "Password"><input type = "password" name = "confirmPassword" value = "" placeholder = "Confirm Password"></p>
    <p><input type = "text" name = "carerID" value = "" placeholder = "Carer ID Number"></p>
    <p>*Please refer to your doctors note for this ID number*</p>
    <p><input type = "text" name = "deviceID" value = "" placeholder = "Device ID / Serial Number"></p>
    <p>*Check under your issued device for this unique code*</p>
    <p class = "submit"><input type = "submit" name = "commit" value = "Register"></p>
  </form>
</div>

<div class = "login-help">
  <p>Already Registered? <a href = "index.php">Go to Login</a>.</p>
</div>

<?php
include "config.php";

$connection = OpenConnection();

$firstName = $_POST["firstName"];
$lastName = $_POST["lastName"];
$emailAddress = $_POST["emailAddress"];
$emergencyPhone = $_POST["contactNumber"];
$password = $_POST["password"];
$confirmPassword = $_POST["confirmPassword"];
$carerID = $_POST["carerID"];
$deviceID = $_POST["deviceID"];

if ($password == $confirmPassword) {
  ImportData($connection, $carerID, $deviceID, $firstName, $lastName, $emailAddress, $password, $emergencyPhone);
}

CloseConnection($connection);
?>

</body>
</html>