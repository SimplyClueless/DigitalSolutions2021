<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<div class="login">
  <h1>Smart Ambient Assisted Living Carer Login</h1>
  <form method="post" action="">
    <p><input type="text" name="login" value="" placeholder="Email Address"></p>
    <p><input type="password" name="password" value="" placeholder="Password"></p>
    <p class="submit"><input type="submit" name="commit" value="Login"></p>
  </form>
</div>

<div class="login-help">
  <p>Need to register your device? <a href="userRegistration.php">Click here</a>.</p>
</div>

<?php
include "config.php";

$connection = OpenConnection();
CloseConnection($connection);
?>

</body>
</html>