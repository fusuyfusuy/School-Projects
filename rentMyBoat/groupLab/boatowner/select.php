<?php 
$DEBUG_MODE=false;
include("connect.php");

echo "<br>
        <br>
        <br>
        <br>
        <br>
        ";

$list=myQuery("select ownerID, name from tbl_boatOwners order by name");
echo "<div><form action='selected.php' method='post'>";
echo "<select name ='ownerID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['ownerID'].">".$record['name']."</option>";
    }
echo "</select><br>";
echo "<input type='submit' name='submit' value='Select'/>";
echo "</form></div>";

?>

<html >
    <head>
        
    </head>
    <body>
        <style>
        
        body{
            text-align: center ;
            background : url(../../img/boat.jpg);
            background-repeat: no-repeat; 
            background-size: cover;
            margin: center;
            font-family: "Arial";
            }
            
            table, td, th {  
  border: 1px solid #ddd;
  text-align: left;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  padding: 15px;
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