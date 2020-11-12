from flask import render_template, url_for, redirect, request

#importing the app and the linked database created in the initialisation file
from application import app, db
#Importing the database models
from application.models import Song, Review
#Importing the forms
from application.forms import SongForm, ReviewForm

@app.route('/')
def index():
    allSongs = Song.query.all()
    return render_template('index.html', allSongs=allSongs)

@app.route('/add-song', methods=['GET', 'POST'])
def addSong():
    form = SongForm()
    #if the form validates on clicking the submit button
    if form.validate_on_submit():
        new_song = Song(title=form.title.data,
                    group=form.group.data,
                    length=form.length.data,
                    yt_link=form.youTube.data)
        db.session.add(new_song)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add-song.html', form=form)

@app.route('/add-review/<int:songID>', methods=['GET', 'POST'])
def addReview(songID):
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(song_id=songID,
                review_text=form.review_text.data,
                score_total=form.score_total.data,
                mosh=form.mosh.data,
                vocals=form.vocals.data,
                riff=form.riff.data,
                bass=form.bass.data,
                beat=form.beat.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('viewSong', songID=songID))
    return render_template('add-review.html', form=form, songID=songID)

@app.route('/song-details/<int:songID>')
def viewSong(songID):
    song_viewed = Song.query.get(songID)
    song_reviews = Review.query.filter_by(song_id=songID)
    return render_template('song-details.html', song_viewed=song_viewed, song_reviews=song_reviews)

@app.route('/edit-song/<int:songID>', methods=['GET', 'POST'])
def editSong(songID):
    form = SongForm()
    #Stros the id and then updated data can be added before commiting
    song_to_update = Song.query.get(songID)
    if form.validate_on_submit():
        #Reading the data provided in the form
        song_to_update.title = form.title.data
        song_to_update.group = form.group.data
        song_to_update.length = form.length.data
        song_to_update.yt_link = form.youTube.data
        db.session.commit()
        return redirect(url_for('viewSong', songID=songID))
    elif request.method == 'GET':
        #Prefill the information in the form
        form.title.data = song_to_update.title
        form.group.data = song_to_update.group 
        form.length.data = song_to_update.length
        form.youTube.data = song_to_update.yt_link

    return render_template('edit-song.html', song_to_update=song_to_update, form=form)

@app.route('/delete-song/<int:songID>')
def deleteSong(songID):
    song_to_delete = Song.query.get(songID)
    reviews_to_delete = Review.query.filter_by(song_id=song_to_delete.song_id)
    for review in reviews_to_delete:
        db.session.delete(review)
    db.session.delete(song_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete-review/<int:reviewID>')
def deleteReview(reviewID):
    review_to_delete = Review.query.get(reviewID)
    songID = review_to_delete.song_id
    print(reviewID)
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for('viewSong', songID=songID))
