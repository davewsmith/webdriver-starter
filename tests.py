#!venv/bin/python

import unittest

from selenium import webdriver
from xvfbwrapper import Xvfb



class TestPagesUsingFirefox(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        options = webdriver.FirefoxOptions()
        self.browser = webdriver.Firefox(options=options)
        self.addCleanup(self.browser.quit)

    def x_testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def testGoogleHomepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


class TestPagesUsingChrome(unittest.TestCase):

    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.addCleanup(self.xvfb.stop)
        self.xvfb.start()
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)
        self.addCleanup(self.browser.quit)

    def x_testUbuntuHomepage(self):
        self.browser.get('http://www.ubuntu.com')
        self.assertIn('Ubuntu', self.browser.title)

    def testGoogleHomepage(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)


if __name__ == '__main__':
    unittest.main()
