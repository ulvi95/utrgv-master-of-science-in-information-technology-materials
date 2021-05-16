<?php
require_once __DIR__ . '/../required/db_connect.php';
?>
<html>
    <head>
        <title>Team Project</title>
        <link rel="stylesheet" type="text/css" href="prjct.css"/>
    </head>
    <body>
        <div id="Header">
            <h1>Monitoring System</h1>
        </div>
        <div id="body">
            <h3>Login</h3>
            <form id="form1" method="post" action="">
                <div>
                    <label for="usernm">Username: </label>
                    <input type="text" name="usernm" id="usernm" required><br><br>
                </div>
                <div>
                    <label for="psswrd">Password: </label>
                    <input type="password" name="psswrd" id="psswrd" required><br><br>
                </div>
                <button id="sub" type="Submit">Submit</button>
            </form>
        </div>
        <div id="check">
            <?php
            if(isset($_POST['usernm']) and isset($_POST['psswrd'])){
                $uname=$_POST['usernm'];
                $passwrd=$_POST['psswrd'];
    
                if($query = $mysqli->prepare("SELECT * FROM Users WHERE pname='$uname'")){
                     $query->execute();
                    $query->bind_result($username,$password);
                    $count=0;
                    while($query->fetch()){
                        $count=$count+1;
                    }
                    if ($count == 1){
                        if(password_verify($passwrd,$password)){
                            $query->close();
                            $id='9';
                            date_default_timezone_set("America/Chicago");
                            $date=date("Y-m-d H:i:s");
                            $stmt=$mysqli->prepare("INSERT INTO TransactionalLogs(TimestampInfo,MessageID,DataInformation) VALUES(?,?,?)");
                            $stmt->bind_param('sss',$date,$id,$uname);
                            $stmt->execute();
                            $stmt->close();
                            echo "<script type='text/javascript'>alert('Login Credentials verified')</script>";
                            echo "<script> window.location.assign('welcome.php');</script>";
                         }
                        else{
                        //echo "Login Credentials verified";
                        echo "<script type='text/javascript'>alert('Login Credentials do not match')</script>";
                
                        }
                    }
                    else{
                    echo "<script type='text/javascript'>alert('Invalid Login Credentials')</script>";
                    //echo "Invalid Login Credentials";
                    }
                }
                else{
                    echo "Error in if 2";
                }
            }
            ?>
        </div>
    </body>
</html>