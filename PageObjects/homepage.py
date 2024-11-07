from Configuration.base_page import BasePage
from PageObjects.homepage_selectors import HomepageSelectors


class HomePage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def open_homepage(self):
        self.driver.get('https://www.mobile.bg/')

    def accept_cookies(self):
        self.click_on_element('Accept Cookies', HomepageSelectors.ACCEPT_COOKIES)

    def go_to_search(self):
        self.click_on_element('Search button', HomepageSelectors.SEARCH_BUTTON)
