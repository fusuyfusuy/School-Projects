<?php
require_once("connect.php");

$customerID = $_POST['customerID'];
$selectedDate = $_POST['selectedDate'];
$boatID = $_POST['boatID'];

$res=myQuery("select dailyPrice from tbl_boats where boatID=".$boatID);

foreach($res as $a){
    $price = $a['dailyPrice'];
}


echo "<div>";
echo "<h1>Confirm the reservation.</h1>";
echo "<form action=newreserve4.php method='post'>";
echo "<p >customerID:           $customerID<input type='hidden' value='".$customerID."'name='customerID'></p>";
echo "<p >selected date:        $selectedDate<input type='hidden' value='".$selectedDate."'name='selectedDate'></p>";
echo "<p >boat id:              $boatID<input type='hidden' value='".$boatID."'name='boatID'></p>";
echo "<p >price:                $price<input type='hidden' value='".$price."'name='price'></p>";
echo "<input class=button type='submit' name='submit' value='confirm'>";
echo "</form>";
echo "<br><br>";

echo "</div>";

?>


<html >
    <head>
        
    </head>
    <br> 
    <br> 
    <br> 
    <br> 
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