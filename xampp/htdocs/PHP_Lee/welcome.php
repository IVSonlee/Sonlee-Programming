<?php
session_start();   // must be the very first thing, before any HTML

$maxEntries = 5;

// Create the list once
if (!isset($_SESSION['entries'])) {
    $_SESSION['entries'] = [];
}

// Save the new submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['entries'][] = [
        'fullname'       => $_POST['fullname']       ?? '',
        'nickname'       => $_POST['nickname']       ?? '',
        'address'        => $_POST['address']        ?? '',
        'second_course'  => $_POST['2nd_course']     ?? '',
        'phone_brand'    => $_POST['phone_brand']    ?? '',
        'music_genre'    => $_POST['music_genre']    ?? '',
        'fave_food'      => $_POST['fave_food']      ?? '',
        'fave_classmate' => $_POST['fave_classmate'] ?? '',
    ];

    // If more than 5, remove the oldest (first) entry.
    // array_shift() removes the first item and re-numbers the rest,
    // so the 2nd submit becomes the 1st.
    while (count($_SESSION['entries']) > $maxEntries) {
        array_shift($_SESSION['entries']);
    }
}
?>
<!DOCTYPE html>
<html lang="en-US">
    <head>
        <link rel="stylesheet" href="CSS/welcome.css">
    </head>
    <body>
        <div>
            <?php foreach ($_SESSION['entries'] as $i => $entry): ?>
                <h3>Submission <?php echo $i + 1; ?></h3>
                <p>Fullname: <?php echo htmlspecialchars($entry['fullname']); ?></p>
                <p>Nickname: <?php echo htmlspecialchars($entry['nickname']); ?></p>
                <p>Address: <?php echo htmlspecialchars($entry['address']); ?></p>
                <p>2nd Preferred Course: <?php echo htmlspecialchars($entry['second_course']); ?></p>
                <p>Favorite Phone Brand: <?php echo htmlspecialchars($entry['phone_brand']); ?></p>
                <p>Favorite Music Genre: <?php echo htmlspecialchars($entry['music_genre']); ?></p>
                <p>Least Favorite Food: <?php echo htmlspecialchars($entry['fave_food']); ?></p>
                <p>Least Favorite Classmate: <?php echo htmlspecialchars($entry['fave_classmate']); ?></p>
                <hr>
            <?php endforeach; ?>
        </div>
    </body>
</html>