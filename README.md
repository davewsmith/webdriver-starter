# Webdriver setup on Ubuntu Trusty

June 13, 2018

This captures a (working!) point-in-time set of instructions for setting up
an environment on ubuntu/trusty for using selenium/webdriver to drive Firefox
and Chrome and includes a simple working example.

The details of getting this stuff working appear to change often,
and much of the doc that Google uncovers is stale.
This will be stale too one day. And so it goes.

For setting up the environment, see `Vagrantfile`.
(Don't worry if you aren't familiar with Vagrant;
the setup details are plain old bash.)

For running webdriver to drive Firefox and Chrome, see `tests.py`.

No license, no warranty. Use at your own risk. That's all.

## Some References

* https://github.com/SeleniumHQ/selenium/tree/master/py/selenium/webdriver

* https://sites.google.com/a/chromium.org/chromedriver/capabilities for ChromeDriver options.

* https://seleniumhq.github.io/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html


