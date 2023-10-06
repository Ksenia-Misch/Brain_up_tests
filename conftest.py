
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



URL = "https://brainup.site/"

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page_open(driver):
    driver.get(URL)
