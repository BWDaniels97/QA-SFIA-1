from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Artist, Gigs
from application.forms import ArtistForm, GigForm, UpdateGigForm

@app.route('/')
@app.route('/home')

def home():
    gigData = Gigs.query.all()
    return render_template('home.html', title='Home', gigs=gigData)



@app.route('/artist', methods=['GET', 'POST'])
def artist():
    form = ArtistForm()
    if form.validate_on_submit():
        artistData = Artist(
            artist_name=form.artist_name.data
        )
        db.session.add(artistData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('artist.html', title='Artist', form=form)



@app.route('/gigs', methods=['GET', 'POST'])



def gig():
    
    form = GigForm()
    opts = []
    artist = Artist.query.all()
    for name in artist:
        opts.append(name.artist_name)

    form.artistname.choices = opts
    if form.validate_on_submit():
        artist = Artist.query.filter_by(artist_name=form.artistname.data).first()
        gigData = Gigs(
            singer=artist,
            city=form.city.data,
            venue=form.venue.data,
            content=form.content.data,
            gig_date=form.gig_date.data,
            gig_time=form.gig_time.data
        )
        db.session.add(gigData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('gigs.html', title='Gigs', form=form)


@app.route('/gigs/update/<id>', methods=['GET','POST'])
def update(id):
    gig = Gigs.query.filter_by(id=id).first()
    form = UpdateGigForm()
    if form.validate_on_submit():
        gig.city=form.city.data
        gig.venue=form.venue.data
        gig.content=form.content.data
        gig.gig_date=form.gig_date.data
        gig.gig_time=form.gig_time.data
        db.session.commit()
        return redirect(url_for('home', form=form))

    elif request.method == 'GET':
        form.city.data=gig.city,
        form.venue.data=gig.venue,
        form.content.data=gig.content
        form.gig_date.data=gig.gig_date
        form.gig_time.data=gig.gig_time
    return render_template('update.html', title='Update',form = form)


@app.route('/gigs/delete/<id>', methods=['Post', 'GET'])
def gig_delete(id):
    gig = Gigs.query.filter_by(id=id).first()
    db.session.delete(gig)
    db.session.commit()
    return redirect(url_for('home'))









