<?php

$DEBUG_MODE=false;

//COURSE CODE = BOATID


include("connect.php");
	
$list=myQuery("select customerID,customerName from tbl_customer order by customerID");
echo "<form action='' method='post'>";
echo "<select name ='customerID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['customerID'].">".$record['customerName']."</option>";
    }
echo "</select><br>";
echo "<input type='submit' name='submit' value='Select'/>";
echo "</form>";

$customerID = $_POST['customerID'];

$result = myQuery("select * from tbl_customer where customerID = ".$customerID);
                    
                    
foreach ($result as $record)
    {
        echo "customerID: ".$record['customerID']."<br>";
        echo "Name: ".$record['customerName']."<br>";
        echo "Surame: ".$record['customerSurname']."<br>";
        echo "E-Mail: ".$record['customerMail']."<br>";
        echo "Phone: ".$record['customerPhone']."<br>";
                }

echo "<form action= 'delexe.php' method='post'>";
echo "<p><input type='hidden' value='".$customerID."'name='customerID'></p>";

echo "<p><input type='submit' name='submit' value='Delete Customer'></p>";
echo "</form>";
?>
