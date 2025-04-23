import requests
from bs4 import BeautifulSoup
import csv
import os

# Get the URL of the site
url = "https://coinmarketcap.com/rankings/exchanges/"

# Get the response and parse it using html.parser
response = requests.get(url)

# Feed the raw response to the HTML parser using BeautifulSoup
parsedResponse = BeautifulSoup(response.text, "html.parser")

# Extract the data (find the table or specific content you're after)
# We'll use the 'table' tag, then identify the rows (tr) and columns (td)
table = parsedResponse.find('table')  # Assuming there's a table tag you want to scrape
rows = table.find_all('tr')  # Get all rows in the table

# Create the file directory
crypto_scraping_folder = "C:\\Users\\user\\Desktop\\crypto_scrapper_folder"
os.makedirs(crypto_scraping_folder, exist_ok=True)  # Ensure folder is created

# Define the file path for the CSV
crypto_file_path = os.path.join(crypto_scraping_folder, "bitcoin_scraper.csv")

# Write data to CSV file
with open(crypto_file_path, mode="w", newline="", encoding="utf-8") as file:
    # Define the headers for the CSV
    headers = ["Exchange", "Trading_volume(24hours)", "Average_Liquidity", "Weekly_visits",
               "Market_coins", "Fiat_supported"]
    writeIn = csv.writer(file)
    writeIn.writerow(headers)

    # Loop through each row in the table (skipping the header row)
    for row in rows[1:11]:
        columns = row.find_all('td')  # Find all columns in the current row
        
        if len(columns) >= 6:  # Ensure there are enough columns to match our headers
            # Extract the text from each column, strip any extra spaces
            exchange = columns[0].text.strip()
            trading_volume = columns[1].text.strip()
            average_liquidity = columns[2].text.strip()
            weekly_visits = columns[3].text.strip()
            market_coins = columns[4].text.strip()
            fiat_supported = columns[5].text.strip()

            # Write the extracted row to the CSV file
            writeIn.writerow([exchange, trading_volume, average_liquidity, weekly_visits, market_coins, fiat_supported])

print("Data extraction complete, and CSV file saved.")
