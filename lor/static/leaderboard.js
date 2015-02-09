var ytAPIKey = 'change_this_key'; // Insert YT Data API browser key


$(function () {
    $("img").each(function () {
        var video_id = $(this).parent().attr("id");
        var responseObject = send_yt_request(video_id);
        var imgsrc = responseObject.items[0].snippet.thumbnails.default.url;
        var vidDescription = responseObject.items[0].snippet.title;
        $(this).attr("src", imgsrc); // Update thumbnail image
        $(this).next().next().html(vidDescription); // Update description span element
    });
});
function send_yt_request (video_id) {
    var responseObj;
    var requestPath = "https://www.googleapis.com/youtube/v3/videos?id="+ video_id +"&key="+ ytAPIKey +"&part=snippet,statistics";
    $.ajax({
        type: "GET",
        url: requestPath,
        async: false
    })
    .done(function( responseJSON ) {
        console.log(responseJSON);
        responseObj = responseJSON;
    });
    return responseObj;
    // Construct the request, get data, and return parsed response
}
