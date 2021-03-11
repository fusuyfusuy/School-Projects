<?php
require ("connect.php");

if (isset($_POST['submit']))
{
    $customerID = $_POST['customerID'];
  

$q ="DELETE from tbl_customer ".

    " where customerID = $customerID";
    
    
   myQuery($q);
}

echo$q

?>
