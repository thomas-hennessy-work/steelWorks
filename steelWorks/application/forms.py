from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from application.models import Song, Review

#Add data required to all feilds that cannot be null in the database
class SongForm(FlaskForm):
    title = StringField('Song title',
        validators=[DataRequired()])
    group = StringField('Group',
        validators=[DataRequired()])
    length = IntegerField('Song length (s)',
        validators=[DataRequired()])
    youTube = StringField('URL to song on YouTube')
    submit = SubmitField('Add song')

class ReviewForm(FlaskForm):
    review_text = StringField('Review',
        validators=[DataRequired()])
    score_total = IntegerField('Total score')
    mosh = IntegerField('Moshability score')
    vocals = IntegerField('Vocals score')
    riff = IntegerField('Riff score')
    bass = IntegerField('Bass score')
    beat = IntegerField('Beat score')
    submit = SubmitField('Add review')
