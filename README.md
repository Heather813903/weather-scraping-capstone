# weather-scraping-capstone
CTD Python Data Analysis Web Scraping Capstone


## Project Overview

This project uses Selenium to collect weather data from Time and Date's Weather Around the World website and Pandas to clean and transform the data.

## Data Collected

- City
- Country
- Temperature (°F)
- Wind Speed (mph)

## Setup

This project uses Python 3.13 and the following packages:

```bash
pip install selenium webdriver-manager pandas
```

## How to Run

Run the scraping script:

```bash
python get_weather.py
```

This creates a raw CSV file named `weather_raw.csv`.

Run the data cleaning script:

```bash
python clean_weather.py
```

## Data Cleaning

- Check for missing values and duplicates.
- Remove measurement units.
- Convert temperature and wind speed to numeric values.
- Remove malformed entries.
- Display data before and after cleaning.

## Current Progress

The initial scrape collected 141 records. All 141 records were retained after cleaning.

The raw CSV is generated locally and is not currently included in the repository pending clarification of data redistribution permissions.

## Data Source

https://www.timeanddate.com/weather/
