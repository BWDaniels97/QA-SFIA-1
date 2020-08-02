from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime, date, time

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    venue = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    gig_date = db.Column(db.Date, nullable=False)
    gig_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', self.user_id, '\r\n',
            'City: ', self.city, '\r\n', self.content
        ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.band_name
        ])
        
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
