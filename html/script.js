function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


direction = 0

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
    console.log("Direction: Up")
    direction = 0                       // Maybe add support for making this a speed up button
    sendDirection()
}
function downPress(e) {
    e.preventDefault();
    console.log("Direction: Down")
    direction = 2
    sendDirection()
}
function leftPress(e) {
    e.preventDefault();
    console.log("Direction: Left")
    direction = 1
    sendDirection()
}
function rightPress(e) {
    e.preventDefault();
    console.log("Direction: Right")
    direction = 3
    sendDirection()
}

function resetPress(e) {
    e.preventDefault();
//    console.log("Direction: Up")          God so much spam please oh god please
    direction = 0
    sendDirection()
}

function sendDirection() {
    // Code to send variable to python
}
