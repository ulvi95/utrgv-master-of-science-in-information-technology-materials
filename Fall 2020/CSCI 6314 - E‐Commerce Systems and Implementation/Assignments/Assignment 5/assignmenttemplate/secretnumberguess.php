<?php

if (!isset($_POST["name"]) || empty(trim($_POST["name"])))
{
    echo    "<div>" .
                "<div class=\"bg-danger text-white\">I do not know what your name is. Let's be friends. :)</div>" .
            "</div>";

    exit();
}

if (!isset($_POST["secretnumber"]) || !is_numeric($_POST["secretnumber"]))
{
    echo    "<div>" .
                "<div class=\"bg-danger text-white\">I do not know what your secret number is. Don't worry, I won't share it. ;)</div>" .
            "</div>";

    exit();
}
else if ($_POST["secretnumber"] != floor($_POST["secretnumber"]) || $_POST["secretnumber"] < 1 || $_POST["secretnumber"] > 100)
{
    echo    "<div>" .
                "<div class=\"bg-warning text-dark\">I do not recognize this complex number. Just need a simple integer between 1 and 100.</div>" .
            "</div>";

    exit();
}

$randomNumber = mt_rand(1, 100);

$difference = abs($_POST["secretnumber"] - $randomNumber);

if ($difference == 0)
    echo    "<div>" .
                "<div class=\"bg-success text-white\">Wow, " . $_POST["name"] . ", I have never met anyone as lucky as you! My secret number was also " . $randomNumber . ".</div>" .
            "</div>";
else if ($difference <= 10)
    echo    "<div>" .
                "<div class=\"guessclose\">Okay, " . $_POST["name"] . ", we were close. My secret number was " . $randomNumber . " (" . $difference . " away).</div>" .
            "</div>";
else if ($difference <= 20)
    echo    "<div>" .
                "<div class=\"guessclose somewhat\">That was a good try, " . $_POST["name"] . ". My secret number was " . $randomNumber . " (" . $difference . " away).</div>" .
            "</div>";
else if ($difference <= 30)
    echo    "<div>" .
                "<div>Hmm, at least we are in the same ballpark, " . $_POST["name"] . "...sort of. My secret number was " . $randomNumber . " (" . $difference . " away).</div>" .
            "</div>";
else if ($difference <= 40)
    echo    "<div>" .
                "<div class=\"guessfar somewhat\">Well, " . $_POST["name"] . ", we are on opposite sides of the bridge. My secret number was " . $randomNumber . " (" . $difference . " away).</div>" .
            "</div>";
else
    echo    "<div>" .
                "<div class=\"guessfar\">Aw shucks, " . $_POST["name"] . ", we are on very different wavelengths. My secret number was " . $randomNumber . " (" . $difference . " away).</div>" .
            "</div>";

?>
