<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "cp";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("db: Connection failed: " . mysqli_connect_error());
}
//echo "db: Connected successfully";
?>