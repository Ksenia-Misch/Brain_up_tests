from locators.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

