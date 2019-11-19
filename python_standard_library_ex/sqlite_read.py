import sqlite3
import json
from pathlib import Path

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    # when reading from a DB the cursor move and in an iterable
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
    # with fetchall we get all in one line
    # but like explained with reading file, the cursor after the firs iteration
    # is at the end
    movies = cursor.fetchall()
    print(movies)
