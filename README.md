# Cryptocurrency Live Data Fetch and Analysis

This project involves fetching live cryptocurrency data for the top 50 cryptocurrencies, analyzing the data, and presenting it in a live-updating Excel sheet. The data is fetched from the CoinGecko API and includes key metrics such as current price, market capitalization, 24-hour trading volume, and 24-hour price change. The project also includes a Python script for data fetching and analysis, an Excel sheet for live data display, and an analysis report.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Live Updating in Excel](#live-updating-in-excel)
- [Data Analysis](#data-analysis)
- [Analysis Report](#analysis-report)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

The goal of this project is to fetch live data for the top 50 cryptocurrencies by market capitalization, analyze the data, and present it in a continuously updating Excel sheet. The analysis includes identifying the top 5 cryptocurrencies by market cap, calculating the average price of the top 50 cryptocurrencies, and finding the highest and lowest 24-hour percentage price changes.

## Features

- Fetch live data from the CoinGecko API.
- Analyze key metrics such as market cap, price, and 24-hour changes.
- Present data in a live-updating Excel sheet.
- Generate an analysis report summarizing key insights.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library
- `openpyxl` library
- Excel 2016 or later (with Power Query)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/crypto-live-data-fetch.git
   cd crypto-live-data-fetch
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv  # On Windows: python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Libraries**:
   ```bash
   pip install requests pandas openpyxl
   ```

## Usage

1. **Run the Python Script**:
   ```bash
   python crypto_fetch_analyze.py
   ```
   - This will fetch live data from the CoinGecko API, save it to `crypto_data.csv`, and perform analysis.

2. **Open Excel and Load Data**:
   - Open `CryptoLiveData.xlsx` in Excel.
   - The data will be automatically fetched and loaded using Power Query.

3. **Set Up Auto-Refresh**:
   - Configure the Excel sheet to refresh data every 5 minutes (See [Live Updating in Excel](#live-updating-in-excel)).

## Live Updating in Excel

1. **Open Excel** and create a new workbook.
2. **Fetch Data with Power Query**:
   - Go to **Data > Get Data > From Web**.
   - Paste the API URL: `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false`.
   - Click **OK** and transform the data in the Power Query Editor.
3. **Set Auto-Refresh**:
   - Right-click the table in Excel > **Table Design > Properties**.
   - Check "Refresh every" and set to **5 minutes**.
   - Uncheck "Enable background refresh" for immediate updates.

## Data Analysis

The analysis performed includes:
- **Top 5 Cryptocurrencies by Market Cap**:
  - Identifies the top 5 cryptocurrencies by market cap.
- **Average Price of Top 50 Cryptocurrencies**:
  - Calculates the average current price of the top 50 cryptocurrencies.
- **Highest and Lowest 24-hour Price Change**:
  - Finds the cryptocurrencies with the highest and lowest 24-hour percentage price changes.

## Analysis Report

A brief report summarizing the key insights and analysis is generated and saved as `analysis_summary.txt`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [CoinGecko](https://www.coingecko.com/) for providing the cryptocurrency data API.
- Python and its amazing libraries (`requests`, `pandas`, `openpyxl`).
