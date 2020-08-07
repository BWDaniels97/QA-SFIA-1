from application import db
from datetime import datetime, date, time

class Gigs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    venue = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    gig_date = db.Column(db.Date, nullable=False)
    gig_time = db.Column(db.Time, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), nullable=False)
    gigs = db.relationship('Gigs', backref='singer', lazy=True)
