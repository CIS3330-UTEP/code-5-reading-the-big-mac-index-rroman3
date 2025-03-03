import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

def load_data():
    df = pd.read_csv(big_mac_file)
    df['year'] = df['date'].str[:4].astype(int)  # Ensure year is an integer
    df = df[df['dollar_price'].notnull()]  # Remove rows where dollar_price is NaN
    df['iso_a3'] = df['iso_a3'].str.lower()  # Normalize country codes to lowercase
    return df

def get_big_mac_price_by_year(year, country_code):
    df = load_data()
    year = int(year)
    country_code = country_code.lower()
    df = df[(df['year'] == year) & (df['iso_a3'] == country_code)]
    
    if df.empty:
        return None
    
    # If multiple prices exist for the same year, take the average
    return round(df['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    df = load_data()
    country_code = country_code.lower()
    
    # Find the most recent year available for this country
    country_df = df[df['iso_a3'] == country_code]
    if country_df.empty:
        return None
    
    latest_year = country_df['year'].max()
    latest_df = country_df[country_df['year'] == latest_year]
    
    # Select the most recent record by date
    latest_df = latest_df.sort_values(by='date', ascending=False)
    return round(latest_df.iloc[0]['dollar_price'], 2)

def get_the_cheapest_big_mac_price_by_year(year):
    df = load_data()
    year = int(year)
    df = df[df['year'] == year]
    if df.empty:
        return None
    cheapest = df.nsmallest(1, 'dollar_price').iloc[0]  # Get the row with the lowest price
    return f"{cheapest['name']}({cheapest['iso_a3'].upper()}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = load_data()
    year = int(year)
    df = df[df['year'] == year]
    if df.empty:
        return None
    most_expensive = df.nlargest(1, 'dollar_price').iloc[0]  # Get the row with the highest price
    return f"{most_expensive['name']}({most_expensive['iso_a3'].upper()}): ${round(most_expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Get Big Mac price by year and country code")
        print("2. Get Big Mac price by country code")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            year = input("Enter year (YYYY): ")
            country_code = input("Enter country code: ")
            price = get_big_mac_price_by_year(year, country_code)
            print(f"Big Mac price: ${price}" if price else "No data found")

        elif option == '2':
            country_code = input("Enter country ISO code: ")
            price = get_big_mac_price_by_country(country_code)
            print(f"Big Mac price: ${price}" if price else "No data found")

        elif option == '3':
            year = input("Enter year (YYYY): ")
            price = get_the_cheapest_big_mac_price_by_year(year)
            print(f"The cheapest Big Mac price in {year}: {price}" if price else "No data found")

        elif option == '4':
            year = input("Enter year (YYYY): ")
            price = get_the_most_expensive_big_mac_price_by_year(year)
            print(f"The most expensive Big Mac price in {year}: {price}" if price else "No data found")
        
        elif option == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")
