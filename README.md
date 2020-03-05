# User Friendly Postgresql Database GUI

A tkinter GUI with psycopg2 database adapter that runs the query and outputs info on the screen.
Useful for HR employees with no sql knowledge.

What it does: 
              
              - Display the database table.  - Sort by Name.
              - Insert data.                 - Sort by salary.
              - Update data.                 - Sort by job.
              - Delete data.                 - Search employee`s Name.           
              - Sort by ID.                  - Select data rows to edit.


## Getting Started

Since this is a GUI to connect to a postgresql database you will need to have a postgresql database (You can use another 
sql language but you would need to change the adapter and tweak the code). 

Install Postgresql here: https://www.postgresql.org/

After finishing your postgre install go to the file postgresql_commands.py and on the first line:
   
    conn = psycopg2.connect(dbname='', host='', user='', password='')
   
Add your database name, host, user and password all inside quotes, by default your info should look like this:
             
    conn = psycopg2.connect(dbname='template0', host='localhost', user='postgres', password='Password you added on install')



### How to run it

We have two options on how to run it:
 
 1- The fast way by just opening the main_file.py on your IDE and running it 
(make sure both files are on the same folder).
 
 2- We can use pyinstaller to make a .exe file (this makes it better for 
the people that will constantly be using it, since after creating a .exe the 
only thing needed to run is to double click the file).

Lets make a .exe file. On your terminal type:

        pip install pyintaller
        
After installing pyinstaller go to the file directory on your terminal and type:

     pyinstaller --onefile -w main_file.py



## Using the GUI

Here are some examples with what you can do with the GUI:


- Inserting data

- Deleting data

- Updating data

- Sorting data

- Search data

- Error box











