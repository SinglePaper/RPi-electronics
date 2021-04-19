<?php
$message = "It works!"
?>
<html>
    <head>
        <title>Charlie Control</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="explanation">
            <h1><?=$message?></h1>
        </div>
        <div class="controls">
            <table>
                <tr>
                    <td></td>
                    <td class="forwards"><button id="forwards" name="forwards">^</button></td>
                    <td></td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
        </div>
    </body>
</html>
