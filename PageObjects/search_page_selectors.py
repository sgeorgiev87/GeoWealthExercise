from selenium.webdriver.common.by import By


class SearchPageSelectors:
    BRAND_SELECT_MENU = (By.CSS_SELECTOR, 'select[name="f5"]')
    MODEL_SELECT_MENU = (By.NAME, 'f6')
    FOUR_WHEEL_DRIVE_CHECKBOX = (By.ID, 'eimg88')

    @staticmethod
    def select_extra_by_name(extra_name):
        return By.XPATH, '//span[(text()="%s")]' % extra_name

    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="button"]')

    PAGE_1 = (By.LINK_TEXT, '1')
    NEXT_PAGE = (By.CSS_SELECTOR, 'a[class*="next"]')

    TOP_ADS = (By.CSS_SELECTOR, 'img[src*="TOP"]')
    VIP_ADS = (By.CSS_SELECTOR, 'img[src*="VIP"]')
    ADS_NUMBER = (By.XPATH, '//div[contains(text(),"общо")]')
