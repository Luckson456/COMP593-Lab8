"""
Description:
Creates the relationships table in the Social Network database
and populates it with 100 fake relationships.

Usage:
python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
from random import randint,choice
from datetime import datetime,date

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def adapt_date(date_obj):
    return date_obj.strftime("%Y-%m-%d")

sqlite3.register_adapter(date, adapt_date)


def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Add the Relationships Table"
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    create_relationships_tbl_query = """
        CREATE TABLE IF NOT EXISTS relationship (
            id INTEGER PRIMARY KEY,
            person1_id INTEGER NOT NULL,
            person2_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            start_date DATE NOT NULL,
            FOREIGN KEY (person1_id) REFERENCES people(id),
            FOREIGN KEY (person2_id) REFERENCES people(id)
        )
    """
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    con=sqlite3.connect(db_path)
    cur=con.cursor()
    add_relationship_query="""
                        INSERT INTO relationship
                        (person1_id,
                        person2_id,
                        type,
                        start_date
                        )
                        VALUES(?,?,?,?)
                        """
    # Hint: See example code in lab instructions entitled "Populate the Relationships Table"
    fake=Faker()
    
    for _ in range (100):
        person1_id=randint(1,200)
        person2_id=randint(1,200)
        while person2_id==person1_id:
            person2_id=randint(1,200)
            
        rel_type=choice(['friend','spouse','partner','relative'])
        start_date=fake.date_between(start_date='-50y', end_date='today')
        new_relationship=(person1_id,person2_id,rel_type,start_date)
        
        cur.execute(add_relationship_query,new_relationship)
        
    con.commit()
    con.close()
    
if __name__ == '__main__':
    main()