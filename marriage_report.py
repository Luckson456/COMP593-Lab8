"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import csv
import os
import sqlite3
from create_relationships import db_path, script_dir

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
    con = sqlite3.connect(db_path)
    cur=con.cursor()
    
    married_couple_query="""
    SELECT person1.name,person2.name,start_date
    FROM relationship r
    JOIN people person1 ON relationships.person1_id=person1.id
    JOIN people person2 ON relationships.person2_id=person2.id
    WHERE type='married'
    """
    cur.execute(married_couple_query)
    married_couples=cur.fetchall()
    con.close()
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    with open(csv_path,'w',newline='')as csvfile:
        csvwriter= csv.writer(csvfile)
        
        csvwriter.writerow(['Person1','Person2','Wedding Anniversary'])
        for couple in married_couples:
            csvwriter.writerow(couple)
    # Hint: We did this in Lab 7.

if __name__ == '__main__':
    main()