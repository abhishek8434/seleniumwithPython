# Setting Up Selenium with Python in Visual Studio Code (VSCode)

## Project Structure
```
automationwithpython/
├── venv/                # Virtual environment (do not modify files here)
├── tests/               # Folder for your Selenium test scripts
│   └── test_script.py   # Example Python file for your Selenium code
└── README.md            # Documentation for the project
```

## Prerequisites
1. **Python**: Download and install Python from the [official Python website](https://www.python.org/). During installation, ensure the option "Add Python to PATH" is checked.
2. **Visual Studio Code**: Download and install VSCode from the [official website](https://code.visualstudio.com/).

---

## Step 1: Install Required Extensions in VSCode
1. Open VSCode.
2. Go to the Extensions view (Ctrl+Shift+X or click the Extensions icon).
3. Install the following extensions:
   - **Python** (by Microsoft)
   - **Pylance** (for IntelliSense and auto-completion)

---

## Step 2: Install Selenium
1. Open the terminal in VSCode.
2. Run the following command to install Selenium:
   ```bash
   pip install selenium
   ```

---

## Step 3: Download a WebDriver
### Option 1: Manually Download
1. Download the WebDriver for the browser you plan to use:
   - **Chrome**: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
   - **Edge**: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
2. Ensure the WebDriver is added to your system's PATH or placed in the same directory as your script.

### Option 2: Using `webdriver-manager` (Recommended)
The `webdriver-manager` library automatically downloads and manages browser drivers for you.
1. Install `webdriver-manager`:
   ```bash
   pip install webdriver-manager
   ```
2. Update your Selenium script to use `webdriver-manager`. Example for Chrome:
   ```python
   from selenium import webdriver
   from webdriver_manager.chrome import ChromeDriverManager

   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get("https://www.google.com")
   print(driver.title)
   driver.quit()
   ```
3. Example for Firefox:
    ```python
    from selenium import webdriver
    from webdriver_manager.firefox import GeckoDriverManager

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    ```
4. Example for Edge:
    ```python
    from selenium import webdriver
    from webdriver_manager.microsoft import EdgeChromiumDriverManager

    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    ```

---

## Step 4: Alternative Driver Installation Options
1. Install all major browser drivers using:
   ```bash
   pip install chromedriver-py geckodriver-autoinstaller msedge-selenium-tools[selenium]
   ```
2. Auto-install GeckoDriver using `geckodriver-autoinstaller`:
   ```python
   import geckodriver_autoinstaller
   from selenium import webdriver

   geckodriver_autoinstaller.install()
   driver = webdriver.Firefox()
   ```
3. Example for Chrome:
    ```python
    from selenium import webdriver

    driver = webdriver.Chrome()
    ```
4. Example for Edge:
    ```python
    from selenium import webdriver
    from msedge.selenium_tools import Edge, EdgeOptions

    # Set up Edge options (optional, for advanced configurations)
    edge_options = EdgeOptions()
    edge_options.use_chromium = True

    # Initialize the Edge WebDriver
    driver = Edge(executable_path="path_to_edge_driver", options=edge_options)
    ```

---

## Step 5: Write a Selenium Script
1. Create a new Python file in the `tests` folder, e.g., `test_script.py`.
2. Example script for Chrome:
   ```python
   from selenium import webdriver
   from webdriver_manager.chrome import ChromeDriverManager

   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get("https://www.google.com")
   print(driver.title)
   driver.quit()
   ```


---

## Step 6: Run the Script
1. Save the file.
2. Open the terminal in VSCode.
3. Run the script using:
   ```bash
   python tests/test_script.py
   ```

---

## Notes
- Ensure Python, Selenium, and WebDriver are correctly installed and up-to-date.
- For browser-specific setup, refer to the official documentation of the respective WebDriver.

Happy Testing!

