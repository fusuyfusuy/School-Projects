<?php

$DEBUG_MODE=false;


require("connect.php");


if (isset($_POST['submit']))
{
    
    $name = $_POST['name'];
    $surname = $_POST['surname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $IBAN = $_POST['IBAN'];
    $ownerPassword=$_POST['ownerPassword'];

$q ="INSERT INTO tbl_boatOwners (name, surname, email, phone, IBAN, ownerPassword) VALUES (".
    "'$name',".
    "'$surname',".
    "'$email',".
    "'$phone',".
    "'$IBAN',".
    "'$hashedPassword'".
    ")";
    
myQuery($q);

echo "You have successfully signed in.";

}

else
{

echo "<div>";
echo "<h1>Fill the form to create new boat owner.</h1>";
echo "<form action=insert.php"." method='post'>";
echo "<p>Email: <input type='text' name='email'></p>";
echo "<p>Password: <input type='text' name='ownerPassword'></p>";
echo "<p>Name: <input type='text' name='name'></p>";
echo "<p>Surname: <input type='text' name='surname'></p>";
echo "<p>Phone: <input type='number' name='phone'></p>";
echo "<p>IBAN: <input type='text' name='IBAN'></p>";
echo "<p><input type='submit' name='submit' value='New Boat Owner'></p>";
echo "</form>";
echo "</div>";

}
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
