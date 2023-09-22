import csv
import random

# Define the number of rows you want
num_rows = 100000000000000000000  # You can change this number as needed

# Create a list to store the data
data = []

# Generate random data for the CSV file
for _ in range(num_rows):
    name = f"Product {_}"
    product_type = random.choice(["Electronics", "Clothing", "Home Decor", "Books", "Toys & Games"])
    category = random.choice(["Electronics & Gadgets", "Apparel & Fashion", "Home & Garden", "Books & Literature", "Toys & Games"])
    price = round(random.uniform(5.0, 500.0), 2)
    quantity = random.randint(1, 100)


    data.append([name, product_type, category, price, quantity])

# Specify the name of the CSV file
csv_file = "large_data.csv"

# Write the data to the CSV file
with open(csv_file, mode="w", newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["name", "type", "category", "price", "quantity"])
    # Write the data rows
    writer.writerows(data)

print(f"CSV file '{csv_file}' with {num_rows} rows has been created.")
