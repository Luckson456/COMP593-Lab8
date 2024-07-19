"""
Description:
Creates the people table in the Social Network database
and populates it with 200 fake people.

Usage:
python create_db.py
"""
import os
import sqlite3
from faker import Faker
from multiprocessing import connection

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    conn=sqlite3.connect(db_path)
    c=conn.cursor()
    
    c.execute(''' Create table if not exists people
                (id   INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT ,
                age   INTEGER,
                location TEXT)''')
    
    conn.commit()
    conn.close()
    

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    fake=Faker()
    
    for _ in range(200):
        name=fake.name()
        age=fake.random_int(min=18,max=100)
        location=fake.city()
        cur.execute("insert into people(name,age,location)VALUES(?,?,?)",
                    (name,age,location))
        
        conn.commit()
    conn.close()
    

if __name__ == '__main__':
    main()