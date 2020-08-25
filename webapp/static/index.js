var web_app_token = "Not set yet";
//TODO : change to app name and secret
var username = "Alex";
var password = "test";

$.ajax({
    type: "POST",
    url: "/api/tokens",
    username: username,
    password: password,
    data: {},
    success: function (msg) {
        web_app_token = msg["token"];
    }
});

if(is_touch_device()){
    $('#console').append("<p>mobile</p>");
    $('.ctrl_btn').on('touchstart', function () {
        $(this).removeClass("mobileHoverFix");
        var id = $(this).attr('id');
        console.log("Mouse down on: " + id);
        sendEvent("mouse_down", id);
    });

    $('.ctrl_btn').on('touchend', function () {
        $(this).addClass("mobileHoverFix");
        var id = $(this).attr('id');
        console.log("Mouse up on: " + id);
        sendEvent("mouse_up", id);
    });
}else{
    $('#console').append("<p>desktop</p>");
    $('.ctrl_btn').mousedown(function () {
        var id = $(this).attr('id');
        console.log("Mouse down on: " + id);
        sendEvent("mouse_down", id);
    });

    $('.ctrl_btn').mouseup(function () {
        var id = $(this).attr('id');
        console.log("Mouse up on: " + id);
        sendEvent("mouse_up", id);
    });    
}


function is_touch_device() {
    var is_touch = 'ontouchstart' in window
    console.log("Is touch device " + is_touch);
    return is_touch;
}

function sendEvent(event, id) {
    console.log("Sending event" + event + " for button " + id);

    var key = id.substr(4, id.length);
    var is_down = event == "mouse_down";
    var json =
        {
            'key': key,
            'is_down': is_down
        };

    $.ajax({
        type: "POST",
        url: "/api/drive",
        headers: {
            "Authorization": "Bearer " + web_app_token
        },
        data: JSON.stringify(json),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (msg) {
            $('#console').append(msg)
        }
})
    ;
}
