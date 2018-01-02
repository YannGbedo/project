<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link href="css/style.css" rel="stylesheet">
        <script src="jquery/jquery.js"></script>
        <script src="js/script.js"></script>
        <script src="bootstrap/js/jquery.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
        <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
        <link rel="icon" type="image/png" href="img/logo.png" />
        <title>hids</title>
    </head>
    <body>
        <?php
            require("php/connect.php");
        ?>
        <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header" id="navbar">
                <a class="navbar-brand" href="index.php">HIDS</a>
            </div>
            <ul class="nav navbar-nav">
                <li><a href="index.php?alerte">ALERTE</a></li>
                <li><a href="index.php?actual">ACTUAL</a></li>
            </ul>
    </body>
</html>