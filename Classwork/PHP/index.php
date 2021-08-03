<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body>
    <link href = "registration.css" type = "text/css" rel = "stylesheet">
    <h2>Hello World!</h2>
    <form names = "form1" action = "modified.php" method = "post" enctype = "data">
    <div class = "container">
        <div class = "form_group">
            <label>First Name:</label>
            <input type = "text" name = "firstName" value = "" required>
        </div>
        <div class = "form_group">
            <label>Middle Name:</label>
            <input type = "text" name = "middleName" value = "" required>
        </div>
        <div class = "form_group">
            <label>Last Name:</label>
            <input type = "text" name = "lastName" value = "" required>
        </div>
        <div class = "form_group">
            <label>Password:</label>
            <input type = "text" name = "password" value = "" required>
        </div>
</body>

<?php
include "config.php";

#$connection = openConnection();

APIDataReturn("SELECT * FROM", "WHERE title LIKE 'jones'");
echo "<br>";
echo "<br>";
echo "--------------------";
echo "<br>";

#closeConnection($connection);
?>

</html>