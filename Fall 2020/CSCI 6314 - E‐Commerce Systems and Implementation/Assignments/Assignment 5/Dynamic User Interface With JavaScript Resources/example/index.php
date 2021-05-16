<!DOCTYPE html>
<html>
    <head>
        <link href="lib/bootstrap/dist/css/bootstrap.min.css?v=<?php echo filemtime("lib/bootstrap/dist/css/bootstrap.min.css"); ?>" rel="stylesheet" type="text/css" />
        <link href="lib/font-awesome/css/all.min.css?v=<?php echo filemtime("lib/font-awesome/css/all.min.css"); ?>" rel="stylesheet" type="text/css" />
        <link href="index.css?v=<?php echo filemtime("index.css"); ?>" rel="stylesheet" type="text/css" />

        <script src="lib/jquery/jquery.min.js?v=<?php echo filemtime("lib/jquery/jquery.min.js"); ?>" type="text/javascript"></script>
        <script src="index.js?v=<?php echo filemtime("index.js"); ?>" type="text/javascript"></script>

        <title>Dynamic User Interface With JavaScript</title>
    </head>

    <body>
        <div class="loading bg-dark text-light text-center fixed-top">Loading...please wait.</div>

        <div>
            <div>
                <form>
                    <div>
                        <div>
                            <h4>Username</h4>
                        </div>

                        <div class="field-expand">
                            <input type="text" class="form-control" name="username" />
                        </div>
                    </div>

                    <div>
                        <div>
                            <h4>Password</h4>
                        </div>

                        <div>
                            <span class="fas fa-eye-slash" id="passwordvisibilitytoggle"></span>
                        </div>

                        <div class="field-expand">
                            <input type="password" class="form-control" name="password" />
                        </div>
                    </div>

                    <div>
                        <div class="field-expand">
                            <button type="button" class="btn btn-outline-danger btn-lg" name="removeoldestrowbutton">Remove Oldest Row</button>
                        </div>
                    </div>

                    <div>
                        <div class="field-expand">
                            <button type="button" class="btn btn-primary btn-lg" name="submitbutton">Submit</button>
                        </div>
                    </div>
                </form>
            </div>

            <div>
                <div></div>
            </div>
        </div>
    </body>
</html>
