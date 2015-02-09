window.loopCount = 0;

var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

//  This function creates an <iframe> (and YouTube player)
//  after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
player = new YT.Player('player', {
  height: '390',
  width: '640',
  videoId: videoIdPassed,
  events: {
    'onReady': onPlayerReady,
    'onStateChange': onPlayerStateChange
  }
});
}

// The API will call this function when the video player is ready.
function onPlayerReady(event) {
    event.target.playVideo();
}

//  The API calls this function when the player's state changes.
//  The function indicates that when playing a video (state=1),
//  the player should play for six seconds and then stop.
function onPlayerStateChange(event) {
    console.log("New State.");
    console.log(event.data);
    if (event.data == YT.PlayerState.ENDED) {
        // Replay it
        player.seekTo(0);
        player.playVideo();
        updateLoopCount();
    }
}
function updateLoopCount() {
    // Triggered whenever the video loops
    // Increment loop count and update counter
    loopCount++;
    $("#loopNum").text(loopCount);
    // Send loop number to server
    $.ajax({
        type: "POST",
        url: "/api/loopcount",
        data: { videoid: videoIdPassed, videoloopcount: loopCount }
    })
    .done(function( global_loop_num ) {
        $("#globalLoopNum").text( global_loop_num );
    });
}

$(function () {
    $("#globalLoopNum").text( initGlobalLoops );
});
