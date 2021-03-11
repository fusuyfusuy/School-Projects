<?php

$DEBUG_MODE=false;
require("connect.php");


if (isset($_POST['submit']))
{
    $customerPassword=$_POST['customerPassword'];
    $customerMail=$_POST['customerMail'];
    
    $hashedPw=md5($customerPassword);
    
    $result = myQuery("SELECT customerID FROM tbl_customer WHERE customerMail = '$customerMail' and customerPassword = '$hashedPw'");
    //$sql = "SELECT customerName FROM tbl_customer WHERE customerMail = '$customerMail' and customerPassword = '$hashedPw'";
    //$result = mysqli_query($db,$sql);
    $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
    $active = $row['active'];
      
    $count = mysqli_num_rows($result);

    // If result matched $myusername and $mypassword, table row must be 1 row
	foreach ($result as $record){
        $customerID = $record['customerID'];
    }
		
    if ($count == 1) {
        echo "<div><p>Login successfull.</p>";
        echo "<form action= ./logged.php method='post'>";
        echo "<p hidden>customerID: $customerID<input type='hidden' value='".$customerID."'name='customerID'></p>";
        echo "<input class=button type='submit' name='submit' value='Click here to access your dashboard'>";
        echo "</form></div>";
    }
    else {
        $error = "Your Login Name or Password is invalid";
        echo "<div><p>$error</p></div>";
    }
    
}


else

{
echo "<div>";
echo "<h1>Enter credentials to login.</h1>";
echo "<form action=\"\" method='post'>";
echo "<p>Email: <input type='text' name='customerMail'></p>";
echo "<p>Password: <input type='text' name='customerPassword'></p>";
echo "<p><input type='submit' name='submit' value='Login'></p>";
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