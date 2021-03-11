<?php

function myQuery($qry)
{
$servername = "localhost";
$username = "gr15boun_group";
$password = "Q23qwe.-L";
$dbname = "gr15boun_rentMyBoat";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error)
{
    
    die("Connection failed: " . $conn->connect_error);
}

$result = mysqli_query($conn, $qry);

if ($GLOBALS['DEBUG_MODE'])
{
   
    echo $qry."<br>";
    echo mysqli_error($conn)."<hr>";
}


mysqli_close($conn);

return $result;

}

?>