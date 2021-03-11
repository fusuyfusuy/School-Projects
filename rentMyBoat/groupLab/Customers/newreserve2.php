<?php
require_once("connect.php");


$DEBUG_MODE=false;

echo <<<EXCERPT
<!DOCTYPE html>
<html>
<head>

<body>

	<div class="container")>
            
            <div class="leftpane" align="left">
              <h1>New Owner Info</h1> 
EXCERPT;



require_once("connect.php");

echo "<table border='1'>";
echo "<tr>";
    echo "<th>Boat ID</th>";
    echo "<th>Location</th>";
    echo "<th>Boat Type</th>";
    echo "<th>Capacity</th>";
    echo "<th>Daily Price</th>";
    echo "<th>Boat Name</th>";
echo "</tr>";

$selectedDate = $_POST['selectedDate'];
$id = $_POST['customerID'];

$records = myQuery("SELECT boatID, location, boatType, capacity, dailyPrice, boatName from `tbl_boats` WHERE boatID NOT IN (
    select boatID from tbl_reservations where tbl_reservations.reservationDate='".$selectedDate."')");

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

$list = myQuery("SELECT boatID from `tbl_boats` WHERE boatID NOT IN (
    select boatID from tbl_reservations where tbl_reservations.reservationDate='".$selectedDate."')");
    
echo "<div><form action='newreserve3.php' method='post'>";
echo "<input type = 'hidden' name=selectedDate value='".$selectedDate."'>";
echo "<p hidden>customerID: $id<input type='hidden' value='".$id."'name='customerID'></p>";
echo "<select name ='boatID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['boatID'].">".$record['boatID']."</option>";
    }
echo "</select><br>";
echo "<input class=button type='submit' name='submit' value='Select a Boat ID to Proceed'/>";
echo "</form> </div>              </body>";

//print $id;
?>

<style>

        body{
            text-align: center ;
            background : url(../../img/transparent.png);
            background-repeat: no-repeat; 
            background-size: cover;
            margin: center;
            font-family: "Arial";
            }
        
  
        h1{
            text-align: center;
        }
            table, td, th {  
             
            border: 1px solid ;
            text-align: left;
            margin: auto;
            }

            table {
                border-color: #000066;
                border-collapse: collapse;
                width: 70%;
                margin: auto;
            }

            th, td {
                padding: 15px;
            }
            
            .button {
                background-color: #19535F; /* Green */
                border: none;
                color: white;
                padding: 10px 25px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;}
                
            input, select {
                width: 20%;
                padding: 12px 20px;
                margin: 8px 0 auto;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
}
    div{
        margin: auto;
        float: center;
        text-align: center;
    }

</style>

</body>
</html>

