<?php

require_once("connect.php");

if (isset($_POST['submit']))
{
    $boatID = $_POST['boatID'];
    $customerTC = $_POST['customerTC'];
 
    $q = myQuery("SELECT tbl_boatOwners.name, tbl_boatOwners.surname, tbl_boatOwners.email, tbl_boatOwners.phone, tbl_boatOwners.IBAN 
    FROM tbl_boatOwners, tbl_boats 
    WHERE tbl_boats.boatID =$boatID AND tbl_boats.ownerID = tbl_boatOwners.ownerID");
    
    Echo "Boat Owner Information";
    
   foreach ($q as $record)
    {
        
        echo "Name: ".$record['name']." ".$record['surname']."<br>";
        echo "E-Mail: ".$record['email']."<br>";
        echo "Phone Number: ".$record['phone']."<br>";
        echo "IBAN for Payment: ".$record['IBAN']."<br>";
      
                }
}
    ?>