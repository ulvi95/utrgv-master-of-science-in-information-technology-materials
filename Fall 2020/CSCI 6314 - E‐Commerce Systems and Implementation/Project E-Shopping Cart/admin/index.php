<html lang="en">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="styles.css">
      <link rel="stylesheet" href="/scripts/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/all.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/font-awesome.min.css">
      <title>CSCI 6314 E-Shopping Cart</title>
   </head>
   <body>
         <div id="forAdminsOnly" class="offset-3 col-xl-6 col-lg-6 col-md-6 col-sm-6 col-xs-6 col-6 d-flex justify-content-center">
            <form action="authenticate.php" method="post">
               <div class="form-group">
                  <label for="usernameInput">Username</label>
                  <input type="text" class="form-control" name="usernameInput" id="usernameInput" aria-describedby="username" placeholder="Enter the username">
                  <small id="usernameMutedText" class="form-text text-muted">The fields are only for administrators.</small>
               </div>
               <div class="form-group">
                  <label for="passwordInput">Password</label>
                  <input type="password" class="form-control" name="passwordInput" id="passwordInput" aria-describedby="password" placeholder="Enter the password">
               </div>
               <div class="form-group">
                  <input id="submitButton" name="submitButton" type="submit" value="Enter" class="btn btn-primary">
               </div>
            </form>
         </div>
    </body>
</html>

