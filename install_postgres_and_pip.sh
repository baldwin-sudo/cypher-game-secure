
#!/bin/bash

# Update the package lists
sudo apt update

# Install PostgreSQL and its contrib package
sudo apt install -y postgresql postgresql-contrib

# Start and enable PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Check the PostgreSQL service status
sudo systemctl status postgresql

# Install python3-pip
sudo apt install -y python3-pip

// a must to install  the psycopg binary 
sudo apt install -y libpq-dev python3-dev build-essential

# Switch to the postgres user and provide access to the psql interface
echo "To switch to the PostgreSQL user and access the psql interface, run:"
echo "    sudo -i -u postgres"
echo "    psql"

# Create a new PostgreSQL database and user (optional)
echo "To create a new PostgreSQL database and user, run the following in the psql interface:"
echo "    CREATE DATABASE mydatabase;"
echo "    CREATE USER myuser WITH PASSWORD 'mypassword';"
echo "    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;"

# Enable remote connections to PostgreSQL
echo "To enable remote connections, edit the following files:"
echo "    1. /etc/postgresql/14/main/postgresql.conf"
echo "        listen_addresses = '*'"
echo "    2. /etc/postgresql/14/main/pg_hba.conf"
echo "        host    all             all             0.0.0.0/0            md5"
echo "After editing, restart PostgreSQL with:"
echo "    sudo systemctl restart postgresql"
