<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Input Form</title>
</head>
<body>
    <h2>Welcome to the Data management web application</h2>
    <form action="process.php" method="POST">
        <div>
            <label for="a">Number a:</label>
            <input type="number" id="a" name="a" required/>
        </div>
        <div>
            <label for="b">Number b:</label>
            <input type="number" id="b" name="b" required/>
        </div>
        <div>
            <label for="c">Number c:</label>
            <input type="number" id="c" name="c" required/>
        </div>
        <div>
            <label for="d">Number d:</label>
            <input type="number" id="d" name="d" required/>
        </div>
        <div>
            <label for="e">Number e:</label>
            <input type="number" id="e" name="e" required/>
        </div>
        <button type="submit">Submit</button>
    </form>
</body>
</html>