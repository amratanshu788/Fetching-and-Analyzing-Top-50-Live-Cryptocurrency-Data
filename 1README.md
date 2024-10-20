# Fetching-and-Analyzing-Top-50-Live-Cryptocurrency-Data
This project fetches live cryptocurrency data for the top 50 cryptocurrencies by market capitalization using the CoinGecko API. The data is continuously updated in an Excel sheet and analyzed to extract useful insights, including:
Top 5 cryptocurrencies by market capitalization.
Average price of the top 50 cryptocurrencies.
Highest and lowest 24-hour percentage price change among the top 50.
The project is written in Python and utilizes xlwings to keep an Excel sheet updated with live cryptocurrency data every 5 minutes.

Features
Fetches live data including cryptocurrency name, symbol, current price, market capitalization, 24-hour trading volume, and 24-hour percentage price change.
Calculates key insights and provides analysis of the top 50 cryptocurrencies.
Updates an Excel sheet in real-time (every 5 minutes).

Requirements
Before running the project, ensure you have the following installed:
Python 3.x
Virtual environment setup (optional but recommended)
Required Python libraries: pandas, xlwings, pycoingecko

Analysis Performed
Top 5 Cryptocurrencies: Based on market capitalization.
Average Price: The average price of the top 50 cryptocurrencies.
Highest and Lowest Percentage Change: Identifies the cryptocurrencies with the highest and lowest 24-hour percentage price change.
Output
Excel Sheet: The output data is written to an Excel sheet, which is updated every 5 minutes.
Report: You can create a report summarizing the key insights from the analysis.
Known Issues
Ensure Microsoft Excel is installed and properly registered for COM access if using xlwings.

If you encounter issues with Excel, consider switching to an alternative method for Excel interaction.
Contact
For any issues or queries, feel free to contact me at:
Amratanshu 
amratanshuchakrawarti9415@gmail.com
