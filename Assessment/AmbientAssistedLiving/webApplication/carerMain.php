<!DOCTYPE html>
<html lang="en">
<head>
    <title>AAL Carer View</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {
        box-sizing: border-box;
    }
</style>
    <link rel = "stylesheet" href = "main.css">
</head>
<body>

<header>
  <h2>AAL Health Service (Carer View)</h2>
</header>

<?php
include "config.php";

error_reporting(0);

$connection = OpenConnection();
createElements($connection);

function createElements($connection)
{
    echo "<section>";
    echo "<nav>";
    echo "<h2>Patient List</h2>";
    echo "<ul>";
    ReturnAssignedPatients($connection, 9);
    echo "</ul>";
    echo "</nav>";

    echo "<article>";
    echo "<h1>2 John Doe</h1>";
    ReturnPatientData($connection, '1000000054a1de0b');
    echo "</article>";
    echo "</section>";
}

CloseConnection($connection);
?>

</body>
</html>