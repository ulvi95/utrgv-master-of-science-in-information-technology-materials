$(document).ready(function ()
{
    $(".loading").hide();


    $("#secretnumbervisibilitytoggle").on("click", function ()
    {
        $(this).toggleClass("fa-eye");
        $(this).toggleClass("fa-eye-slash");

        if ($("input[name=\"secretnumber\"]").attr("type") == 'text')
        {
            $("input[name=\"secretnumber\"]").attr("type", "password");
        }
        else if ($("input[name=\"secretnumber\"]").attr("type") == 'password')
        {
            $("input[name=\"secretnumber\"]").attr("type", "text");
        }
    })


    $("button[name=\"submitbutton\"]").on("click", function ()
    {
        $(this).prop("disabled", true);
        $(this).addClass("enabled");
        $(".loading").show();
        $.ajax({
            type: 'POST',
            url: "secretnumberguess.php",
            data: $("form").serialize(),
            success: function(response) {$("#attemptlogs").prepend(response);},
            complete: function()
        {
            $("button[name=\"submitbutton\"]").prop("disabled", false);
            $("button[name=\"submitbutton\"]").removeClass("enabled");
            $(".loading").hide();
        }
        });
    });
    




    $("#clearlastattemptbutton").on("click", function ()
    {
        $("#attemptlogs > div:first-of-type").remove();
    });    

    $("#clearallattemptsbutton").on("click", function ()
    {
        $("#attemptlogs").empty();
    });
});
