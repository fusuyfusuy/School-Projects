<?php
require ("connect.php");

if (isset($_POST['submit']))
{
    $ownerID = $_POST['ownerID'];
  

$q ="DELETE from tbl_boatOwners ".

    " where ownerID = $ownerID";
    
    
   myQuery($q);
}

echo$q

?>
