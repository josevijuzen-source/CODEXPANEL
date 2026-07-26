#!/bin/sh

BRANCH_NAME=v$(curl -s https://codexpanel.net/version.txt | sed -e 's|{"version":"||g' -e 's|","build":|.|g'| sed 's:}*$::')

rm -f /usr/local/codexpanel_upgrade.sh
wget -O /usr/local/codexpanel_upgrade.sh https://raw.githubusercontent.com/usmannasir/CodexPanel/$BRANCH_NAME/codexpanel_upgrade.sh 2>/dev/null
chmod 700 /usr/local/codexpanel_upgrade.sh
/usr/local/codexpanel_upgrade.sh
