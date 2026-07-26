Server_IP=$(curl --silent --max-time 30 -4 https://codexpanel.sh/?ip)
echo "$Server_IP" > "/etc/codexpanel/machineIP"