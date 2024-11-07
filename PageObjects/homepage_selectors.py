from selenium.webdriver.common.by import By


class HomepageSelectors:
    ACCEPT_COOKIES = (By.ID, 'cookiescript_accept')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'a[href*="search"]')

