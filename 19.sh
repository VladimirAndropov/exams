#!/bin/bash

HOSTS_FILE="/etc/hosts"

if grep -qE '^[^#]*[[:space:]]+(?!127\.0\.0\.1)[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$HOSTS_FILE"; then
  echo "В файле /etc/hosts есть записи, относящиеся к адресам отличным от 127.0.0.1."
else
  echo "Все записи в файле /etc/hosts относятся к адресу 127.0.0.1."
fi

