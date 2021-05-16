<?php
require_once 'db_connect.php';
// Function to create a secure session (use of cookies prevents attacks involving passing session IDs thru URLs)
function secure_session_start()
{
    $session_name = 'secure_session_id'; // custom session name
    $secure = true; // HTTPS session
    $httpsonly = true; // access a cookie thru HTTPS protocol only
    if (ini_set('session.use_only_cookies', 1) == false)
    { // check if cookies can be used
        header("Location: ../error.php?err=Cannot exclusively use cookies (ini_set)");
        exit(); // exit if unable to use cookies
        
    }
    $cookieParams = session_get_cookie_params(); // get parameters of a cookie
    session_set_cookie_params($cookieParams["lifetime"], $cookieParams["path"], $cookieParams["domain"], $secure, $httpsonly); // keep same lifetime, path, and domain
    session_name($session_name); // set the session name
    session_start(); // Start the session
    session_regenerate_id(); // regenerate session id to prevent session hijacking
    
}
// Function to login
function login($username, $password, $mysqli)
{ // $mysqli is the db connection
    if ($stmt = $mysqli->prepare("SELECT pid, pname, password FROM webuser where pname = ? LIMIT 1"))
    {
        $stmt->bind_param('s', $username); // pass param to mysqli statement
        $stmt->execute(); // execute mysqli
        $stmt->store_result(); // store complete result including $stmt->num_rows
        $stmt->bind_result($db_pid, $db_pname, $db_password); // bind values retrieved from the database
        $stmt->fetch();
        if ($stmt->num_rows == 1)
        { // only one row is expected
            if (password_verify($password, $db_password))
            {
                $user_browser = $_SERVER['HTTP_USER_AGENT']; // get browser type -- to be able to detect
                $_SESSION['user_id'] = $db_pid; // browser change (session hijacking)
                $_SESSION['username'] = $username;
                $_SESSION['login_string'] = hash('sha512', $db_password . $user_browser); //use Secure Hash Alg
                return true; //to hash password + browser type
                
            }
            else
            {
                return false;
            } // bad password
            
        }
        else
        {
            return false;
        } // number of rows != 1
        
    }
    else
    {
        return false;
    } // mysqli statement error
    
}
// Function to check if user is logged in
function login_check($mysqli)
{ // $mysqli is the db connection
    if (isset($_SESSION['user_id'], $_SESSION['username'], $_SESSION['login_string']))
    { // check if each of
        $user_id = $_SESSION['user_id']; // these values is set (no null)
        $username = $_SESSION['username'];
        $login_string = $_SESSION['login_string'];
        $user_browser = $_SERVER['HTTP_USER_AGENT'];
        if ($stmt = $mysqli->prepare("SELECT password FROM webuser WHERE pid = ? LIMIT 1"))
        {
            $stmt->bind_param('i', $user_id);
            $stmt->execute(); //get the password for the user of this session
            $stmt->store_result();
            $stmt->bind_result($password);
            $stmt->fetch();
            if ($stmt->num_rows == 1)
            {
                $login_check = hash('sha512', $password . $user_browser);
                if (hash_equals($login_check, $login_string))
                { // session is not hijacked if logins match
                    return true; // if logins match, then user is logged in
                    
                }
                else
                {
                    return false;
                } // login check failed
                
            }
            else
            {
                return false;
            } // number of rows != 1
            
        }
        else
        {
            return false;
        } // mysqli statement error
        
    }
    else
    {
        return false;
    } // isset error?
    
}
?>
