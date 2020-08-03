from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Artist, Gigs
from application.forms import ArtistForm, GigForm

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', title='Home')



@app.route('/artist', methods=['GET', 'POST'])
def artist():
    form = ArtistForm()
    if form.validate_on_submit():
        postData = Artist(
            artist_name=form.artist_name.data
        )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('artist.html', title='Artist', form=form)



@app.route('/gigs', methods=['GET', 'POST'])
def gig():
    form = GigForm()
    if form.validate_on_submit():
        postData = Gigs(
            artist_id=form.opts.data,
            city=form.city.data,
            venue=form.venue.data,
            content=form.content.data,
            gig_date=form.gig_date.data,
            gig_time=form.gig_time.data
        )
        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gigs.html', title='Gigs', form=form)
