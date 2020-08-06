from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Artist, Gigs


class ArtistForm(FlaskForm):
    artist_name = StringField('Name',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    submit = SubmitField('Post!')

def getOpts():
    opts = []
    artist = Artist.query.all()
    for name in artist:
        opts.append(name.artist_name)

    return opts

class GigForm(FlaskForm):
    
    artistname = SelectField("Artist Name", choices=getOpts(), validators = [])



    city = StringField('City',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    venue = StringField('Venue',
        validators = [
            DataRequired(),
            Length(min=2, max=50)
        ]
    )
    gig_date = DateField('Date',
        validators = [
            DataRequired()
        ]
    )
    gig_time = TimeField('Time',
        validators = [
            DataRequired()
        ]
    )
    content = StringField('Content',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    submit = SubmitField('Post!')
