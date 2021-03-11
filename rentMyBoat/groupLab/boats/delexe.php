<?php
require ("connect.php");


if (isset($_POST['submit']))
{
    $boatID = $_POST['boatID'];
  

$q ="DELETE from tbl_boats ".

    " where boatID = $boatID";
    
    
   myQuery($q);
}

echo$q

?>
