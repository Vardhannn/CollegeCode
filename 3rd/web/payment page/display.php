<?php
// Capture the submitted form data
$name = $_POST['name'];
$cardNumber = $_POST['card_number'];
$expiry = $_POST['expiry'];
$cvv = $_POST['cvv'];

// Basic HTML structure to display the details
echo "<h2>Payment Details Summary</h2>";
echo "<p>Name: " . $name . "</p>";
echo "<p>Card Number: " . $cardNumber . "</p>";
echo "<p>Expiry: " . $expiry . "</p>";
echo "<p>CVV: " . $cvv . "</p>";
?>
