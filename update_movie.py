from movies import Movies

movie = Movies()
filename = 'data.json'
moviedata = movie.get_movies_data(filename)
searchtitle = str(input("Please enter movie title to update: "))
updatetitle = str(input("Please enter Updated movie title: "))

movie.update_movie(moviedata, searchtitle, updatetitle, filename)