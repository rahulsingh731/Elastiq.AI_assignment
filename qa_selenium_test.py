import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    """Setup Selenium WebDriver."""
    options = Options()
    options.add_argument("--headed")  # Run tests in headless mode
    driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe", options=options)
    yield driver
    driver.quit()


def test_table_search(driver):
    """Validate search functionality on the Table Sort and Search demo page."""
    driver.maximize_window()
    # Navigate to the page
    driver.get(
        "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    )
    
    # Wait for the search field and perform a search
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#example_filter input"))
    )
    search_field.send_keys("New York")

    # Wait for the filtered results
    WebDriverWait(driver, 10).until(
        lambda d: "Showing 1 to 5 of 5 entries"
        in d.find_element(By.CSS_SELECTOR, "#example_info").text
    )

    # Verify the table content
    rows = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
    assert len(rows) == 5, f"Expected 5 entries, but found {len(rows)}"

    # Verify the filter info text
    info_text = driver.find_element(By.CSS_SELECTOR, "#example_info").text
    assert (
        info_text == "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
    ), f"Unexpected info text: {info_text}"

    print("Test Passed!")
