from sqlalchemy import text

new_movie = text(
    'INSERT INTO movies (movie_id, name, description, genre, votes) '
    'VALUES (DEFAULT, :name, :description, :genre, 0)'
)
get_movie = text(
    'SELECT movies.movie_id, movies.name, movies.description ,movies.votes, genre.type '
    'FROM movies '
    'INNER JOIN genre '
    'ON genre.genre_id = movies.genre '
    'WHERE movies.movie_id = :id'
)
get_all_movies = text(
    'SELECT movies.movie_id, movies.name, movies.description ,movies.votes, genre.type '
    'FROM movies '
    'INNER JOIN genre '
    'ON genre.genre_id = movies.genre '
    'ORDER BY movies.name'
)
get_popular_movies = text(
    'SELECT movies.movie_id, movies.name, movies.description ,movies.votes, genre.type '
    'FROM movies '
    'INNER JOIN genre '
    'ON genre.genre_id=movies.genre '
    'ORDER BY movies.votes DESC'
)
add_vote = text(
    'UPDATE movies SET votes = votes + 1 '
    'WHERE movie_id = :id'
)
delete_movie = text(
    'DELETE FROM movies '
    'WHERE movie_id = :id'
)

new_review = text(
    'INSERT INTO reviews (review_id, movie, reviewer_name, review) '
    'VALUES (DEFAULT, :movie_id, :name, :review)'
)
get_reviews_for_movie = text(
    'SELECT * FROM reviews '
    'WHERE movie = :id'
)
delete_review = text(
    'DELETE FROM reviews '
    'WHERE review_id = :id'
)
