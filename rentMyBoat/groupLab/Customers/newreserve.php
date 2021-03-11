<?php

$DEBUG_MODE=false;


require("connect.php");

$id=$_POST['customerID'];

echo <<<exe
<div>
<form action=newreserve2.php method='post'>
<p>Select Your Available Date: <input type="date" name="selectedDate" ></p>
<p hidden>customerID: $id<input type='hidden' value='$id'name='customerID'></p>
  <input type="submit" value="Select">
</form></div>
exe;
//print $id;
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
  width: 300px;
  float: center;
  margin: auto;
}
         </style>
    </body>
</html>
