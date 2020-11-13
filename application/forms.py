from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from application.models import Song, Review

#Ensures that scores given are in a predefined range
class pointsCheck:
    def __init__(self):    
        self.message = "Please choose a point value between 1 and 10"

    def __call__(self, form, field):
        if type(field.data) == int:
            if field.data > 10 or field.data < 0:
                raise ValidationError(self.message)

#Ensures special characters are not used
class SpecialCharCheck:
    def __init__(self, banned):
        self.banned = banned
        self.message = 'Please do not include special characters'

    def __call__(self, form, field):
        for specialChar in self.banned:
            if specialChar in field.data:
                raise ValidationError(self.message)

#Add data required to all feilds that cannot be null in the database
class SongForm(FlaskForm):
    title = StringField('Song title',
        validators=[DataRequired(),
            SpecialCharCheck(banned = ['%','^','&','*','(',')'])])
    group = StringField('Group',
        validators=[DataRequired(),
            SpecialCharCheck(banned = ['%','^','&','*','(',')'])])
    length = IntegerField('Song length (s)',
        validators=[DataRequired()])
    youTube = StringField('URL to song on YouTube')
    submit = SubmitField('Add song')

class ReviewForm(FlaskForm):
    review_text = StringField('Review',
        validators=[DataRequired(),
            SpecialCharCheck(banned = ['%','^','&','*','(',')'])])
    score_total = IntegerField('Total score',
            validators=[pointsCheck()])
    mosh = IntegerField('Moshability score',
            validators=[pointsCheck()])
    vocals = IntegerField('Vocals score',
            validators=[pointsCheck()])
    riff = IntegerField('Riff score',
            validators=[pointsCheck()])
    bass = IntegerField('Bass score',
            validators=[pointsCheck()])
    beat = IntegerField('Beat score',
            validators=[pointsCheck()])
    submit = SubmitField('Add review')
