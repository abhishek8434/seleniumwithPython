import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize WebDriver using Chrome
driver = webdriver.Chrome()  # No need to specify executable_path; it's handled by chromedriver-py

# Open a webpage
driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

# Print the title of the webpage
print(driver.title)

# Find the search bar using its xpath
searchxpath = "/html/body/div[1]/div/section[2]/div/div/div/div/div[2]/label/input";

search_box = driver.find_element(By.XPATH, searchxpath)

# Type a search query into the search bar
search_box.send_keys("New York")

# Submit the search form (equivalent to pressing the 'Enter' key)
search_box.send_keys(Keys.RETURN)

# Locate the element that contains the text
message_element = driver.find_element(By.CSS_SELECTOR, "#example_info")  # Adjust selector as needed

# Get the actual text from the element
actual_text = message_element.text

# Define the expected text
expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"

# Verify if the actual text matches the expected text
if actual_text == expected_text:
    print(f"Text verified successfully!")
else:
    print(f"Text verification failed! Expected: {expected_text}, but got: {actual_text}")

# Optionally, wait for some time for results to load
#driver.implicitly_wait(5)

# Wait for 2 seconds before closing the browser
time.sleep(2)

# Close the browser
driver.quit()
