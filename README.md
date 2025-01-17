# Web Scraping Books

This project demonstrates a Python script that scrapes book information from the website [Books to Scrape](https://books.toscrape.com). It extracts details about books such as their title, price, availability, and links to their pages. The collected data is then saved into a CSV file for further analysis or usage.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Output](#output)
7. [License](#license)

---

## Overview

The script uses Python libraries like `requests` and `BeautifulSoup` to scrape the website's data. It iterates through pages until no more books are found and outputs the results into a CSV file (`books.csv`).

---

## Features

- Scrapes multiple pages from [Books to Scrape](https://books.toscrape.com).
- Collects the following details for each book:
  - **Title**
  - **Price**
  - **Stock Status**
  - **Direct Link**
- Saves the data into a clean and structured CSV file (`books.csv`).

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
