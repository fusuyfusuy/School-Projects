<?php

$DEBUG_MODE=false;

//COURSE CODE = BOATID


include("connect.php");

echo "<br>
        <br>
        <br>
        <br>
        <br>
        ";


$boatID = $_POST['boatID'];

$result = myQuery("select boatID, ownerID, location, boatType, capacity, dailyPrice, boatName from tbl_boats where boatID = ".$boatID);
                    
                    
foreach ($result as $record)
    {
        echo "Boat ID: ".$record['boatID']."<br>";
        echo "Owner ID: ".$record['ownerID']."<br>";
        echo "Location: ".$record['location']."<br>";
        echo "Boat Type: ".$record['boatType']."<br>";
        echo "Capacity: ".$record['capacity']."<br>";
        echo "Daily Price: ".$record['dailyPrice']."<br>";
        echo "Boat Name: ".$record['boatName']."<br>";
                }

echo "<form action= 'delexe.php' method='post'>";
echo "<p><input type='hidden' value='".$boatID."'name='boatID'></p>";

echo "<p><input type='submit' name='submit' value='Delete Boat'></p>";
echo "</form>";
?>
<html >
    <head>
        
    </head>
    <body>
        
        
        
        <style>
        
        body{
             color: #19535F;
            text-align: center ;
            background : url(../../img/transparent.png);
            background-repeat: no-repeat; 
            background-size: cover;
            margin: center;
            font-family: "Arial";
            }
               </style>
    </body>
</html>

