<?php

$DEBUG_MODE=false;

//COURSE CODE = BOATID


include("connect.php");
	
$list=myQuery("select ownerID,name from tbl_boatOwners order by ownerID");
echo "<form action='' method='post'>";
echo "<select name ='ownerID'>";
foreach ($list as $record)    {
        echo "<Option value=".$record['ownerID'].">".$record['name']."</option>";
    }
echo "</select><br>";
echo "<input type='submit' name='submit' value='Select'/>";
echo "</form>";

$ownerID = $_POST['ownerID'];

$result = myQuery("select ownerID, name, surname, email, phone, IBAN from tbl_boatOwners where ownerID = ".$ownerID);
                    
                    
foreach ($result as $record)
    {
        echo "ownerID: ".$record['ownerID']."<br>";
        echo "Name: ".$record['name']."<br>";
        echo "Surame: ".$record['surname']."<br>";
        echo "E-Mail: ".$record['email']."<br>";
        echo "Phone: ".$record['phone']."<br>";
        echo "IBAN: ".$record['IBAN']."<br>";
                }

echo "<form action= 'delexe.php' method='post'>";
echo "<p><input type='hidden' value='".$ownerID."'name='ownerID'></p>";

echo "<p><input type='submit' name='submit' value='Delete Boat Owner'></p>";
echo "</form>";
?>
