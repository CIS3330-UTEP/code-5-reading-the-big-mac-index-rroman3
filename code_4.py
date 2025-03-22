import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def load_data():
    df = pd.read_csv(big_mac_file)
    df['year'] = df['date'].str[:4]
    return df

def get_big_mac_price_by_year(year, country_code): 
    df = load_data()
    df = df[(df['year'] == str(year)) & (df['iso_a3'].str.lower() == country_code.lower())]
    if df.empty:
        return None
    return round(df['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    df = load_data()
    df = df[df['iso_a3'].str.lower() == country_code.lower()]
    if df.empty:
        return None
    return round(df['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    df = load_data()
    df = df[df['year'] == str(year)]
    if df.empty:
        return None
    cheapest = df.iloc[df['dollar_price'].idxmin()]
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"
    
def get_the_most_expensive_big_mac_price_by_year(year):
    df = load_data()
    df = df[df['year'] == str(year)]
    if df.empty:
        return None
    expensive = df.iloc[df['dollar_price'].idxmax()]
    return f"{expensive['name']}({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    while True:
        print("1. Get Big Mac price by year and country code")
        print("2. Get Big Mac price by country code")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            year = input("Enter year:(YYY): ")
            country_code = input("Enter country code (lowercase): ")    
            price = get_big_mac_price_by_year(year, country_code)
            if price is not None:
                print(f"Big Mac price: ${price}")
            else:
                print('Data not found')

        elif choice == '2':
            country_code = input("Enter country code (lowercase): ")
            price = get_big_mac_price_by_country(country_code)
            if price is not None:
                print(f"Big Mac price: ${price}")
            else:
                print('Data not found')

        elif choice == '3':
            year = input("Enter year:(YYY): ")
            result = get_the_cheapest_big_mac_price_by_year(year)
            print(f"The cheapest Big Mac price in {year}: {price}" if price else "No data found")

        elif choice == '4':
            year = input("Enter year:(YYY): ")
            result = get_the_most_expensive_big_mac_price_by_year(year)
            print(f"The most expensive Big Mac price in {year}: {price}" if price else "No data found")

        elif choice == '5':
            print("My pleasure! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

