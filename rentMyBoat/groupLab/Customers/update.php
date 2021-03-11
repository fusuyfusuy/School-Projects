<?php
require ("connect.php");
//update.php

if (isset($_POST['submit']))
{
    $customerID = $_POST['customerID'];
    $name = $_POST['name'];
    $surname = $_POST['surname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];

    

$q ="UPDATE tbl_customer SET ".
    "customerName = '$name',".
    "customerSurname = '$surname',".
    "customerMail = '$email',".
    "customerPhone = '$phone'".
    
    " where customerID = $customerID";
    
    
   myQuery($q);
}


?>