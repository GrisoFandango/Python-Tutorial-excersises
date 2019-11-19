import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Robocop", "year": 1989},
# ]

# data = json.dumps(movies)
# print(data)
data2 = Path("movies.json").read_text()
movies = json.loads(data2)
print(movies)
print(movies[0])
