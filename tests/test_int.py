import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Artist, Gigs


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/bwdaniels97/QA-SFIA-1/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)





class TestArtist(TestBase):

    def test_artist(self):

        self.driver.find_element_by_xpath("/html/body/div/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="artist_name"]').send_keys("Artist1")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url





class TestGig(TestBase):

    def test_gig(self):

        self.driver.find_element_by_xpath("/html/body/div/a[2]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="artist_name"]').send_keys("Artist")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        self.driver.find_element_by_xpath("/html/body/div/a[3]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="artistname"]').send_keys("Artist")
        self.driver.find_element_by_xpath('//*[@id="city"]').send_keys("Sheffield")
        self.driver.find_element_by_xpath('//*[@id="venue"]').send_keys("Cafe Totem")
        self.driver.find_element_by_xpath('//*[@id="gig_date"]').send_keys("2020-11-11")
        self.driver.find_element_by_xpath('//*[@id="gig_time"]').send_keys("19:00")
        self.driver.find_element_by_xpath('//*[@id="content"]').send_keys("Test content")
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('home') in self.driver.current_url




