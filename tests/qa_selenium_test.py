import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def get_driver(browser):
    if browser == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
        chrome_options.add_argument('--no-sandbox')  # Disable sandbox for running in Docker
        chrome_options.add_argument('--remote-debugging-port=9222')  # Fix the DevToolsActivePort issue
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument('--headless')  # Run in headless mode
        
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    return driver



@pytest.fixture
def driver(browser):
    """Pytest fixture to initialize and quit the WebDriver."""
    driver = get_driver(browser)
    yield driver
    driver.quit()


def test_table_search(driver):
    """Test to validate search functionality on the Selenium Playground."""
    # Open the webpage
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    # Maximize the window
    driver.maximize_window()

    # Validate page title
    assert "Selenium Grid Online | Run Selenium Test On Cloud" in driver.title, "Page title does not match"

    # Find the search bar and perform the search
    search_xpath = "//label/input[@type='search']"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    search_query = "New York"
    search_box.send_keys(search_query)

    # Allow time for search results to update
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#example_info"), "Showing 1 to 5 of 5 entries")
    )

    # Locate and validate the result text
    message_element = driver.find_element(By.CSS_SELECTOR, "#example_info")
    actual_text = message_element.text
    expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

    time.sleep(2)

    assert actual_text == expected_text, f"Text verification failed! Expected: '{expected_text}', but got: '{actual_text}'"


if __name__ == "__main__":
    pytest.main(["-v", "-s", __file__])
