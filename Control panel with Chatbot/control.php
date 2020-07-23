<html>
<style>

body{
  background-color:#FFFAF0;
  }
</style>  
</html>

<?php

$conn = mysqli_connect("localhost", "root", "", "cp");
$result = ""; 
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if(isset($_POST['F']))
{	
// Attempt insert query execution
$sql = "UPDATE rd SET direction = 'F' WHERE id=1";
$result = $conn->query($sql);
}

if(isset($_POST['B']))
{	
// Attempt insert query execution
$sql = "UPDATE rd SET direction = 'B' WHERE id=1";
$result = $conn->query($sql);
}

if(isset($_POST['R']))
{	
// Attempt insert query execution
$sql = "UPDATE rd SET direction = 'R' WHERE id=1";
$result = $conn->query($sql);
}

if(isset($_POST['L']))
{	
// Attempt insert query execution
$sql = "UPDATE rd SET direction = 'L' WHERE id=1";
$result = $conn->query($sql); 
}


if(isset($_POST['S']))
{	
// Attempt insert query execution
$sql = "UPDATE rd SET direction = 'S' WHERE id=1";
$result = $conn->query($sql);  
}

  
$result = $conn->query("SELECT Direction FROM rd");
$row = $result->fetch_assoc();
echo "" . $row["Direction"]. "<br>";

// Close connection
$conn->close();
?>