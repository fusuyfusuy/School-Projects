<?php
$DEBUG_MODE=false;


require("connect.php");


if (isset($_POST['submit']))
{
    $ownerID = $_POST['ownerID'];
    $location = $_POST['location'];
    $boatType = $_POST['boatType'];
    $capacity = $_POST['capacity'];
    $dailyPrice = $_POST['dailyPrice'];
    $boatName = $_POST['boatName'];

echo 'ownerID is '.$ownerID."<br>";


$q ="INSERT INTO tbl_boats (ownerID, location, boatType, capacity, dailyPrice, boatName) VALUES (".
    "'$ownerID',".
    "'$location',".
    "'$boatType',".
    "'$capacity',".
    "'$dailyPrice',".
    "'$boatName'".
    ")";
    
echo $q;
myQuery($q);

}

?>