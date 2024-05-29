open_ports=$(netstat -tuln | grep 'LISTEN')

echo "Список открытых портов на данной машине:"
echo "$open_ports" | awk '{print $4}' | awk -F ':' '{print $NF}'