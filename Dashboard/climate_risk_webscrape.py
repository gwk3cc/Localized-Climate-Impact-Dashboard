#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Created on Sat Sep 21 23:59:24 2024

@author: garrettkent

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Step 1: Set up the Safari WebDriver
driver = webdriver.Safari()  # No need to specify a path since Safari has a built-in WebDriver

# Step 2: Open the webpage
url = 'https://projects.propublica.org/climate-migration/'
driver.get(url)

# Step 3: Wait for the page to load
time.sleep(5)  # Adjust the sleep time if needed based on the page load time

# Step 4: Find the table by class or id (adjust according to the page structure)
# Here, I'm using XPath as an example. Modify it based on your inspection of the HTML structure
table = driver.find_element(By.XPATH, '//*[@id="doom-table"]')

# Step 5: Extract headers and rows
headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]
rows = []
for row in table.find_elements(By.TAG_NAME, "tr"):
    cols = [col.text for col in row.find_elements(By.TAG_NAME, "td")]
    if cols:
        rows.append(cols)

# Step 6: Create a DataFrame and save the table
climate_risk_df = pd.DataFrame(rows, columns=['County','Heat','Wet Bulb','Farm Crop Yields','Sea Level Rise','Very Large Fires','Economic Damages','Score'])
print(climate_risk_df)

# Optional: Save to CSV
climate_risk_df.to_csv('climate_risk_table.csv', index=False)

# Close the browser
driver.quit()

# references:
# OpenAI. (2024). ChatGPT (Sep 22 version) [Large language model]. 
#    https://chat.openai.com/chat