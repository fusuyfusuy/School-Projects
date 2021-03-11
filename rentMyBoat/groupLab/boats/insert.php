<?php

echo "<br>
        <br>
        <br>
        <br>
        <br>
        ";
        
$ownerID=$_POST['ownerID'];

echo "<div><form action=insertexe.php"." method='post'>";
echo "<p>OwnerID: $ownerID<input type='hidden' value='$ownerID' name='ownerID'></p>";
echo "<p>Location: <input type='text' name='location'></p>";
echo "<p>Boat Type: <input type='text' name='boatType'></p>";
echo "<p>Capacity: <input type='number' name='capacity'></p>";
echo "<p>Daily Price: <input type='number' name='dailyPrice'></p>";
echo "<p>Boat Name: <input type='text' name='boatName'></p>";
echo "<p><input type='submit' name='submit' value='Insert New Boat'></p>";
echo "</form></div>";

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
