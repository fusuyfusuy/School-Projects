<?php

$DEBUG_MODE=false;

//COURSE CODE = BOATID


include("connect.php");
	
$reservationID = $_POST['reservationID'];

$result = myQuery("select * from tbl_reservations where reservationID = ".$reservationID);
                    
echo "<div><p>";          
foreach ($result as $record)
    {
        echo "reservationID: ".$record['reservationID']."<br>";
        echo "boatID: ".$record['boatID']."<br>";
        echo "customerID: ".$record['customerID']."<br>";
        echo "reserve date: ".$record['reservationDate']."<br>";
                }

echo "</p><form action= 'reservedx.php' method='post'>";
echo "<p><input type='hidden' value='".$reservationID."'name='reservationID'></p>";

echo "<p><input type='submit' name='submit' value='cancel reservation'></p>";
echo "</form></div>";
?>




<html >
    <head>
        
    </head>
    <body>
        
        
        
        <style>
        
        body{
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