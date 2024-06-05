<!DOCTYPE html>
<html>
<head>
  <title>Image Upload</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      background-color: #f5f5f5;
    }
    
    h1 {
      text-align: center;
      color: #333;
      margin-bottom: 20px;
    }
    
    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 20px;
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 5px;
    }
    
    form label {
      margin-bottom: 5px;
      color: #333;
    }
    
    #image-container {
      text-align: center;
    }
    
    #uploaded-image {
      width: 300px;
      max-width: 100%;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      padding: 5px;
      border-radius: 5px;
    }
    
    #view-button {
      padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
    }

    #fileToUpload{

    }

    #upload{
        padding: 10px 20px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
    }

    #upload:hover{
        background-color: #3e8e41;
    }
    
    #view-button:hover {
      background-color: #3e8e41;
    }
    
    .success-message {
      color: green;
      text-align: center;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>Upload and View Image</h1>
  <form action="upload.php" method="post" enctype="multipart/form-data">
    <label for="fileToUpload">Select image to upload:</label><br>
    <input type="file" name="fileToUpload" id="fileToUpload">
    <br><br>
    <input type="submit" value="Upload Image" name="submit" id = "upload">
  </form>
  <?php 
    if(isset($_GET['success'])) {
      echo "<p>Image uploaded successfully!</p>";
    }
  ?>
  <div id="image-container">
    <img id="uploaded-image" src="" alt="Uploaded Image">
    <button id="view-button">View Image</button>
  </div>

  <script>
  document.getElementById('view-button').addEventListener('click', function() {
    document.getElementById('uploaded-image').src = "uploads/<?php echo (isset($_GET['image']) ? $_GET['image'] : ""); ?>";
  });
  </script>
</body>
</html>
