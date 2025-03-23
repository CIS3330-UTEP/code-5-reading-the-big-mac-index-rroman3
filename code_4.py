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
    year = str(year)
    lowest_price = None
    name = ""
    code = ""
    for row in data.values:
        if str(row[0]).startswith(year):
            price = row[6]
            if lowest_price is None or price < lowest_price:
                lowest_price = price
                name = row[3]
                code = row[1]
    if lowest_price is None:
        return None
    return name + "(" + code + "): $" + str(round(lowest_price, 2))

def get_the_most_expensive_big_mac_price_by_year(year):
    data = load_data()
    year = str(year)
    highest_price = None
    name = ""
    code = ""
    for row in data.values:
        if str(row[0]).startswith(year):
            price = row[6]
            if highest_price is None or price > highest_price:
                highest_price = price
                name = row[3]
                code = row[1]
    if highest_price is None:
        return None
    return name + "(" + code + "): $" + str(round(highest_price, 2))

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

