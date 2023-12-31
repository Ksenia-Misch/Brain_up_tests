
from pages.main_page import MainPage
import pytest

class TestMainPage:

    def test_MP_01_verify_redirection_to_description_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_description_page()

    def test_MP_02_verify_redirection_to_telegram_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_telegram_page()

    @pytest.mark.xfail
    def test_MP_03_1_verify_redirection_to_contributors_page(self, driver, main_page_open):
        page = MainPage(driver)
        page.open_contributors_page()
