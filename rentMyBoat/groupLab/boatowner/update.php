<?php
require ("connect.php");
//update.php

if (isset($_POST['submit']))
{
    $ownerID = $_POST['ownerID'];
    $name = $_POST['name'];
    $surname = $_POST['surname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $IBAN = $_POST['IBAN'];

    

$q ="UPDATE tbl_boatOwners SET ".
    "name = '$name',".
    "surname = '$surname',".
    "email = '$email',".
    "phone = '$phone',".
    "IBAN = '$IBAN'".
    
    " where ownerID = $ownerID";
    
    
   myQuery($q);
}


?>