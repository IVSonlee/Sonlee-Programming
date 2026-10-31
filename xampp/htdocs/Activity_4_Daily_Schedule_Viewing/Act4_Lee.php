<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);

$selectedDay = '';
$dayNote     = '';
$error       = '';
$rows        = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit'])) {
    $selectedDay = trim($_POST['day'] ?? '');

    switch ($selectedDay) {
        case 'Monday':
        case 'Wednesday':
            $dayNote = 'No classes today. Daily routine:';
            break;
        case 'Tuesday':
        case 'Thursday':
        case 'Saturday':
            $dayNote = 'Class day (see regcard):';
            break;
        case 'Friday':
            $dayNote = 'No classes today. Daily routine:';
            break;
        case 'Sunday':
            $dayNote = 'Rest day. Daily routine:';
            break;
        default:
            $error       = 'Invalid day selected.';
            $selectedDay = '';
            break;
    }

    // Fetch that day's entries from the database.
    if ($selectedDay !== '') {
        try {
            $conn = new mysqli('localhost', 'root', '', 'class_schedule');
            $conn->set_charset('utf8mb4');

            $stmt = $conn->prepare(
                'SELECT start_time, end_time, subject_code, activity, room, entry_type
                 FROM schedule
                 WHERE day_name = ?
                 ORDER BY start_time'
            );
            $stmt->bind_param('s', $selectedDay);
            $stmt->execute();
            $rows = $stmt->get_result()->fetch_all(MYSQLI_ASSOC);

            $stmt->close();
            $conn->close();
        } catch (mysqli_sql_exception $e) {
            $error = 'Could not load the schedule. Make sure XAMPP MySQL is running and schedule.sql was imported.';
        }
    }
}

function fmtTime($t) {
    return date('g:i A', strtotime($t));
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="CSS/schedule.css">
    <title>Weekly Class Schedule</title>
</head>
<body>
    <h2>Weekly Class Schedule</h2>

    <form action="" method="post">
        <label for="day">Select a day:</label>
        <select name="day" id="day" required>
            <option value="">-- Choose a Day --</option>
            <?php
            foreach (['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] as $d) {
                $sel = ($selectedDay === $d) ? ' selected' : '';
                echo "<option value=\"$d\"$sel>$d</option>\n";
            }
            ?>
        </select>
        <input type="submit" name="submit" value="View Schedule">
    </form>

    <?php if ($error !== ''): ?>
        <p class="error"><?= htmlspecialchars($error) ?></p>
    <?php elseif ($selectedDay !== ''): ?>
        <h3>Schedule for <?= htmlspecialchars($selectedDay) ?></h3>
        <p class="note"><?= htmlspecialchars($dayNote) ?></p>

        <?php if (count($rows) === 0): ?>
            <p>No entries found for this day.</p>
        <?php else: ?>
            <table>
                <tr><th>Time</th><th>Activity</th><th>Room / Place</th><th>Type</th></tr>
                <?php foreach ($rows as $r): ?>
                    <tr class="<?= $r['entry_type'] === 'Class' ? 'class-row' : 'routine-row' ?>">
                        <td><?= fmtTime($r['start_time']) ?> - <?= fmtTime($r['end_time']) ?></td>
                        <td>
                            <?= $r['subject_code'] ? htmlspecialchars($r['subject_code']) . ' - ' : '' ?>
                            <?= htmlspecialchars($r['activity']) ?>
                        </td>
                        <td><?= htmlspecialchars($r['room'] ?? '') ?></td>
                        <td><?= htmlspecialchars($r['entry_type']) ?></td>
                    </tr>
                <?php endforeach; ?>
            </table>
        <?php endif; ?>
    <?php endif; ?>

    <div class="footer">
        <h2>Lee Iverson Richmond</h2>
        <h3>BSIT 4 Y1-4</h3>
    </div>
</body>
</html>
