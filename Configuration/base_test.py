import unittest
from Configuration.drivers_setup import *

"""
A Base Test to be inherited by all tests, so we can manage settings here
"""


class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
