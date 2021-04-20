function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var data = {"direction": 0, "speed": 1}

up_button = document.getElementById("up");
down_button = document.getElementById("down");
left_button = document.getElementById("left");
right_button = document.getElementById("right");

// Events for up button
up_button.addEventListener("mousedown", upPress, false);
up_button.addEventListener("mouseup", resetPress, false);
up_button.addEventListener("mouseleave", resetPress, false);

// Events for down button
down_button.addEventListener("mousedown", downPress, false);
down_button.addEventListener("mouseup", resetPress, false);
down_button.addEventListener("mouseleave", resetPress, false);

// Events for left button
left_button.addEventListener("mousedown", leftPress, false);
left_button.addEventListener("mouseup", resetPress, false);
left_button.addEventListener("mouseleave", resetPress, false);

// Events for right button
right_button.addEventListener("mousedown", rightPress, false);
right_button.addEventListener("mouseup", resetPress, false);
right_button.addEventListener("mouseleave", resetPress, false);

function upPress(e) {
    e.preventDefault();
    data["direction"] = 0                       // Maybe add support for making this a speed up button
    updateData()
}
function downPress(e) {
    e.preventDefault();
    data["direction"] = 2
    updateData()
}
function leftPress(e) {
    e.preventDefault();
    data["direction"] = 1
    updateData()
}
function rightPress(e) {
    e.preventDefault();
    data["direction"] = 3
    updateData()
}

function resetPress(e) {
    e.preventDefault();
    data["direction"] = 0
    updateData()
}

function updateData() {
    sendDirection()
}

function sendDirection() {
    console.clear()
    console.log(data)
    $.ajax({
        type: "POST",
        url: "{{ url_for('get_post_json') }}",
        contentType: "application/json",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(err) {
            console.log(err);
        }
    });
}
