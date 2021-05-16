$(document).ready(function ()
{
    $(".loading").hide();

    $("#passwordvisibilitytoggle").on("mouseover", function ()
    {
        $(this).removeClass("fa-eye-slash");
        $(this).addClass("fa-eye");

        $("input[name=\"password\"]").attr("type", "text");
    }).on("mouseout", function ()
    {
        $(this).removeClass("fa-eye");
        $(this).addClass("fa-eye-slash");

        $("input[name=\"password\"]").attr("type", "password");
    });

    $("button[name=\"removeoldestrowbutton\"]").on("click", function ()
    {
        $("body > div:last-of-type > div:last-of-type > div > div:first-of-type").remove();
    });

    $("button[name=\"submitbutton\"]").on("click", function ()
    {
        $(this).prop("disabled", true);
        $(this).addClass("disabled");

        $(".loading").css({ opacity: 1 });
        $(".loading").show();

        $(".loading").animate({ opacity: 0 }, 1000, function ()
        {
            $("button[name=\"submitbutton\"]").prop("disabled", false);
            $("button[name=\"submitbutton\"]").removeClass("disabled");

            $(".loading").hide();

            let message = "";

            if ($("input[name=\"username\"]").val().trim() === "")
                message = "I wish I knew what your username was.";
            else if ($("input[name=\"password\"]").val() === "")
                message = "You wouldn't trust me with a password?";
            else
                message = "Thanks for inputting your password, " + $("input[name=\"username\"]").val().trim() + ". Hopefully this isn't the same one used to login to your computer.";

            $("body > div:last-of-type > div:last-of-type > div").append("<div>Message at timestamp " + Date.now() + " received: " + message + "</div>");
        });
    });
});
