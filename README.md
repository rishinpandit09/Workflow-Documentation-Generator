# 8-Day Weather Forecast Extractor with Network Log Analysis

This project automates the process of capturing network logs and extracting weather forecast data for a specific city from the **OpenWeatherMap** website. It identifies forecast-related API calls and parses the HTML to retrieve data into PDF.

---

## Project Overview

The project performs the following tasks:

### 1. Capture Network Logs
- Monitors all network requests made while interacting with the **OpenWeatherMap** website.
- Identifies relevant API calls related to weather forecasts.

### 2. Analyze API Calls
- Scans and analyzes captured network logs.
- Identifies and displays forecast API URLs used by the OpenWeatherMap website.

---

## Technologies Used

- **Python** (3.x)
- **Selenium WebDriver** (for browser automation)
- **ChromeDriver** (to interact with Google Chrome)
- **JSON** (to parse network logs)
- **Web Scraping** (XPath, CSS Selectors)

