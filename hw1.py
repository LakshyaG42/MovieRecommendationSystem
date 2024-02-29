# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    usersRated = {}
    ratingsData = {}
    for line in open(f):
        words = line.split("|")
        title = words[0].strip()
        rating = float(words[1].strip())
        userid = int(words[2].strip())
        if(title in usersRated.keys() and title in ratingsData.keys()):
            if(userid not in usersRated[title]):
                usersRated[title].append(userid)
                ratingsData[title].append(rating)
        else:
            usersRated[title] = [userid]
            ratingsData[title] = [rating]
    return ratingsData
    pass
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    movieIDs = {}
    genreData = {}
    for line in open(f):
        words = line.split("|")
        genre = words[0].strip()
        movieID = int(words[1].strip())
        title = words[2].strip()
        if(title in movieIDs.keys() and title in genreData.keys()):
            if(movieID not in movieIDs.values()):
                movieIDs[title] = movieID 
                genreData[title] = genre
        else:
            movieIDs[title] = movieID 
            genreData[title] = genre
    return genreData

    pass

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genreDict = {}
    for key, value in d.items():
        if(value in genreDict.keys()):
            genreDict[value].append(key)
        else: 
            genreDict[value] = [key]

    return genreDict
    pass
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    averageRatings = {}
    for key, values in d.items():
        averageRatings[key] = (sum(values))/len(values)
            
    return averageRatings
    pass
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    pass
    sortedMovies = dict(Counter(d).most_common(n))
    return sortedMovies
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    thresholdMovies = {}
    for key, value in d.items():
        if(value >= thres_rating):
            thresholdMovies[key] = value
    return thresholdMovies
    pass
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    popularInGenre = {}
    if(genre in genre_to_movies.keys()):
        movies = genre_to_movies[genre]
    for movie in movies:
        if(movie in movie_to_average_rating.keys()):
            popularInGenre[movie] = movie_to_average_rating[movie]
        else:
            popularInGenre[movie] = 0
    return get_popular_movies(popularInGenre, n)
    pass
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    genreRating = 0.0
    moviesInGenre = []

    if genre in genre_to_movies.keys():
        moviesInGenre.extend(genre_to_movies[genre])
    else:
        return -1
    for movie in moviesInGenre:
        if movie in movie_to_average_rating.keys():
            genreRating += movie_to_average_rating[movie]
    genreRating = genreRating / len(moviesInGenre)
    return genreRating
    pass
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genresToAvg = {}
    for genre in genre_to_movies.keys():
        genresToAvg[genre] = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)

    return get_popular_movies(genresToAvg, n)
    pass

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    UserRatings = {}
    for line in open(f):
        words = line.split("|")
        title = words[0].strip()
        rating = float(words[1].strip())
        userid = int(words[2].strip())
        if(userid in UserRatings.keys()):
            UserRatings[userid].append((title, rating))
        else:
             UserRatings[userid] = [(title, rating)]
    return UserRatings
    pass
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    userMoviesToRatings = dict(user_to_movies[user_id]) 
    #print(userMoviesToRatings)
    userMovies_to_genre = {}
    for key in userMoviesToRatings.keys():
        userMovies_to_genre[key] = movie_to_genre[key]
    #print(userMovies_to_genre)
    userGenreToMovies = create_genre_dict(userMovies_to_genre)
    #print(userGenreToMovies)
    #allusersPopularGenres = genre_popularity(userGenreToMovies, userMoviesToRatings)
    #print(allusersPopularGenres)
    usersPopularGenre = genre_popularity(userGenreToMovies, userMoviesToRatings, 1)
   #print(usersPopularGenre)
    for key in usersPopularGenre.keys():
        return key
        
    pass
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    userMoviesToRatings = dict(user_to_movies[user_id])
    genreToMovies = create_genre_dict(movie_to_genre)
    usersFavGenre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    movieRecs = {}
    for movie in genreToMovies[usersFavGenre]:
        if movie not in userMoviesToRatings.keys():
            movieRecs[movie] = movie_to_average_rating[movie]
    topMovieRecs = Counter(movieRecs)
    top3movies = topMovieRecs.most_common(3)
    return top3movies

    pass

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    
    
    #create_genre_dict(read_movie_genre("genreMovieSample.txt"))
    #get_popular_movies(calculate_average_rating(read_ratings_data("movieRatingSample.txt")), 3)
    
    
    #print(f"Movie Genres: {read_movie_genre('genreMovieSample.txt')}")
    #print(f'Movie Average Ratings {calculate_average_rating(read_ratings_data("movieRatingSample.txt"))}')
    #print(f"Adventure Avg Ratings: {get_genre_rating('Adventure', create_genre_dict(read_movie_genre('genreMovieSample.txt')),calculate_average_rating(read_ratings_data('movieRatingSample.txt')))}")
    #print(f'All Genre Avg Ratings: {genre_popularity(create_genre_dict(read_movie_genre("genreMovieSample.txt")),calculate_average_rating(read_ratings_data("movieRatingSample.txt")))}')
    #print(read_user_ratings("movieRatingSample.txt"))

    #print(get_user_genre(6, read_user_ratings("movieRatingSample.txt"), read_movie_genre("genreMovieSample.txt")))


    #Check with Friend:
    movie_ratings_dict = read_ratings_data('movieRatingSample.txt')
    #print(movie_ratings_dict)
    
    movie_genre_dict = read_movie_genre('genreMovieSample.txt')
    #print(movie_genre_dict)
    
    cgd = create_genre_dict(movie_genre_dict)
    #print(cgd)
    
    avgR = calculate_average_rating(movie_ratings_dict)
    #print(avgR)
    
    popMov = get_popular_movies(avgR, 6)
    #print(popMov)
   
    fm = filter_movies(avgR)
    #print(fm)

    gpg = get_popular_in_genre('Comedy', cgd, avgR)
    #print(gpg)

    ggr = get_genre_rating('Comedy', cgd, avgR)
    #print(ggr)

    gp = genre_popularity(cgd, avgR)
    #print(gp)

    rur = read_user_ratings('movieRatingSample.txt')
    #print(rur)

    gug = get_user_genre(15, rur, movie_genre_dict)
    #print(gug)

    rm = recommend_movies(15, rur, movie_genre_dict, avgR)
    #print(rm)
    pass

    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    