import json
from collections import Counter


class Movies():

    # Writting json file
    def write_json_file(self,filename, moviedata):
        with open(filename, 'w') as f:
            json.dump(moviedata, f, indent=2)

    # get all movie data
    def get_movies_data(self, filename):
        with open(filename) as json_file:
            moviedata = json.load(json_file)
        return moviedata

    # Add movie details
    def add_movies(self, filename, moviedata, moviedetails):
        temp = moviedata['movie_details']
        # appending data to emp_details
        temp.append(moviedetails)
        self.write_json_file(filename, moviedata)

    # Delete movie details
    def delete_movie(self, moviedata, searchtitle, filename):
        count = self.is_unique(moviedata, searchtitle)
        if count == 0:
            print("Record Not Found!")
        else:
            for match in moviedata['movie_details']:
                if match['title'] == searchtitle:
                    moviedata['movie_details'].remove(match)
                    self.write_json_file(filename, moviedata)
                    print(match)

    # search movie details by title
    def search_movie(self, moviedata, searchtext):
        count = self.is_unique(moviedata, searchtext)
        if count == 0:
            print("Record Not Found!")
        else:
            for match in moviedata['movie_details']:
                if match['title'] == searchtext:
                    print(match)

    # search movie details by title
    def update_movie(self, moviedata, searchtitle, updatetitle, filename):
        count = self.is_unique(moviedata, searchtitle)
        if count > 1:
            print("Title is not unique!")
        elif count == 0:
            print("Record Not Found!")
        else:
            for match in moviedata['movie_details']:
                if match['title'] == searchtitle:
                    moviedata['movie_details'].remove(match)
                    match['title'] = updatetitle
                    self.add_movies(filename, moviedata, match)
                    print(match)

    # search report by genre
    def report_by_genre(self, moviedata, genre):
        for match in moviedata['movie_details']:
            if match['major_genre'] == genre and match['major_genre'] != '':
                print(match)

    # search report by year
    def report_by_year(self, moviedata, year):
        for match in moviedata['movie_details']:
            if match['year'] == year:
                print(match)

    # to check duplicate movie title
    def is_unique(self, moviedata, searchtitle):
        count = 0
        for match in moviedata['movie_details']:
            if match['title'] == searchtitle:
                count += 1
        return count

