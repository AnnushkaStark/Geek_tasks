<?php
$pdo = new PDO('sqlite:chat.db');

if (isset($_POST['username']) && !empty($_POST['username']) && isset($_POST['message']) && !empty($_POST['message'])) {
    $username = strip_tags($_POST['username']);
    $message = strip_tags($_POST['message']);

    $statement = $pdo->prepare(
        'INSERT INTO messages (username, message) VALUES (?, ?)'
    );
    $statement->execute([$username, $message]);

    $result = [
        'status' => 'ok'
    ];
    echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);

    die();
}

$statement = $pdo->prepare(
    'SELECT * FROM messages ORDER BY id desc LIMIT 10;'
);

$statement->execute();

$messages = $statement->fetchAll(PDO::FETCH_ASSOC);

$result = [
    'status' => 'ok',
    'messages' => $messages
];

echo json_encode($result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
