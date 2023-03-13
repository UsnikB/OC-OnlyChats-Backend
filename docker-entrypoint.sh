#!/bin/sh
set -e

# Wait for the MySQL database to start
until nc -z -v -w30 db 3306
do
  echo 'Waiting for MySQL database to start...'
  sleep 5
done
echo 'MySQL database started successfully!'

# Run the web application
python app.py
