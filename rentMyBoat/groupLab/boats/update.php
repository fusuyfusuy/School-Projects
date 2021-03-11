<?php
require ("connect.php");
//update.php

if (isset($_POST['submit']))
{
    $boatID = $_POST['boatID'];
    $ownerID = $_POST['ownerID'];
    $location = $_POST['location'];
    $boatName = $_POST['boatName'];
    $boatType = $_POST['boatType'];
    $capacity = $_POST['capacity'];
    $dailyPrice = $_POST['dailyPrice'];
    
    

$q ="UPDATE tbl_boats SET ".
    "ownerID = '$ownerID',".
    "location = '$location',".
    "boatName = '$boatName',".
    "boatType = '$boatType',".
    "capacity = '$capacity',".
    "dailyPrice = '$dailyPrice'".
    
    " where boatID = $boatID";
    
    
   myQuery($q);
}


?>