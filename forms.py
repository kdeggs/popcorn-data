from wtforms import StringField, SelectField, SubmitField, TextAreaField, Form
from wtforms.validators import DataRequired, Regexp


class AddMoviesForm(Form):
    name = StringField('Suggested Movie', validators=[DataRequired()])
    description = TextAreaField('Write description of movie here: ')
    genre = SelectField(
        choices=[('action', 'Action'), ('comedy', 'Comedy'), ('horror', 'Horror'), ('romance', 'Romance')],
        validators=[DataRequired()])

    submit = SubmitField('Submit Movie')
