from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AddMoviesForm(FlaskForm):
    name = StringField('Suggested Movie Name', validators=[DataRequired()])
    description = TextAreaField('Write a Description of the Movie', validators=[DataRequired()])
    genre = SelectField(
        choices=[(1, 'Action'), (2, 'Comedy'), (3, 'Horror'), (4, 'Romance')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit Movie')


class AddReviewForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    review = TextAreaField('Write your review here', validators=[DataRequired()])

    submit = SubmitField('Submit Review')
