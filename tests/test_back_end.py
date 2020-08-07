import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Artist, Gigs
from os import getenv

class TestBase(TestCase):

    def create_app(self):

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
        db.session.commit()
        db.drop_all()
        db.create_all()

        artist = Artist(artist_name = "Artic Monkeys")

        gig = Gigs(id = 1, city = "Sheffield", venue = "Cafe Totem", content = "This is a gig", gig_date = '2020-11-11', gig_time = '19:00:00', artist_id = 1)

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

    def test_gigpage_view(self):
        response = self.client.get(url_for('gigs'))
        self.assertEqual(response.status_code, 200)

    def test_artistpage_view(self):
        response = self.client.get(url_for('artist'))
        self.assertEqual(response.status_code, 200)


    def test_add_gig(self):
        with self.client:
            response = self.client.post(url_for('gigs'),
                data=dict(artistname='Artic Monkeys', city='Test City', venue='test venue', gig_date='2020-11-11', gig_time= '19:00:00', content='Test Gig'),follow_redirects=True)
            self.assertIn(b'Test Gig', response.data)


    def test_add_artist(self):
        with self.client:
            response = self.client.post(url_for('artist'),
                data=dict(artist_name='Kooks'), follow_redirects=True)
            self.assertEqual(response.status_code, 200)


    '''def test_update_gig(self):
        with self.client:
            response = self.client.post(url_for('/update/1')
                    data=dict(city='update', venue='update', gig_date='2020-11-11', gig_time='19:00:00', content='Updated'),follow_redirects=True)
            self.assertIn(b'Updated', response.data)'''

    '''def test_update(self):
        
        response = self.client.get(url_for('/update/1')) 
        self.assertEqual(response.status_code, 200)'''













