<?php

$DEBUG_MODE=false;

include("connect.php");

echo "<br>
        <br>
        <br>
        <br>
        <br>
        ";

$ownerID = $_POST['ownerID'];


$result = myQuery("select name,surname,email, phone, IBAN from tbl_boatOwners where ownerID = ".$ownerID);
                    
         
foreach ($result as $record)
    {
        $name = $record['name'];
        $surname = $record['surname'];
        $email = $record['email'];
        $phone = $record['phone'];
        $IBAN = $record['IBAN'];

        
    }

echo "<div><form action=update.php method='post'>";
echo "<p>ownerID: $ownerID <input type='hidden' value='".$ownerID."'name='ownerID'></p>";
echo "<p>name: <input type='text' value='".$name."'name='name'></p>";
echo "<p>surname: <input type='text' value='".$surname."' name='surname'></p>";
echo "<p>email: <input type='text' value='".$email."'name='email'></p>";
echo "<p>phone: <input type='number' value='".$phone."'name='phone'></p>";
echo "<p>IBAN: <input type='text' value='".$IBAN."'name='IBAN'></p>";
echo "<p><input type='submit' name='submit' value='Update BoatOwners'></p>";
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