<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Create Your Own Sign Key (JKS)</h1>
    <h2>Instructions</h2>
    <p>Follow these steps to create your own signing key (JKS) using Termux:</p>
    <ol>
        <li>Open Termux and run the following command:</li>
        <pre><code>pkg install git && pkg update && pkg install python && git clone https://github.com/SuperKulot/SKGENKEY.git && cd SKGENKEY && pip install -r requirements.txt && apt install openjdk-17 && python generate_keystore.py</code></pre>
    </ol>
    <h2>Credentials</h2>
    <ul>
        <li>Username: <strong>SuperKulot</strong></li>
        <li>Password: <strong>SuperKulot</strong></li>
    </ul>
    <h2>Run Script</h2>
    <p>To run the script, use the following command:</p>
    <pre><code>python generate_keystore.py</code></pre>
</body>
</html>
