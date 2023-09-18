"""Working with jsons"""
import json
from pathlib import Path
# movies = [
#     {'id': 1, 'title': 'David goggin'},
#     {'id': 2, 'title': 'Andrew tate'}
# ]

# converts the data into json
# the array of dictioneries and json looks same
#  but this feature is not in every language

# data = json.dumps(movies)
# Path('movies.json').write_text(data)

result = Path('movies.json').read_text()
# parse the json
movies = json.loads(result)
for i, _ in enumerate(movies):

    print(movies[i]['title'])
