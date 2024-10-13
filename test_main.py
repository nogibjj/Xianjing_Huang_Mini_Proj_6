import sqlite3
import os
import shutil
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create_CRUD, read_CRUD, update_CRUD, delete_CRUD


def test_extract():
    if os.path.exists("data"):
        shutil.rmtree("data")
    expected_file_path = "data/play_tennis.csv"
    result = extract()
    assert result == expected_file_path, "Extract failed."
    assert os.path.exists(expected_file_path), "File was not created."
    if os.path.exists(expected_file_path):
        os.remove(expected_file_path)


def test_load():
    extract()
    data = load()
    if data:
        print("Database loading successful:")
        for row in data:
            print(row)
    else:
        print("Failed to load the database.")


def test_create_CRUD():
    print("Test Insert a Record...")
    create_CRUD("TestD15", "Sunny", "Hot", "High", "Weak", "Yes")
    conn = sqlite3.connect("PlayTennisDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PlayTennisDB WHERE id = ?", (15,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print("Inserted data:")
        print(result)
    else:
        print("Failed to create.")


def test_read_CRUD():
    print("Test Read Database...")
    result = read_CRUD()
    if result:
        print("Data has been successfully read!")
    else:
        print("Failed to read.")


def test_update_CRUD():
    print("Test Update a Record...")
    update_CRUD("TestD15", "Sunny", "Hot", "High", "Weak", "No", 15)
    conn = sqlite3.connect("PlayTennisDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PlayTennisDB WHERE id = ?", (15,))
    result = cursor.fetchone()
    conn.close()
    expected_data = (15, "TestD15", "Sunny", "Hot", "High", "Weak", "No")
    assert result == expected_data, "Data update failed."


def test_delete_CRUD():
    print("Test Delete a Record...")
    delete_CRUD(15)
    conn = sqlite3.connect("PlayTennisDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PlayTennisDB WHERE id = ?", (15,))
    result = cursor.fetchone()
    conn.close()
    assert result is None, "Data delete failed."


if __name__ == "__main__":
    test_extract()
    test_load()
    test_create_CRUD()
    test_read_CRUD()
    test_update_CRUD()
    test_delete_CRUD()
