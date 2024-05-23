import requests
import csv
import time
from datetime import datetime

# Define the URL for the API endpoint
url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'


# Functions to get Bitcoin price
def get_bitcoin_price():
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bpi']['USD']['rate-float']
        return price
    except Exception as e:
        print(f"Error fetching data:) {e}")
        return None
    

# Function to write data to CSV
def write_to_csv(timesstamp, price):
    with open('bitcoin_prices.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timesstamp,price])


#Main function to fetch price
def main():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    price = get_bitcoin_price        
    if price:
        write_to_csv(timestamp, price)
        print(f"Recorded at {timestamp}: ${price}")
    else:
        print(f"Failed to record at {timestamp}")


if __name__ == "__main__":
  main()

    




