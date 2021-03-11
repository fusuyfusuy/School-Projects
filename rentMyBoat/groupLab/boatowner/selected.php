 <head>
  <meta charset="UTF-8">
</head> 

<?php

include("connect.php");

    $ownerID = $_POST["ownerID"];
    
echo "<h1> owner information</h1><br>";
echo "<table border='1'>";
echo "<tr>";
    echo "<th>Owner ID</th>";
    echo "<th>name</th>";
    echo "<th>surname</th>";
    echo "<th>email</th>";
    echo "<th>phone</th>";
    echo "<th>iban</th>";
echo "</tr>";


$records = myQuery("SELECT ownerID, name, surname, email, phone, IBAN FROM tbl_boatOwners WHERE ownerID='".$ownerID."'");

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
echo "<form action=edit.php method='post'>";
echo "<p hidden>ownerID: $ownerID<input type='hidden' value='".$ownerID."'name='ownerID'></p>";
echo "<input class=button type='submit' name='submit' value='click to edit owner info'>";
echo "</form>";
echo "<br><br>";


echo "<h1> boats of the owner</h1>";
echo "<table border='1'>";
echo "<tr>";
    echo "<th>Boat ID</th>";
    echo "<th>Location</th>";
    echo "<th>Boat Type</th>";
    echo "<th>Capacity</th>";
    echo "<th>Daily Price</th>";
    echo "<th>Boat Name</th>";
echo "</tr>";

$records = myQuery("SELECT boatID, location, boatType, capacity, dailyPrice, boatName from `tbl_boats` WHERE ownerID='.$ownerID.'");

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

echo "<form action=../boats/insert.php method='post'>";
echo "<input type='hidden' value='$ownerID' name='ownerID'>";
echo "<input class=button type='submit' name='submit' value='click to create new boat'>";
echo "</form>";
echo "<br><br><br>";

$list=myQuery("SELECT boatID, boatName from `tbl_boats` WHERE ownerID='.$ownerID.'");
echo "<form action=../boats/edit.php method='post'>";
echo "<select name ='boatID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['boatID'].">".$record['boatName']."</option>";
    }
echo "</select><br><br>";
echo "<input class=button type='submit' name='submit' value='Select Boat to edit'/><br><br>";
echo "</form>";


echo "<br>";
$list=myQuery("SELECT boatID, boatName from `tbl_boats` WHERE ownerID='.$ownerID.'");
echo "<form action=../boats/delete.php method='post'>";
echo "<select name ='boatID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['boatID'].">".$record['boatName']."</option>";
    }
echo "</select><br><br>";
echo "<input class=button type='submit' name='submit' value='Select Boat to remove'/>";
echo "</form>";

echo "<br>";


echo "<h1> reservations </h1>";
echo "<table border='1'>";
echo "<tr>";
    echo "<th>reservationID</th>";
    echo "<th>customerID</th>";
    echo "<th>boatID</th>";
    echo "<th>reservationDate</th>";
    echo "<th>totalCost</th>";
    echo "<th>transactionDate</th>";
    echo "<th>paymentDate</th>";
echo "</tr>";

$records = myQuery("SELECT * from `tbl_reservations` WHERE boatID IN (SELECT boatID FROM tbl_boats WHERE ownerID='.$ownerID.')");

foreach ($records as $row) 
    { 
        echo "<tr>";
        foreach ($row as $field)
            {
                echo "<td>".$field."</td>";
            }
        echo "</tr>";
    }
    
echo "</table><br>";

$list=myQuery("SELECT reservationID from `tbl_reservations` WHERE paymentDate IS NULL AND boatID IN (SELECT boatID FROM tbl_boats WHERE ownerID='.$ownerID.')");
echo "<form action=payment.php method='post'>";
echo "<p>Select reservation to confirm payment (only non confirmed reservations are shown):   <select name ='reservationID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['reservationID'].">".$record['reservationID']."</option>";
    }
echo "</select><br>";
echo "<p>Confirmed payment date:    <input type='date' name='paymentDate'><br>";
echo "<br><input class=button type='submit' name='submit' value='confirm payment'/>";
echo "</form>";

echo "<br><br><br>";



?>



<html >
    <head>
        
    </head>
    <body>
        
        
        
        <style>
        
        body{
            text-align: center ;
            background : url(../../img/transparent.png);
            background-repeat: no-repeat; 
            background-size: cover;
            margin: center;
            font-family: "Arial";
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
            h1{
                font-family: "Arial";
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
                width: 30%;
                padding: 12px 20px;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid #ccc;
                border-radius: 4px;
                box-sizing: border-box;
}

       </style>
    </body>
</html>