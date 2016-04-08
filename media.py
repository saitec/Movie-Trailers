__author__ = 'Sai'
class Movie():
    """Creates movie object that maps movie with various attributes.

    A factory for creating movie objects that is subsequently used
    by fresh_tomatoes.html to display movie, its attributes, and media.

    """

    def __init__(self, title, storyline, poster_image, trailer_video):
        self.title                  = title
        self.storyline              = storyline
        self.poster_image_url       = poster_image
        self.trailer_youtube_url    = trailer_video
