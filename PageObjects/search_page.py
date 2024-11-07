import re
from selenium.common.exceptions import TimeoutException
from Configuration.base_page import BasePage
from PageObjects.search_page_selectors import SearchPageSelectors


class MainSearchPage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def select_brand(self, brand_to_select):
        self.select_by_value(selector=SearchPageSelectors.BRAND_SELECT_MENU, value=brand_to_select)

    def select_model(self, model_to_select):
        self.select_by_value(selector=SearchPageSelectors.MODEL_SELECT_MENU, value=model_to_select)

    def select_specific_extra(self, extra_visible_text):
        self.click_on_element(f'{extra_visible_text} checkbox',
                              SearchPageSelectors.select_extra_by_name(extra_visible_text))

    def select_brand_model_and_extras(self, brand, model, extras):
        self.select_brand(brand)
        self.select_model(model)
        for extra in extras:
            self.select_specific_extra(extra)

    def click_search_button(self):
        self.click_on_element('Search button', SearchPageSelectors.SEARCH_BUTTON)


class SearchPageResults(BasePage):
    def __init__(self, driver, timeout=3):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def get_number_total_ads(self):
        number_text = self.visibility_of_element(SearchPageSelectors.ADS_NUMBER).text
        all_numbers = [int(s) for s in re.findall(r'\d+', number_text)]
        total_ads = max(all_numbers)
        return total_ads

    def get_number_top_ads(self):
        self.clickable_element(SearchPageSelectors.PAGE_1).click()
        all_top_ads = []
        while self.is_element_clickable(SearchPageSelectors.NEXT_PAGE):
            try:
                top_ads = self.visibility_of_elements(SearchPageSelectors.TOP_ADS)
                all_top_ads.extend(top_ads)
                self.clickable_element(SearchPageSelectors.NEXT_PAGE).click()
            except TimeoutException:
                break
        return len(all_top_ads)

    def get_number_vip_ads(self):
        self.clickable_element(SearchPageSelectors.PAGE_1).click()
        all_vip_ads = []
        while self.is_element_clickable(SearchPageSelectors.NEXT_PAGE):
            try:
                vip_ads = self.visibility_of_elements(SearchPageSelectors.VIP_ADS)
                all_vip_ads.extend(vip_ads)
                self.clickable_element(SearchPageSelectors.NEXT_PAGE).click()
            except TimeoutException:
                break
        return len(all_vip_ads)
