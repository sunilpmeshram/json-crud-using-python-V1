from movies import Movies

movie = Movies()
filename = 'data.json'
moviedata = movie.get_movies_data(filename)

searchtext = str(input("Please enter movie title to delete: "))
movie.delete_movie(moviedata, searchtext, filename)