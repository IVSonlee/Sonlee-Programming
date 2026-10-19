<!DOCTYPE html>
<html lang="en-US">
    <head>
        <link rel="stylesheet" href="CSS/signin.css">
        <title>PHP Account - Sign in</title>
        <style>
            
        </style>
    </head>
    <body>
        <form id="signin_form" action="welcome.php" method="POST">
            <table>
                <tr>
                    <td><label for="fullname">Fullname</label></td>
                    <td><input type="text" name="fullname"></td>
                </tr>
                <tr>
                    <td><label for="nickname">Nickname</label></td>
                    <td><input type="text" name="nickname"></td>
                </tr>
                <tr>
                    <td><label for="address">Address</label></td>
                    <td><input type="text" name="address"></td>
                </tr>
                <tr>
                    <td><label for="2nd_course">2nd Preferred Course</label></td>
                    <td><input type="text" name="2nd_course"></td>
                </tr>
                <tr>
                    <td><label for="phone_brand">Favorite Phone Brand</label></td>
                    <td><input type="text" name="phone_brand"></td>
                </tr>
                <tr>
                    <td><label for="music_genre">Favorite Music Genre</label></td>
                    <td><input type="text" name="music_genre"></td>
                </tr>
                <tr>
                    <td><label for="fave_food">Least Favorite Food</label></td>
                    <td><input type="text" name="fave_food"></td>
                </tr>
                <tr>
                    <td><label for="fave_classmate">Least Favorite Classmate</label></td>
                    <td><input type="text" name="fave_classmate"></td>
                </tr>
                <tr>
                    <td  colspan="2"><input id="submit" type="submit"></td>
                </tr>
            </table>
            
            
            
        </form>
    </body>
</html>