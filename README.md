# Selenium Automation with Python

This project demonstrates how to set up and run Selenium tests using Python and Pytest. It includes integration with GitHub Actions for Continuous Integration (CI), ensuring automated testing on every push or pull request.

## Project Structure

```
automationwithpython/
├── .github/
│   └── workflows/
│       └── build.yml         # GitHub Actions workflow for running tests
├── tests/
│   ├── seleniumwithpytest.py  # Your main Selenium test script
│   └── conftest.py            # Configuration for pytest fixtures
├── .gitignore                 # Ignore files/folders for Git
├── README.md                  # Documentation for the project
├── requirements.txt           # List of dependencies
└── build.yml                  # GitHub Actions configuration file
```

## Prerequisites

- **Python**: You need Python 3.x installed on your machine. Download from the [official Python website](https://www.python.org/downloads/).
- **Visual Studio Code (VSCode)**: Recommended IDE. Download from [here](https://code.visualstudio.com/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/automationwithpython.git
    cd automationwithpython
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Install the necessary WebDriver for your browser, or use `webdriver-manager` to manage drivers automatically.

    ```bash
    pip install webdriver-manager
    ```

## Usage

### Running Tests Locally

To run the tests locally, you can use the following command in your terminal:

```bash
pytest -v --tb=short tests/
```

This will run all tests in the `tests` directory, outputting verbose test results with shortened tracebacks.

### Running Tests with GitHub Actions

When you push your changes to GitHub, the GitHub Actions workflow defined in `.github/workflows/build.yml` will automatically trigger, running all tests in the `tests` directory. You can view the results in the **Actions** tab of your GitHub repository.

### Example Test

Here’s an example of a simple test for the Playground homepage:

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()

def test_title(driver):
    url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    driver.get(url)

    # Maximize the window
    driver.maximize_window()

    # Validate page title
    assert "Selenium Grid Online | Run Selenium Test On Cloud" in driver.title, "Page title does not match"
```

### Test Fixtures

In `conftest.py`, you can define reusable fixtures for setting up WebDriver instances, which can be shared across multiple test files:

```python
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
```

## GitHub Actions CI/CD

The GitHub Actions workflow defined in `.github/workflows/build.yml` will automatically:

- Set up Python and dependencies.
- Run all tests with `pytest`.
- Show detailed results in the GitHub Actions interface.

### Example `build.yml` Workflow

```yaml
name: Selenium Test Automation

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  selenium-tests:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        browser: [chrome, firefox]

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest selenium webdriver-manager

      - name: Run Selenium tests
        env:
          BROWSER: ${{ matrix.browser }}
        run: |
          pytest -v --tb=short tests/

```

This workflow ensures your tests are run automatically with each push or pull request to the `main` branch.

## Requirements

The project dependencies are listed in `requirements.txt`:

```
selenium
pytest
webdriver-manager
```

You can install them using the following command:

```bash
pip install -r requirements.txt
```


