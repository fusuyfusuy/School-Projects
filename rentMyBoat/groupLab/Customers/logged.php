 <head>
  <meta charset="UTF-8">
</head> 

<?php

include("connect.php");

    $customerID = $_POST["customerID"];
echo "<h1> customer information</h1><br>";
echo "<table border='1'>";
echo "<tr>";
    echo "<th>Customer ID</th>";
    echo "<th>name</th>";
    echo "<th>surname</th>";
    echo "<th>email</th>";
    echo "<th>phone</th>";
echo "</tr>";


$records = myQuery("SELECT customerID, customerName,customerSurname,customerMail,customerPhone FROM tbl_customer WHERE customerID='".$customerID."'");

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
echo "<p hidden>customerID: $customerID<input type='hidden' value='".$customerID."'name='customerID'></p>";
echo "<input class=button type='submit' name='submit' value='click to edit customer info'>";
echo "</form>";
echo "<br><br>";

echo "<h1> reservations </h1>";
echo "<table border='1'>";
echo "<tr>";
    echo "<th>reservationID</th>";
    echo "<th>boatID</th>";
    echo "<th>customerID</th>";
    echo "<th>reservationDate</th>";
    echo "<th>totalCost</th>";
    echo "<th>transactionDate</th>";
    echo "<th>paymentDate</th>";
echo "</tr>";

$records = myQuery("SELECT * from `tbl_reservations` WHERE customerID = ".$customerID);

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

echo "<br>";
echo "<form action=newreserve.php method='post'>";
echo "<p hidden>customerID: $customerID<input type='hidden' value='".$customerID."'name='customerID'></p>";
echo "<input class=button type='submit' name='submit' value='click to create new reservation'>";
echo "</form>";
echo "<br><br>";

$list=myQuery("SELECT reservationID from `tbl_reservations` WHERE customerID=".$customerID);
echo "<form action='reservationdel.php' method='post'>";
echo "<p>Select reservation to cancel:   <select name ='reservationID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['reservationID'].">".$record['reservationID']."</option>";
    }
echo "</select><br>";
echo "<br><input class=button type='submit' name='submit' value='cancel reservation'/>";
echo "</form>";




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