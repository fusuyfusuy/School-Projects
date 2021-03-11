<?php

$DEBUG_MODE=false;


require("connect.php");


if (isset($_POST['submit']))
{
    $customerName=$_POST['customerName'];
    $customerSurname=$_POST['customerSurname'];
    $customerPassword=$_POST['customerPassword'];
    $customerMail=$_POST['customerMail'];
    $customerPhone=$_POST['customerPhone'];
    
$hashedPassword=md5($customerPassword);

$q ="INSERT INTO tbl_customer (customerName, customerSurname, customerMail, customerPhone, customerPassword) VALUES (".
    "'$customerName',".
    "'$customerSurname',".
    "'$customerMail',".
    "'$customerPhone',".
    "'$hashedPassword'".
    ")";
    
myQuery($q);

echo "You have successfully signed up.";

}

else
{

echo "<div>";
echo "<h1>Fill the form to create new customer.</h1>";
echo "<form action=insert.php"." method='post'>";
echo "<p>Email: <input type='text' name='customerMail'></p>";
echo "<p>Password: <input type='text' name='customerPassword'></p>";
echo "<p>Name: <input type='text' name='customerName'></p>";
echo "<p>Surname: <input type='text' name='customerSurname'></p>";
echo "<p>Phone: <input type='number' name='customerPhone'></p>";
echo "<p><input type='submit' name='submit' value='New Customer'></p>";
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