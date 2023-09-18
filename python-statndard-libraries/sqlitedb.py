import sqlite3
import json
from pathlib import Path
movies = json.loads(Path('movies.json').read_text())

# the connect method is used to connect to db if file doesn't exits it will create

# with sqlite3.connect('moviesdb.sqlite3') as conn:
#     COMMAND = "INSERT INTO Movies VALUES(?,?)"
#     for movie in movies:
#         conn.execute(COMMAND, tuple(movie.values()))
#     conn.commit()


with sqlite3.connect('moviesdb.sqlite3') as conn:
    COMMAND = "SELECT * FROM Movies"
    cursor = conn.execute(COMMAND)
    # for row in cursor:
    #     print(row)
    result = cursor.fetchall()
    print(result)
