# Documentation Database

This project was designed as a way to store many links to different tutorials, datasheets and documentation in one simple place.
The interface provides an easy-to-use and intuitive front-end to a postgreSQL database that runs on a server machine.

Full Project Documentation:
 - [Installation](#installation)
 - [Usage](#usage)

## Installation

### Server-Side
I recommend using a Raspberry Pi 3/4 for the server for this project, but in theory anything could be used
1. Install postgreSQL server 

    `sudo apt install postgresql`

2. Login as postgres user 

    `sudo su postgres`
    
3. Execute the [database.sql](database.sql) file to set up and initialise your database

The database should now be setup and ready to query

### Client-Side
1. Clone the repository

    `git clone https://www.github.com/RM220507/DocumentationDatabase.git`
    
2. Install the required dependencies 
    
    `pip install psycopg2`
    
3. Insert your server host and user/password into the [client_conf.ini](client_conf.ini) file
4. Run [main.py](main.py)

## Usage
The server should just need to be booted, and postgreSQL will automatically start.
Most of these instructions are fairly obvious, so feel free to skip through them.

### Searching
1. Enter the name of the entry in the text box
2. Click the `Search` button
3. Find your result in the table
4. Copy the link into your browser

### Adding Languages
1. On the search screen, click the `Add New ->` button
2. Type the name of your new language in the text entry below the `Add New Language` label
3. Click the first `Add` button
4. You should now see your language in the `Language` option selection

### Adding Links
1. Type the name of the link in the `Name` entry
2. Copy the web url into the `Link` text entry
3. Select the language from the `Language` option selection
4. Check/uncheck the checkbox, based on whether the link is documentation or tutorial
5. Click the `Add` button