<?php

require 'db.php';

function opt_param($key)
{
    return isset($_POST[$key]) ? $_POST[$key] : null;
}

print_r($_POST);

$first_name = $_POST["first_name"];
$last_name = $_POST["last_name"];
$email = $_POST["email"];
$quality = intval($_POST["quality"]);
$like_service_speed = opt_param("like-service-speed") == "on";
$like_interface = opt_param("like-interface") == "on";
$like_assortment = opt_param("like-assortment") == "on";
$comment = opt_param("comment");

DB_createFeedback(
    $mysqli,
    $first_name,
    $last_name,
    $email,
    $quality,
    $like_service_speed,
    $like_interface,
    $like_assortment,
    $comment
);

// Redirect to feedback-success
header("Location: feedback-success.html");
