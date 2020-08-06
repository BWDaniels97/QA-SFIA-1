from application import db
from application.models import Artist, Gigs

db.drop_all()
db.create_all()
