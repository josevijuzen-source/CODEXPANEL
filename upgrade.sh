#!/bin/bash
## Script to clear caches after static file changes. Useful for development and testing.
## All credit belongs to Usman Nasir
## To use make it executable
## chmod +x /usr/local/CodexCP/upgrade.sh
## Then run it like below.
## /usr/local/CodexCP/upgrade.sh

# Check if virtual environment exists
if [[ ! -f /usr/local/CodexCP/bin/python ]]; then
    echo "Error: CodexPanel virtual environment not found at /usr/local/CodexCP/bin/python"
    echo "Please ensure CodexPanel is properly installed."
    exit 1
fi

cd /usr/local/CodexCP && /usr/local/CodexCP/bin/python manage.py collectstatic --no-input
rm -rf /usr/local/CodexCP/public/static/*
cp -R  /usr/local/CodexCP/static/* /usr/local/CodexCP/public/static/
# CSF support removed - discontinued on August 31, 2025
# mkdir /usr/local/CodexCP/public/static/csf/
find /usr/local/CodexCP -type d -exec chmod 0755 {} \;
find /usr/local/CodexCP -type f -exec chmod 0644 {} \;
chmod -R 755 /usr/local/CodexCP/bin
chown -R root:root /usr/local/CodexCP
chown -R lscpd:lscpd /usr/local/CodexCP/public/phpmyadmin/tmp
systemctl restart lscpd
