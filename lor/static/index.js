$(function () {
    $("#showVideo").click(function () {
        var youtubeLink = $('#ytLink').val();
        var idRegex = /^.*youtube.com\/(.*)$/;
        var ytSuffix;
        try {
            ytSuffix = youtubeLink.match(idRegex)[1]; // Parse YouTube link
        }
        catch (e) {
            // If regex is unsuccessful (e.g not YouTube link), then show error
            $("#error").html("Invalid YouTube Link. Format is https://www.youtube.com/watch?v=videoID");
            setTimeout(function () {
                $('#error').fadeOut();
            }, 2000);
            return; // Prevent redirection
        }

        window.location = ytSuffix;
    });
});
