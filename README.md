# Documentation Database

This project was designed as a way to store many links to different tutorials, datasheets and documentation in one simple place.
The interface provides an easy-to-use and intuitive front-end to a postgreSQL database that runs on a server machine.

Full Project Documentation:
 - [Installation](#installation)

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

