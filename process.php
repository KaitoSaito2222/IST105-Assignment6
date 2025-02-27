<?php
// Get user input from either POST or GET method
$a = $_REQUEST['a'] ?? '';
$b = $_REQUEST['b'] ?? '';
$c = $_REQUEST['c'] ?? '';
$d = $_REQUEST['d'] ?? '';
$e = $_REQUEST['e'] ?? '';

// Function to escape command line arguments
function escapeArgument($arg) {
    return escapeshellarg($arg);
}

// Call the Python script with user input
$command = sprintf(
    'python3 data_management.py %s %s %s %s %s',
    escapeArgument($a),
    escapeArgument($b),
    escapeArgument($c),
    escapeArgument($d),
    escapeArgument($e)
);
$html_output = shell_exec($command);
echo $html_output;
echo "<p><a href='form.php'>Back to input form</a></p>";
?>