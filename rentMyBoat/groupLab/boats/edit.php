<?php

$DEBUG_MODE=false;

include("connect.php");

echo "<br>
        <br>
        <br>
        <br>
        <br>
        ";

$boatID = $_POST['boatID'];


$result = myQuery("select boatName,ownerID,location,boatType, capacity, dailyPrice from tbl_boats where boatID = ".$boatID);
                    
         
foreach ($result as $record)
    {
        $boatName = $record['boatName'];
        $ownerID = $record['ownerID'];
        $location = $record['location'];
        $boatType = $record['boatType'];
        $capacity=$record['capacity'];
        $dailyPrice=$record['dailyPrice'];
    
        
    }
    
echo "<div><form action=update.php method='post'>";
echo "<p>boatID: $boatID<input type='hidden' value='".$boatID."'name='boatID'></p>";
echo "<p>boatName: <input type='text' value='".$boatName."'name='boatName'></p>";
echo "<p>ownerID: $ownerID<input type='hidden'  value='".$ownerID."' name='ownerID'></p>";
echo "<p>location: <input type='text' value='".$location."'name='location'></p>";
echo "<p>boatType: <input type='text' value='".$boatType."'name='boatType'></p>";
echo "<p>capacity: <input type='text' value='".$capacity."'name='capacity'></p>";
echo "<p>dailyPrice: <input type='text' value='".$dailyPrice."'name='dailyPrice'></p>";
echo "<p><input type='submit' name='submit' value='Update Boat'></p>";
echo "</div></form>";

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
                        
input, select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}
input[type=text]:focus {
  border: 3px solid #555;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width: 600px;
  float: center;
  margin: auto;
}
               </style>
    </body>
</html>
