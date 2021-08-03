<?php
error_reporting(0);

function OpenConnection()
{
    $dbhost = "35.201.1.208";
    $dbuser = "root";
    $dbpass = "Sheldon#1";
    $dbname = "benHealthService";
    
    $connection = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die("Connect failed: $s\n". $connection->error);
    
    return $connection;
}

function ReturnPatientDetails($connection, $address)
{
    $query = "SELECT password FROM patientData WHERE emailAddress = '$address'";
    $result = $connection->query($query);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $password = $row["password"];
        }
    }

    return $password;    
}

function ReturnCarerDetails($connection, $address)
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

function ImportData($connection, $carerID, $deviceID, $firstName, $lastName, $emailAddress, $password, $emergencyPhone, $dob, $gender, $address, $healthConditions)
{
    $query = "INSERT INTO patientData (carerID, deviceID, firstName, lastName, emailAddress, password, emergencyPhone, dob, gender, address, healthConditions) 
    VALUES ('$carerID', '$deviceID', '$firstName', '$lastName', '$emailAddress', '$password', '$emergencyPhone', '$dob', '$gender', '$address', '$healthConditions')";

    if (mysqli_query($connection, $query)) {
        echo "Device added successfully...";
    }
    else {
        echo "Error...";
    }
}

function ReturnAssignedPatients($connection, $carerID)
{
    $query = "SELECT patientID, firstName, lastName FROM patientData WHERE carerID = $carerID";
    $result = $connection->query($query);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<input type = 'submit' name = '" . $row["patientID"] . "' value = '" . $row["patientID"] . " " . $row["firstName"] . " " . $row["lastName"] . "'><br><br>";
        }
    }
}

function ReturnPatientData($connection, $deviceID)
{
    $query = "SELECT * FROM deviceInformation WHERE deviceID = '$deviceID' ORDER BY dateTime DESC";
    $result = $connection->query($query);

    echo "<h2>Device ID, Heart Rate, Acceleration, Temperature, Date Time</h2>";
    echo "<div class = 'clsScroll'>";
    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<div>" . $row["deviceID"] . ", " . $row["heartRate"] . ", " . $row["acceleration"] . ", " . $row["temperature"] . ", " . $row["dateTime"] . ", " . "</div>";
        }
    }
    echo "</div>";
}

function CloseConnection($connection)
{
    $connection->close();
}       
?>