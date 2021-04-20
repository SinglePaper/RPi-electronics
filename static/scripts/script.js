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
    console.log("Direction: Up")
}
function downPress(e) {
    e.preventDefault();
    data["direction"] = 2
    updateData()
    console.log("Direction: Down")
}
function leftPress(e) {
    e.preventDefault();
    data["direction"] = 1
    updateData()
    console.log("Direction: Left")
}
function rightPress(e) {
    e.preventDefault();
    data["direction"] = 3
    updateData()
    console.log("Direction: Right")
}

function resetPress(e) {
    e.preventDefault();
//    console.log("Direction: Up")          God so much spam please oh god please
    data["direction"] = 0
    updateData()
    console.log("Direction: Up")
}

function updateData() {
    sendDirection()
}

function sendDirection() {
    console.clear()
    $.post("receiver", data, function(){
	});
}
