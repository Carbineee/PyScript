<?php

    $servername = 'localhost';
    $username = 'root';
    $password = '';
    $dbname = 'hwid';

    $conn = new mysqli($servername, $username, $password, $dbname);

    $sql = "SELECT * FROM hwid WHERE id=1";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Outputting the rows
        while($row = $result->fetch_assoc())
        {
            if($_GET['hwid'] == $row['hardware']) {
                echo 'authed';
            }
            else {
                die('error');
            }

        }
    }
?>
