"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/play_tennis.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""
    #prints the full working directory and path
    #print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect('PlayTennisDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS PlayTennisDB")
    c.execute(
        """
        CREATE TABLE PlayTennisDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT,
            outlook TEXT,
            temp TEXT,
            humidity TEXT,
            wind TEXT,
            play TEXT
        )
    """
    )

    #insert
    c.executemany(
        """
        INSERT INTO PlayTennisDB (
            day,
            outlook,
            temp,
            humidity,
            wind,
            play
            ) 
            VALUES (?, ?, ?, ?, ?, ?)""",
        payload,
    )
    # c.executemany("INSERT INTO PlayTennisDB VALUES (?,?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "PlayTennisDB.db"

