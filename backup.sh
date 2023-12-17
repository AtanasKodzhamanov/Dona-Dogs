#!/bin/bash

# temp backup

# Extract database credentials from individual environment variables
HOST=$POSTGRES_HOST
PORT=$POSTGRES_PORT
USER=$POSTGRES_USERNAME
PASSWORD=$POSTGRES_PASSWORD
DB_NAME=$POSTGRES_NAME

echo "HOST: $HOST"
echo "PORT: $PORT"
echo "USER: $USER"
echo "PASSWORD: $PASSWORD"
echo "DB_NAME: $DB_NAME"

# Backup file name
BACKUP_FILE="donadogs_backup_$(date +%Y%m%d_%H%M%S).sql"

# Exporting the password for pg_dump
export PGPASSWORD=$PASSWORD

# Running pg_dump
pg_dump -h $HOST -p $PORT -U $USER -d $DB_NAME -F c > "$BACKUP_FILE"

echo "Backup created: $BACKUP_FILE"

# to run command
# chmod +x backup.sh
# ./backup.sh

# to list backups
# pg_restore -l donadogs_backup_.sql     

# to convert to sql 
# pg_restore -F c -f converted_backup.sql donadogs_backup_.sql
