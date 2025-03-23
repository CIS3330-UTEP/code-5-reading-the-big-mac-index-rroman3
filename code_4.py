import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def load_data():
    return pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code): 
    data = load_data()
    total = 0
    count = 0
    for row in data.values:
        year_str = str(row[0])
        if year_str.startswith(str(year)):
            if row[1].lower() == country_code.lower():
                total += row[6]
                count += 1
    if count == 0:
        return None
    return round(total / count, 2)            

def get_big_mac_price_by_country(country_code):
    data = load_data()
    total = 0
    count = 0
    for row in data.values:
        if row[1].lower() == country_code.lower():
            total += row[6]
            count += 1
    if count == 0:
        return None
    return round(total / count, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    data = load_data()
    data['year'] = data['date'].str[:4]
    filter = data[data['year'] == str(year)]
    if len(filter) == 0:
        return None
    min_price = filter['dollar_price'].min()
    for i in range(len(filter)):
        if filter.iloc[i]['dollar_price'] == min_price:
            row = filter.iloc[i]
            break
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    data = load_data()
    data['year'] = data['date'].str[:4]
    filter = data[data['year'] == str(year)]
    if len(filter) == 0:
        return None
    max_price = filter['dollar_price'].max()
    for i in range(len(filter)):
        if filter.iloc[i]['dollar_price'] == max_price:
            row = filter.iloc[i]
            break
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"

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
                print("No data found")

        elif choice == '2':
            country_code = input("Enter country code (lowercase): ")
            price = get_big_mac_price_by_country(country_code)
            if price is not None:
                print(f"Big Mac price: ${price}")
            else:
                print("No data found")

        elif choice == '3':
            year = input("Enter year:(YYY): ")
            result = get_the_cheapest_big_mac_price_by_year(year)
            if result is not None:
                print(result)
            else:
                print("No data found")

        elif choice == '4':
            year = input("Enter year:(YYY): ")
            result = get_the_most_expensive_big_mac_price_by_year(year)
            if result is not None:
                print(result)
            else:
                print("No data found")

        elif choice == '5':
            print("My pleasure! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

