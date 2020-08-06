import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Artist, Gigs
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        artist = Artist(artist_name = "Artic Monkeys")

        gig = Gigs(city = "Sheffield", venue = "Cafe Totem", content = "This is a gig", gig_date = 2020-1-1, gig_time = 19-0-0)

        db.session.add(artist)
        db.session.add(gig)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):

    def test_homepage_view(self):
        
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
