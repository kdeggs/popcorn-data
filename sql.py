from sqlalchemy import text

new_movie = text(
    'INSERT INTO movies (movie_id, name, description, genre, votes) '
    'VALUES (DEFAULT, :name, :description, :genre, 0)'
)
get_all_movies = text(
    'SELECT * FROM movies'
)
get_votes = text(
    'SELECT votes FROM movies '
    'WHERE movie_id = :id'
)
add_vote = text(
    'UPDATE movies SET votes = :count '
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
