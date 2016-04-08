"""
Movie Trailer Website

Creates a HTML page with a list of predefined movies. On the page,
users can select the image/poster to view the movies' trailer.

Usage:
    Just run this file from your Python interpreter.
    Alternatively, you can open the 'fresh_tomatoes.html' file.
"""
__author__ = 'Sai'

from media import Movie
import fresh_tomatoes

# Movie Objects:
world_war_z = Movie(
    'World War Z',
    'As the world is grasped by a mysterious infection that turns humans into zombies' 
    'Gerry, a former U.N. investigator has to leave his family' 
    'to determine the source of the infection',
    'http://goo.gl/1pZBuW',
    'https://www.youtube.com/watch?v=HcwTxRuq-uk')

the_social_network = Movie(
    'The Social Network',
    'Mark Zuckerberg creates a social networking site, Facebook, with the help of his'
    'friend Eduardo Saverin. But soon, a string of lies tears their relationship apart'
    'even as Facebook connects people.',
    'http://goo.gl/200E9J',
    'https://www.youtube.com/watch?v=lB95KLmpLR4')

the_lion_king = Movie(
    'The Lion King',
    'Naive cub and lion prince Simba is made to believe that he killed his father,'
    'which is why he flees into exile. After several years,'
    ' Simba returns to claim the kingdom and overthrow the usurper.',
    'http://goo.gl/xpRU5E',
    'https://www.youtube.com/watch?v=GibiNy4d4gc')

the_dark_knight = Movie(
    'The Dark Knight',
    'Batman has a new foe, the Joker, who is an accomplished criminal hell-bent on '
    'decimating Gotham City. Together with Gordon and Harvey Dent, Batman struggles'
    'to thwart the Joker before it is too late.',
    'https://goo.gl/EUnbcs',
    'https://www.youtube.com/watch?v=EXeTwQWrcwY')

interstellar = Movie(
    'interstellar',
    'In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper,'
    'along with a team of researchers, is sent on a planet exploration mission to'
    'report which planet can sustain life.',
    'https://goo.gl/WxdbB1',
    'https://www.youtube.com/watch?v=zSWdZVtXT7E')

the_prestige = Movie(
    'The Prestige',
    'Two friends and fellow magicians become bitter enemies after a sudden tragedy.'
    'As they devote themselves to this rivalry, they make sacrifices that bring them'
    'fame but with terrible consequences.',
    'http://goo.gl/4C46tf',
    'https://www.youtube.com/watch?v=o4gHCmTQDVI')


#############################
#           main            #
#############################

def main():
    # store movie objects as list to be processed by fresh_tomatoes
    movies = [world_war_z, the_social_network,
              the_lion_king, the_dark_knight, interstellar,
              the_prestige]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
