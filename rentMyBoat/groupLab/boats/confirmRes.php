<?php

require_once("connect.php");

if (isset($_POST['submit']))
{
    
$boatID = $_POST['boatID'];

echo "<form action=ownerinfo.php method='post'>";
echo "<input type = 'hidden' name=boatID value='".$boatID."'";
echo "<p>Customer ID Number (TC): <input type='number' name='customerTC'></p>";
echo "<p><input type='submit' name='submit' value='Confirm Reservation'></p>";
echo "</form>";

}

?>