import pandas as pd
import time
from pycoingecko import CoinGeckoAPI

# Instantiate the CoinGecko API client
cg = CoinGeckoAPI()

def fetch_crypto_data():
    """
    Fetches the top 50 cryptocurrencies by market cap using CoinGecko API.
    """
    try:
        data = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page=50, page=1)
        return data
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return []

def create_dataframe(data):
    """
    Converts the fetched cryptocurrency data into a pandas DataFrame.
    """
    df = pd.DataFrame(data)
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
    df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Cap', '24h Trading Volume', '24h Price Change (%)']
    return df

def update_csv(dataframe, file_path):
    """
    Updates the CSV file with the latest cryptocurrency data.
    If the file does not exist, it creates a new one.
    """
    try:
        # Write the DataFrame to a CSV file
        dataframe.to_csv(file_path, index=False)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"Error updating CSV: {e}")

def perform_analysis(df):
    """
    Performs basic analysis on the fetched cryptocurrency data.
    """
    top_5_by_market_cap = df.nlargest(5, 'Market Cap')
    avg_price = df['Current Price (USD)'].mean()
    highest_24h_change = df.nlargest(1, '24h Price Change (%)')
    lowest_24h_change = df.nsmallest(1, '24h Price Change (%)')

    return top_5_by_market_cap, avg_price, highest_24h_change, lowest_24h_change

def main_loop(file_path):
    """
    Main loop that fetches live data, updates CSV, and performs analysis every 5 minutes.
    """
    while True:
        # Fetch live cryptocurrency data
        data = fetch_crypto_data()
        if data:
            # Create a DataFrame from the fetched data
            crypto_df = create_dataframe(data)

            # Update CSV with the live data
            update_csv(crypto_df, file_path)

            # Perform analysis on the live data
            top_5, avg_price, highest_change, lowest_change = perform_analysis(crypto_df)

            # Print the analysis results
            print("\nTop 5 Cryptocurrencies by Market Cap:\n", top_5)
            print("\nAverage Price of Top 50 Cryptocurrencies: $", round(avg_price, 2))
            print("\nHighest 24h Percentage Price Change:\n", highest_change[['Cryptocurrency Name', '24h Price Change (%)']])
            print("\nLowest 24h Percentage Price Change:\n", lowest_change[['Cryptocurrency Name', '24h Price Change (%)']])
        else:
            print("No data to update.")

        # Wait for 5 minutes before the next update
        time.sleep(300)

if __name__ == "__main__":
    # Define the path to the CSV file
    file_path = "crypto_analysis.csv"
    main_loop(file_path)
