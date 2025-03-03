import requests
import pandas as pd
import time

# Function to fetch live data from CoinGecko API
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        # Create DataFrame with required fields
        df = pd.DataFrame(data, columns=['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h'])
        df.columns = ['Name', 'Symbol', 'Current Price (USD)', 'Market Cap (USD)', '24h Volume (USD)', '24h Price Change (%)']
        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to analyze data
def analyze_data(df):
    if df is None:
        return None
    # 1. Top 5 by market cap
    top_5_market_cap = df.nlargest(5, 'Market Cap (USD)')[['Name', 'Market Cap (USD)']]
    # 2. Average price
    average_price = df['Current Price (USD)'].mean()
    # 3. Highest and lowest 24h price change
    highest_change = df.nlargest(1, '24h Price Change (%)')[['Name', '24h Price Change (%)']]
    lowest_change = df.nsmallest(1, '24h Price Change (%)')[['Name', '24h Price Change (%)']]
    return top_5_market_cap, average_price, highest_change, lowest_change

# Main execution
if __name__ == "__main__":
    # Fetch data
    crypto_data = fetch_crypto_data()
    if crypto_data is not None:
        # Save to CSV for Excel
        crypto_data.to_csv('crypto_data.csv', index=False)
        print("Data saved to crypto_data.csv")

        # Analyze data
        analysis = analyze_data(crypto_data)
        if analysis:
            top_5_market_cap, average_price, highest_change, lowest_change = analysis
            # Display results
            print("\nTop 5 Cryptocurrencies by Market Cap:")
            print(top_5_market_cap.to_string(index=False))
            print(f"\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")
            print("\nHighest 24h Price Change:")
            print(highest_change.to_string(index=False))
            print("\nLowest 24h Price Change:")
            print(lowest_change.to_string(index=False))

            # Save analysis to text file
            with open('analysis_summary.txt', 'w') as f:
                f.write("Top 5 Cryptocurrencies by Market Cap:\n")
                f.write(top_5_market_cap.to_string(index=False))
                f.write(f"\n\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")
                f.write("\n\nHighest 24h Price Change:\n")
                f.write(highest_change.to_string(index=False))
                f.write("\n\nLowest 24h Price Change:\n")
                f.write(lowest_change.to_string(index=False))
            print("\nAnalysis saved to analysis_summary.txt")