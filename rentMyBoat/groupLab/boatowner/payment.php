<?php

$DEBUG_MODE=false;


require("connect.php");


if (isset($_POST['submit']))
{
    
    $reservationID = $_POST['reservationID'];
    $paymentDate = $_POST['paymentDate'];
 

$q ="UPDATE tbl_reservations SET ".
    "paymentDate = '$paymentDate' where reservationID = $reservationID";
    
myQuery($q);

}

?>
