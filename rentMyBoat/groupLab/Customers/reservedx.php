<?php
require ("connect.php");

if (isset($_POST['submit']))
{
    $reservationID = $_POST['reservationID'];
  

$q ="DELETE from tbl_reservations ".

    " where reservationID = $reservationID";
    
    
   myQuery($q);
}

echo "Your reservation is cancelled."

?>
