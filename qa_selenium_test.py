from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Setup
options = Options()
# options.add_argument("--incognito")
from selenium.webdriver.chrome.service import Service
service = Service('C:/Users/Rahul/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

def test_table_search():
    try:
        # Navigate to the page
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

        # Wait for the search field
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#example_filter input")))
        
        # Perform search
        search_field = driver.find_element(By.CSS_SELECTOR, "#example_filter input")
        search_field.send_keys("New York")

        # Wait for the filtered results to load
        WebDriverWait(driver, 10).until(
            lambda d: "Showing 1 to 5 of 5 entries" in d.find_element(By.CSS_SELECTOR, "#example_info").text
        )

        # Verify the table content
        elements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
        assert len(elements) == 5, f"Expected 5 entries, but got {len(elements)}"

        # Verify the filter info text
        info_text = driver.find_element(By.CSS_SELECTOR, "#example_info").text
        assert info_text == "Showing 1 to 5 of 5 entries (filtered from 24 total entries)", f"Unexpected info text: {info_text}"

        print("Test Passed")

    except Exception as e:
        print("Test Failed:", str(e))

    finally:
        time.sleep(5)
        driver.quit()

# Run the test
test_table_search()
