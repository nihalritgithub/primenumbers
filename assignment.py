# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setting up the driver
driver = webdriver.Chrome()
driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")

# Waiting for the page to load
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.posting-list div.posting-item")))

# Scraping the first 5 postings
postings = driver.find_elements_by_xpath("//table[@class='datatable table table-striped table-bordered dataTable no-footer']//tbody/tr")[:5]

# Extracting the required fields from each posting
for posting in postings:
    post_date = posting.find_element_by_xpath(".//td[@aria-label='Post Date']").text
    bid_request_name = posting.find_element_by_xpath(".//td[@aria-label='Bid/Request Name']").text
    bid_closing_date = posting.find_element_by_xpath(".//td[@aria-label='Bid Closing Date']").text
    
    # Printing the extracted fields
    print("Post Date:", post_date)
    print("Bid/Request Name:", bid_request_name)
    print("Bid Closing Date:", bid_closing_date)
    print("--------------------------------------------------")

# Closing the driver
driver.quit()
