from movies import Movies

movie = Movies()
filename = 'data.json'
moviedata = movie.get_movies_data(filename)

reportType = int(input("Please enter number 1 for Genre 2 for year wise report: "))

if reportType == 1:
    # report by genre
    genre = str(input("Please enter Genre: "))
    movie.report_by_genre(moviedata, genre)
elif reportType == 2:
    # report by year
    year = int(input("Please enter Year: "))
    movie.report_by_year(moviedata, year)
else:
    print("Wrong Input!")