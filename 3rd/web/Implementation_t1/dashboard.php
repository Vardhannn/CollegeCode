


<head>
    <style>
        .user-details-form {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f8f8f8;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: left; /* Align the whole form to the left */
            display: flex;
            flex-direction: column;
            align-items: left;
        }

        h2 {
            color: #333;
            text-align: center; /* Center the heading within the form */
        }

        .details-group {
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        label {
            font-weight: bold;
            width: 180px; /* Fixed width for labels */
        }

        span {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            flex: 1; /* Take the remaining space */
            margin-left: 10px; /* Add some space between label and value */
        }

        input {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            
        }
    </style>
</head>
<div class="user-details-form">
    <h2>Welcome, <?php echo $row['firstname'] . ' ' . $row['lastname']; ?>!</h2>

    <div class="details-group">
        <label for="regNumber">Registration Number:</label>
        <span id="regNumber"><?php echo $row['regNumber']; ?></span>
    </div>

    <div class="details-group">
        <label for="email">Email:</label>
        <span id="email"><?php echo $row['Email']; ?></span>
    </div>

    <div class="details-group">
        <label for="contact">Contact:</label>
        <span id="contact"><?php echo $row['contact']; ?></span>
    </div>

    <div class="details-group">
        <label for="Birth">Date of Birth:</label>
        <span id="age"><?php echo $row['Birth']; ?></span>
    </div>

    <div class="details-group">
        <label for="gender">Gender:</label>
        <span id="gender"><?php echo $row['gender']; ?></span>
    </div>

    <div class="details-group">
        <label for="address">Address:</label>
        <span id="address"><?php echo $row['address']; ?></span>
    </div>

    <div class="details-group">
        <label for="degree">Degree:</label>
        <span id="degree"><?php echo $row['Degree']; ?></span>
    </div>

    <a href="login_page.html"><input type = "button" name = "back" value = "Back to Login">
    </a>


</div>