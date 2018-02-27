# Recommendation-System
Different algorithms to make recommendations for movies

#Movie Recommendation System
#The Training Data
The training data: a set of movie ratings by 200 users (userid: 1-200) on 1000 movies (movieid: 1-1000). The data is stored in a 200 row x 1000 column table. Each row represents one user. Each column represents one movie. A rating is a value in the range of 1 to 5, where 1 is "least favored" and 5 is "most favored". Please NOTE that a value of 0 means that the user has not explicitly rated the movie.
Please download the training data here: train.txt.

#The Test Data
There are three test files: test5.txt, test10.txt and test20.txt.
[test5.txt] A pool of movie ratings by 100 users (userid: 201-300). Each user has already rated 5 movies. The format of the data is as follows: the file contains 100 blocks of lines. Each block contains several triples : (U, M, R), which means that user U gives R points to movie M. Please note that in the test file, if R=0, then you are expected to predict the best possible rating which user U will give movie M. 
The following is a block for user 276. (line 6545-6555 of test5.txt)
276 42 4 // user 276 gives movie 42 4 points. 
276 85 2 // user 276 gives movie 85 2 points. 
276 194 5 // user 276 gives movie 194 5 points.
276 208 5 // user 276 gives movie 208 5 points.
276 585 1 // user 276 gives movie 585 1 point.
276 4 0 // need to predict user 276's rating for movie 4
276 26 0 // need to predict user 276's rating for movie 26
