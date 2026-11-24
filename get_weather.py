# Task 7 - Web Scraping Capstone

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# Set up ChromeDriver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Define the website URL
url = "https://www.timeanddate.com/weather/"

# Open the weather website
driver.get(url)

# Find the table rows
rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

# Create an empty list to store the weather data
results = []

# Extract weather data from each row
for row in rows:
    try:
        city = row.find_element(By.CSS_SELECTOR, "td.tad-weather-table__city-cell").text
        country = row.find_element(By.CSS_SELECTOR, "td.tad-weather-table__country-cell").text
        temperature = row.find_element(By.CSS_SELECTOR, "td.tad-weather-table__temperature-cell").text
        wind = row.find_element(By.CSS_SELECTOR, "td.tad-weather-table__wind-cell").text

        results.append({
            "City": city,
            "Country": country,
            "Temperature": temperature,
            "Wind Speed": wind
        })

    except NoSuchElementException:
        continue

# Close the browser
driver.quit()

# Create a DataFrame
df = pd.DataFrame(results)
print(df.head())

# Save raw weather data to CSV
df.to_csv("weather_raw.csv", index=False)