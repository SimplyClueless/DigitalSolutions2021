<?php
function OpenConnection()
{
    $dbhost = "35.116.119.134";
    $dbuser = "root";
    $dbpass = "Sheldon#1";
    $dbname = "juriDB";
    
    $connection = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die("Connect failed: $s\n". $connection->error);
    
    return $connection;
}

function CloseConnection($connection)
{
    $connection->close();
}    
?>