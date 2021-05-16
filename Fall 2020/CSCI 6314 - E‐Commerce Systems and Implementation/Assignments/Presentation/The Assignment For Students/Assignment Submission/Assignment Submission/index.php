<!DOCTYPE html>
<html>
    <head></head>

    <body>
        <?php
            function test_input($data)
            {
                $data = trim($data);
                $data = stripslashes($data);
                $data = htmlspecialchars($data);

                return $data;
            }

            $server = "localhost";
            $database = "temp";
            $username = "root";
            $password = "";

            $conn = new mysqli($server, $username, $password, $database);

            if ($conn->connect_error)
                die("Connection failed: " . $conn->connect_error);

            $firstnameerror = "";
            $lastnameerror = "";
            $gendererror = "";
            $colorerror = "";
            $ratingerror = "";

            if ($_SERVER["REQUEST_METHOD"] == "POST")
            {
                $firstname = test_input($_POST["firstname"]);

                if (empty($firstname))
                    $firstnameerror = "First name is required";

                $lastname = test_input($_POST["lastname"]);

                if (empty($lastname))
                    $lastnameerror = "Last name is required";

                if (!isset($_POST["gender"]))
                    $gendererror = "Gender is required";

                $color = test_input($_POST["color"]);

                if (empty($color))
                    $colorerror = "Color is required";

                $rating = test_input($_POST["rating"]);

                if (empty($rating))
                    $ratingerror = "Rating is required";
                else if (!is_numeric($rating) || $rating < 1 || $rating > 10)
                    $ratingerror = "Rating must be between 1 and 10";

                if (empty($firstnameerror) && empty($lastnameerror) && empty($gendererror) && empty($colorerror) && empty($ratingerror))
                {
                    $query = "INSERT INTO formsubmit (firstname, lastname, gender, color, rating) VALUES (?, ?, ?, ?, ?)";

                    $statement = $conn->prepare($query);

                    $statement->bind_param("ssssi", $firstname, $lastname, $_POST["gender"], $color, $rating);

                    $statement->execute();

                    $statement->close();

                    echo "Form submitted successfully!";
                    echo "<br />";
                    echo "<br />";
                    echo "First Name: " . $firstname;
                    echo "<br />";
                    echo "Last Name: " . $lastname;
                    echo "<br />";
                    echo "Gender: " . $_POST["gender"];
                    echo "<br />";
                    echo "Color: " . $color;
                    echo "<br />";
                    echo "Rating: " . $rating;
                }
            }
        ?>

        <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]) ?>">
            <fieldset>
                <legend>Personalia:</legend>

                <label for="firstname">First name:</label>
                <input type="text" id="firstname" name="firstname" />
                <?php echo $firstnameerror; ?>

                <br />
                <br />

                <label for="lastname">Last name:</label>
                <input type="text" id="lastname" name="lastname" />
                <?php echo $lastnameerror; ?>

                <br />
                <br />

                <input type="radio" id="male" name="gender" value="Male" />
                <label for="male">Male</label>

                <br />

                <input type="radio" id="female" name="gender" value="Female" />
                <label for="female">Female</label>

                <br />

                <input type="radio" id="other" name="gender" value="Other" />
                <label for="other">Other</label>

                <br />

                <?php echo $gendererror; ?>
            </fieldset>

            <br />
            <br />

            <label for="color">Choose a color:</label>

            <select id="color" name="color">
                <option value=""></option>
                <option value="Red">Red</option>
                <option value="Green">Green</option>
                <option value="Blue">Blue</option>
            </select>

            <br />
            <br />

            <label for="rating">Rating (between 1 and 10):</label>
            <input type="number" id="rating" name="rating" min="1" max="10" />
            <?php echo $ratingerror; ?>

            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
