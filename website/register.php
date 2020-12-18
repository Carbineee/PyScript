<?php


    $username = $_GET['username'];
    $password = $_GET['password'];
    $code = $_GET['code'];

    $servername = 'localhost';
    $username = 'root';
    $password = '';
    $dbname = 'hwid';

    $conn = new mysqli($servername, $username, $password, $dbname);

    //Check if code exists and is not used

    $checkSql = "SELECT * FROM codes WHERE code = '" . $code . "'";

    $checkResult = $conn->query($checkSql);

    if ($checkResult->num_rows > 0) {
        // Outputting the rows
        while($row = $checkResult->fetch_assoc())
        {
            
            if ( $row['used'] == 0 ) {
               
                $insertSql = "INSERT INTO hwid (username, password) VALUES ($username, $password)";

                if( $conn->query($insertSql) === TRUE) {
                    echo 'success';
                } else {
                    echo "Error: " . $insertSql . "<br>" . $conn->error;
                }
            }
            else {
                echo 'error:code_used';
            }

        }
    }


?>
