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
        <div class="loading bg-dark text-light text-center">Loading...please wait.</div>

        <div>
            <div>
                <form>
                    <div>
                        <div>
                            <h4>Name</h4>
                        </div>

                        <div class="field-expand">
                            <input type="text" class="form-control" name="name" />
                        </div>
                    </div>

                    <div>
                        <div>
                            <h4>Secret Number</h4>
                        </div>

                        <div>
                            <span class="fas fa-eye-slash" id="secretnumbervisibilitytoggle"></span>
                        </div>

                        <div class="field-expand">
                            <input type="password" class="form-control" name="secretnumber" />
                        </div>
                    </div>

                    <div>
                        <p class="form-text text-muted">Guess the secret number between 1 and 100. You might win the lottery.</p>
                    </div>

                    <div>
                        <div class="field-expand">
                            <button type="button" class="btn btn-primary btn-lg" name="submitbutton">Submit</button>
                        </div>
                    </div>
                </form>
            </div>

            <div>
                <div class="text-center">
                    <button type="button" class="btn btn-warning" id="clearlastattemptbutton">Clear Last Attempt</button>
                    <button type="button" class="btn btn-danger" id="clearallattemptsbutton">Clear All Attempts</button>
                </div>

                <div id="attemptlogs"></div>
            </div>
        </div>
    </body>
</html>
