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
    console.log("Button: Up")
    direction = 0                       // Maybe add support for making this a speed up button
}
function downPress(e) {
    e.preventDefault();
    console.log("Button: Down")
    direction = 2
}
function leftPress(e) {
    e.preventDefault();
    console.log("Button: Left")
    direction = 1
}
function rightPress(e) {
    e.preventDefault();
    console.log("Button: Right")
    direction = 3
}

function resetPress(e) {
    e.preventDefault();
    direction = 0
}

async function updateDirection() {
    switch (direction) {
        case 0:
            console.log("Forward")
            break
        case 1:
            console.log("Left")
            break
        case 2:
            console.log("Backward")
            break
        case 3:
            console.log("Right")
    }
    await sleep(500);
}

while (true) {updateDirection();}