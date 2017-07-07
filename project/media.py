import webbrowser


class Movie():
    # This class provides a way to store movie related information

    # List of valid ratings a movie can have
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor for initializing a movie instance
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens a browser and navigates to the trailer URL for this movie
    # in YouTube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
