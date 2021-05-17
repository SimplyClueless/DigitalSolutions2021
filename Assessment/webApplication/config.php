<?php
function OpenConnection()
{
    $dbhost = "35.201.1.208";
    $dbuser = "root";
    $dbpass = "Sheldon#1";
    $dbname = "benHealthService";
    
    $connection = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die("Connect failed: $s\n". $connection->error);
    
    return $connection;
}

function ReturnDetails($connection, $address)
{
    $query = "SELECT password FROM carerDetails WHERE emailAddress = '$address'";
    $result = $connection->query($query);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $password = $row["password"];
        }
    }

    return $password;    
}

function ImportData($connection, $carerID, $deviceID, $firstName, $lastName, $emailAddress, $password, $emergencyPhone)
{
    $query = "INSERT INTO patientData (carerID, deviceID, firstName, lastName, emailAddress, password, emergencyPhone) 
    VALUES ('$carerID', '$deviceID', '$firstName', '$lastName', '$emailAddress', '$password', '$emergencyPhone')";

    if (mysqli_query($connection, $query)) {
        echo "Device added successfully...";
    }
    else {
        echo "Error...";
    }
}

function CloseConnection($connection)
{
    $connection->close();
}       
?>