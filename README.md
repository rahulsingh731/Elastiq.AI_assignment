# Elastiq.AI_assignment

## Overview
This repository contains a Selenium automation script written in Python to validate the search functionality on the [Selenium Playground Table Sort Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo). The script uses Selenium WebDriver and Python's `pytest` framework for test case execution.

---

## Prerequisites

### Tools and Libraries
1. **Python 3.8+**
2. **Selenium**
   ```bash
   pip install selenium
   ```
3. **pytest** (for test case execution)
   ```bash
   pip install pytest
   ```
4. **Google Chrome** (latest version)
5. **ChromeDriver** compatible with the installed version of Chrome.

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/rahulsingh731/Elastiq.AI_assignment.git
cd Elastiq.AI_assignment
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Setup ChromeDriver
- Download the ChromeDriver that matches your Chrome version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
- Place the `chromedriver.exe` file in the `drivers/` folder or update the path in the script.

### Step 4: Run the Test
Execute the test using `pytest`:
```bash
pytest -s qa_selenium_test.py
```

---

## Script Details

### **`qa_selenium_test.py`**

The script:
1. Navigates to the Selenium Playground Table Sort Search Demo.
2. Locates the search input field and enters "New York."
3. Waits for the table results to filter and validates:
   - The number of rows displayed is 5.
   - The informational text matches expectations.
4. Asserts all conditions and prints "Test Passed" if successful.

### Key Highlights
- **Headless Mode:** The WebDriver is configured to run in headless mode for CI/CD integration.
- **Dynamic Locators:** Uses `WebDriverWait` and robust CSS selectors for reliable element interaction.

---

## Example Output
### Successful Execution
```
Navigating to page...
Locating search field...
Waiting for results...
Validating table rows...
Validating info text...
Test Passed!
```

### Failure Example
```
Test Failed: Expected 5 entries, but found 3
```

---

## Troubleshooting

### Common Issues
1. **ChromeDriver Path Error:**
   Ensure the correct ChromeDriver path is specified in the script:
   ```python
   service = Service(os.getenv("CHROMEDRIVER_PATH", "drivers/chromedriver.exe"))
   ```

2. **Timeouts:**
   Increase the WebDriverWait timeout if the website is slow to load:
   ```python
   WebDriverWait(driver, 20)
   ```

3. **Environment Issues:**
   Verify the Python and Chrome versions are compatible.

---
