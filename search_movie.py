from movies import Movies

movie = Movies()
filename = 'data.json'
moviedata = movie.get_movies_data(filename)

# Serach movie details by title
# searchtext = "Indian"

searchtext = str(input("Please enter movie title to search: "))
movie.search_movie(moviedata, searchtext)