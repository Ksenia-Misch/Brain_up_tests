from pages.base_page import BasePage
from locators.locators import BasePageLocators
from test_data.links import MainPageLinks


class MainPage(BasePage):


    def open_description_page(self):
        self.driver.find_element(*BasePageLocators.DESCRIPTION_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_DESCRIPTION_PAGE, \
            "The link leads to an incorrect page"