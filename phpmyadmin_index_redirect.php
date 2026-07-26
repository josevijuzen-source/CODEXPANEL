<?php
/**
 * phpMyAdmin Access Control - Direct Access Redirect
 * 
 * This file should be placed at /usr/local/CodexCP/public/phpmyadmin/index.php
 * to replace the default phpMyAdmin index.php and redirect unauthenticated users
 * to the CodexPanel login page.
 */

// Check if user is logged into CodexPanel
session_start();
if (!isset($_SESSION['userID'])) {
    // Redirect to CodexPanel login page
    header('Location: /base/');
    exit();
}

// If user is authenticated, redirect to the actual phpMyAdmin interface
// through the proper CodexPanel route
header('Location: /dataBases/phpMyAdmin');
exit();
?>
