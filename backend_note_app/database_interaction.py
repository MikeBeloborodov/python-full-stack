import sqlite3

def create_database():
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE notes(
                text text,
                owner text,
                date_created text,
                date_updated text
            )
    """)  
    except Exception as error:
        print("[!]ERROR DURING DATABASE CREATION")
        print(error) 
    connection.commit()
    connection.close()
    print("[!]DATABASE CREATED")

def get_all_data() -> list:
    connection = sqlite3.connect('notes.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT rowid, *
            FROM notes
    """)
    except Exception as error:
        print("[!]ERROR DURING ALL DATA RETRIEVING")
        print(error)
    data = cursor.fetchall()
    print("[+]DATA SUCCESSFULLY RETRIEVED")
    return data