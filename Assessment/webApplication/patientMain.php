<!DOCTYPE html>
<html>
<head>
   <link rel = "stylesheet" href = "main.css">
</head>
<body>

<header>
    <h1>AAL Health Service (Patient View)</h1>
</header>

<?php
include "config.php";

error_reporting(0);

$connection = OpenConnection();

echo "<section>";
echo "<article>";
ReturnPatientData($connection, '1000000054a1de0b');
echo "</article>";
echo "</section>";

CloseConnection($connection);
?>

</body>
</html>