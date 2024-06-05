<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Process form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $gender = $_POST['gender'];
    $branch = $_POST['branch'];
    $registrationNumber = $_POST['registrationNumber'];
    $location = $_POST['location'];

    // You can store data in a database, display it, or do whatever you like with it here
    // For this example, let's just echo it back to the user

    echo "<h2>Submitted Data:</h2>";
    echo "<p>Name: $name</p>";
    echo "<p>Email: $email</p>";
    echo "<p>Message: $message</p>";
    echo "<p>Gender: $gender</p>";
    echo "<p>Branch: $branch</p>";
    echo "<p>Registration Number: $registrationNumber</p>";
    echo "<p>Location: $location</p>"; 

} else {
    echo "Error: This form should be submitted using the POST method.";
}
?>
