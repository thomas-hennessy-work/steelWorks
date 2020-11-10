from flask import render_template, url_for

#importing the app and the linked database created in the initialisation file
from application import app, db
#Importing the database models
from application.models import Song, Review
#Importing the forms
from application.forms import SongForm, ReviewForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-song' methods=['GET', 'POST'])
def addSong():
    form = SongForm()
    #if the form validates on clicking the submit button
    if form.validate_on_submit():
        new_song = Song(song_title=form.title.data,
                    song_group=form.group.data,
                    song_length=form.length.data,
                    song_yt_link=form.youTube.data)
        db.session.add(new_song)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-song', form=form)
