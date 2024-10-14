import movierating


if __name__ == '__main__':
    movietitle = input('input the title of the movie: ')
    moviedict = movierating.ratings
    if movietitle in moviedict:
        print('rating of {}: {}'.format(movietitle, moviedict[movietitle]))

    else:
        print('Movie not found')
