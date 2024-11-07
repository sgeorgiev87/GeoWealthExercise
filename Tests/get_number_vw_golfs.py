import unittest

from Configuration.drivers_setup import driver_init, handle_exception
from Configuration.constants import Brands, VwModels, Extras
from Configuration.logger import logger
from PageObjects.homepage import HomePage
from PageObjects.search_page import MainSearchPage, SearchPageResults

BRAND = Brands.VW
MODEL = VwModels.GOLF
EXTRAS = [Extras.FOUR_WHEEL_DRIVE]


class TestSearchWidget(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = driver_init()
        cls.driver.maximize_window()

    def test_01_get_vw_golf_results(self):
        try:
            homepage = HomePage(self.driver)
            homepage.open_homepage()
            homepage.accept_cookies()
            homepage.go_to_search()
            search_page = MainSearchPage(self.driver)
            search_page.select_brand_model_and_extras(brand=BRAND, model=MODEL, extras=EXTRAS)
            search_page.click_search_button()
            search_results = SearchPageResults(self.driver)
            total_ads = search_results.get_number_total_ads()
            print(f'---> Total ads are {total_ads}')
            logger.info(f'---> Total ads are {total_ads}')

            top_ads = search_results.get_number_top_ads()
            print(f'---> Total TOP ads are {top_ads}')
            logger.info(f'---> Total TOP ads are {top_ads}')

            vip_ads = search_results.get_number_vip_ads()
            print(f'---> Total VIP ads are {vip_ads}')
            logger.info(f'---> Total VIP ads are {vip_ads}')
        except:
            handle_exception(self.driver, screenshot_name='VW_Golf_ads.png',
                             custom_exception='#### Counting VW Golf ads test failed!!!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
