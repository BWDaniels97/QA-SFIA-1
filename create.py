from application import db
from application.models import Artist

db.drop_all()
db.create_all()
