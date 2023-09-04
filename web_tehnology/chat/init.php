<?php
$pdo = new PDO('sqlite:chat.db');

$pdo->exec('CREATE TABLE messages (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(100)
  message VARCHAR(250)
)');

