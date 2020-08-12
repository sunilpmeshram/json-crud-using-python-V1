from movies import Movies
import json

class mydict(dict):
        def __str__(self):
            return json.dumps(self)


title = str(input("Please add movie title: "))
genre = str(input("Please add movie genre: "))
year = str(input("Please add movie year: "))
movieDetails = [['title', title],
                   ['genre', genre],
                   ['year', year]]
moviedetails = mydict(movieDetails)

movie = Movies()
filename = 'data.json'
moviedata = movie.get_movies_data(filename)

movie.add_movies(filename, moviedata, moviedetails)
print(moviedata)