# Import the csv module (not used, but can be used for alternative CSV handling)
import csv

# Import the pandas library to work with dataframes
import pandas as pd

# Define the path to the Big Mac data CSV file
big_mac_file = './big-mac-full-index.csv'

# Function to load the CSV data into a pandas DataFrame
def load_data():
    return pd.read_csv(big_mac_file)

# Function to calculate the average Big Mac price in a specific year and country
def get_big_mac_price_by_year(year, country_code): 
    data = load_data()  # Load the CSV data
    total = 0  # Total to hold the sum of prices
    count = 0  # Counter to count matches
    for row in data.values:  # Loop through each row of the dataset
        year_str = str(row[0])  # Get the date string (e.g., 2008-01-01)
        if year_str.startswith(str(year)):  # If it matches the year
            if row[1].lower() == country_code.lower():  # If it matches the country code (case-insensitive)
                total += row[6]  # Add the dollar price
                count += 1  # Increment match count
    if count == 0:
        return None  # Return None if no matching records found
    return round(total / count, 2)  # Calculate and return the average price rounded to 2 decimals

# Function to calculate the average Big Mac price for a country across all years
def get_big_mac_price_by_country(country_code):
    data = load_data()  # Load the data
    total = 0  # Sum of prices
    count = 0  # Count of matching records
    for row in data.values:
        if row[1].lower() == country_code.lower():  # Match country code
            total += row[6]  # Add dollar price
            count += 1  # Count match
    if count == 0:
        return None  # Return None if no matches
    return round(total / count, 2)  # Return average

# Function to find the country with the cheapest Big Mac in a given year
def get_the_cheapest_big_mac_price_by_year(year):
    data = load_data()  # Load data
    data['year'] = data['date'].str[:4]  # Extract year from date and create new column
    filter = data[data['year'] == str(year)]  # Filter rows for the given year
    if len(filter) == 0:
        return None  # Return None if no data for year
    min_index = filter['dollar_price'].idxmin()  # Get index of lowest dollar_price
    row = filter.loc[min_index]  # Get row from the dataframe using the index
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"  # Format and return result string

# Function to find the country with the most expensive Big Mac in a given year
def get_the_most_expensive_big_mac_price_by_year(year):
    data = load_data()  # Load data
    data['year'] = data['date'].str[:4]  # Extract year from date and add a 'year' column
    filter = data[data['year'] == str(year)]  # Filter data for the given year
    if len(filter) == 0:
        return None  # Return None if no entries match
    max_index = filter['dollar_price'].idxmax()  # Find index of highest dollar_price
    row = filter.loc[max_index]  # Access row with highest price using .loc
    return f"{row['name']}({row['iso_a3']}): ${round(row['dollar_price'], 2)}"  # Return formatted result

# Main user interface for the program
if __name__ == "__main__":
    while True:
        # Display menu options
        print("\nChoose an option:")
        print("1. Get Big Mac price by year and country code")
        print("2. Get Big Mac price by country code")
        print("3. Get the cheapest Big Mac price by year")
        print("4. Get the most expensive Big Mac price by year")
        print("5. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            year = input("Enter year (YYYY): ")
            country_code = input("Enter country code (lowercase): ")
            price = get_big_mac_price_by_year(year, country_code)  # Get average Big Mac price for a year and country
            if price is not None:
                print(f"Big Mac price: ${price}")
            else:
                print("No data found")

        elif option == '2':
            country_code = input("Enter country code (lowercase): ")
            price = get_big_mac_price_by_country(country_code)  # Get average Big Mac price for a country
            if price is not None:
                print(f"Big Mac price: ${price}")
            else:
                print("No data found")

        elif option == '3':
            year = input("Enter year (YYYY): ")
            result = get_the_cheapest_big_mac_price_by_year(year)  # Find the cheapest Big Mac for that year
            if result is not None:
                print(result)
            else:
                print("No data found")

        elif option == '4':
            year = input("Enter year (YYYY): ")
            result = get_the_most_expensive_big_mac_price_by_year(year)  # Find the most expensive Big Mac for that year
            if result is not None:
                print(result)
            else:
                print("No data found")

        elif option == '5':
            print("Exiting...")
            break  # End loop and program

        else:
            print("Invalid option. Please try again.")
