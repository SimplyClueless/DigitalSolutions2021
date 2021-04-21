<?php
function OpenConnection()
{
    $dbhost = "34.116.119.134";
    $dbuser = "root";
    $dbpass = "sheldon1";
    $dbname = "benDB";
    
    $connection = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die("Connect failed: $s\n". $connection->error);
    
    return $connection;
}

function CloseConnection($connection)
{
    $connection->close();
}       
?>