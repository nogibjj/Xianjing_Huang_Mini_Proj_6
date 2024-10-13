"""Query the database"""

import sqlite3

LOG_FILE = "query_log.md"


def log(query):
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def create_CRUD(day, outlook, temp, humidity, wind, play):
    conn = sqlite3.connect("PlayTennisDB.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO PlayTennisDB(
            day,
            outlook,
            temp,
            humidity,
            wind,
            play
            ) 
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        (day, outlook, temp, humidity, wind, play),
    )
    conn.commit()
    conn.close()

    log(
        f"""INSERT INTO PlayTennisDB VALUES (
            {day}, 
            {outlook}, 
            {temp}, 
            {humidity}, 
            {wind}, 
            {play});"""
    )

def read_CRUD():
    conn = sqlite3.connect("PlayTennisDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PlayTennisDB")
    results = cursor.fetchall()
    conn.close()
    log("SELECT * FROM PlayTennisDB;")
    return results

def update_CRUD(day, outlook, temp, humidity, wind, play, updateID):
    conn = sqlite3.connect("PlayTennisDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE PlayTennisDB
        SET day=?, 
        outlook=?, 
        temp=?,
        humidity=?, 
        wind=?, 
        play=?
        WHERE id=?
        """,
        (
            day, outlook, temp, humidity, wind, play,
            updateID,
        ),
    )
    conn.commit()
    conn.close()

    log(
        f"""UPDATE PlayTennisDB SET 
        day={day}, 
        outlook={outlook},
        temp={temp}, 
        humidity={humidity}, 
        wind={wind}, 
        play={play} 
        WHERE id={updateID};"""
    )

def delete_CRUD(deleteID):
    """delete query"""
    conn = sqlite3.connect("PlayTennisDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM PlayTennisDB WHERE id=?", (deleteID,))
    conn.commit()
    conn.close()

    log(f"DELETE FROM PlayTennisDB WHERE id={deleteID};")





