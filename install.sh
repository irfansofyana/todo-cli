#! /bin/bash -

# install all library dependencies
pip install -r requirements.txt

# create database file
databasePath="./src/database.db"
echo "creating database..."
if [[ ! -f "$databasePath" ]]; then
    touch $databasePath
    echo "database created!"
else
    echo "database is already exist!"
fi

# Build the application into binary file
cd src
pyinstaller --add-data "./database.db:." --add-data "../pyfiglet:./pyfiglet" todo-cli.py --onedir
