<!DOCTYPE html>
<html>
<head>
  <link rel = "stylesheet" href = "inputStyle.css">
</head>
<body>

<div class = "login">
  <h1>AAL Device Registration</h1>
  <form method = "post" action="">
    <p><input type = "text" name = "firstName" value = "" placeholder = "First Name"><input type = "text" name = "lastName" value = "" placeholder = "Last Name"></p>
    <p><input type = "text" name = "emailAddress" value = "" placeholder = "Email Address"><input type = "text" name = "contactNumber" value = "" placeholder = "Mobile / Emergency Number"></p>
    <p><input type = "password" name = "password" value = "" placeholder = "Password"><input type = "password" name = "confirmPassword" value = "" placeholder = "Confirm Password"></p>
    <p><input type = "text" name = "dob" value = "" placeholder = "Date of Birth"><input type = "text" name = "gender" value = "" placeholder = "Gender (M, F or O)"><input type = "text" name = "address" value = "" placeholder = "Street Address"><input type = "text" name = "healthConditions" value = "" placeholder = "Health Conditions"></p>
    <p><input type = "text" name = "carerID" value = "" placeholder = "Carer ID Number *"><input type = "text" name = "deviceID" value = "" placeholder = "Device ID / Serial Number **"></p>
    <p>*Please refer to your doctors note for this ID number*</p>
    <p>**Check under your issued device for this unique code*</p>
    <p class = "submit"><input type = "submit" name = "commit" value = "Register"></p>
  </form>
</div>

<div class = "login-help">
  <p>Already Registered? <a href = "index.php">Go to Login</a>.</p>
</div>

<?php
include "config.php";

error_reporting(0);

$connection = OpenConnection();

$firstName = $_POST["firstName"];
$lastName = $_POST["lastName"];
$emailAddress = $_POST["emailAddress"];
$emergencyPhone = $_POST["contactNumber"];
$password = $_POST["password"];
$confirmPassword = $_POST["confirmPassword"];
$dob = $_POST["dob"];
$gender = $_POST["gender"];
$address = $_POST["address"];
$healthConditions = $_POST["healthConditions"];
$carerID = $_POST["carerID"];
$deviceID = $_POST["deviceID"];

if ($password == $confirmPassword) {
  ImportData($connection, $carerID, $deviceID, $firstName, $lastName, $emailAddress, $password, $emergencyPhone, $dob, $gender, $address, $healthConditions);
}

CloseConnection($connection);
?>

</body>
</html>