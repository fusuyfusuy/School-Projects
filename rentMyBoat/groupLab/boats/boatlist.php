<?php


$DEBUG_MODE=false;
require("connect.php");


$ownerID = $_POST['ownerID'];
print $ownerID;


echo "<table border='1'>";
echo "<tr>";
    echo "<th>Boat ID</th>";
    echo "<th>Location</th>";
    echo "<th>Boat Type</th>";
    echo "<th>Capacity</th>";
    echo "<th>Daily Price</th>";
    echo "<th>Boat Name</th>";
echo "</tr>";



$records = myQuery("SELECT boatID, location, boatType, capacity, dailyPrice, boatName from `tbl_boats` WHERE ownerID=".$ownerID);

foreach ($records as $row) 
    { 
        echo "<tr>";
        foreach ($row as $field)
            {
                echo "<td>".$field."</td>";
            }
        echo "</tr>";
    }
    
echo "</table>";

echo "<br>";


?>


