import csv
import random
import time
import os
import datetime


# Data for vendors and their components
vendors = {
    "Trek Bikes": [
        ("Bike Frame Carbon Pro", 1200),
        ("Bike Frame Carbon Premium", 1400),
        ("Bike Frame Aluminum X", 900),
        ("Saddle Pro", 95),
        ("Saddle Premium", 110),
        ("Saddle X", 85),
        ("Road Bike Wheelset Pro", 450),
        ("Road Bike Wheelset Premium", 500),
        ("Road Bike Wheelset X", 420),
        ("Carbon Brake Pads Pro", 35),
        ("Carbon Brake Pads Premium", 40),
        ("Carbon Brake Pads X", 30),
    ],
    "Specialized Bikes": [
        ("Bike Frame Carbon Pro", 1250),
        ("Bike Frame Carbon Premium", 1450),
        ("Bike Frame Aluminum X", 950),
        ("Saddle Pro", 100),
        ("Saddle Premium", 120),
        ("Saddle X", 90),
        ("Road Bike Wheelset Pro", 470),
        ("Road Bike Wheelset Premium", 520),
        ("Road Bike Wheelset X", 440),
        ("Disc Brake Pads Pro", 45),
        ("Disc Brake Pads Premium", 50),
        ("Disc Brake Pads X", 40),
    ],
    "Giant Bicycles": [
        ("Bike Frame Carbon Pro", 1180),
        ("Bike Frame Carbon Premium", 1350),
        ("Bike Frame Aluminum X", 880),
        ("Saddle Pro", 92),
        ("Saddle Premium", 105),
        ("Saddle X", 88),
        ("Road Bike Wheelset Pro", 460),
        ("Road Bike Wheelset Premium", 510),
        ("Road Bike Wheelset X", 430),
        ("Hydraulic Brake Pads Pro", 38),
        ("Hydraulic Brake Pads Premium", 42),
        ("Hydraulic Brake Pads X", 35),
    ],
}

# Generate a random purchase order number
def generate_po_number():
    return f"PO-{random.randint(10000, 99999)}"

# Select a random vendor and create a purchase order with a random subset of components
def create_random_purchase_order(vendors):
    # Randomly select a vendor
    vendor = random.choice(list(vendors.keys()))
    components = vendors[vendor]

    # Randomly select a subset of components (between 1 and all available components)
    num_components = random.randint(1, len(components))  # Random number of components to select
    selected_components = random.sample(components, num_components)  # Select random components

    # Create a purchase order with random quantities for the selected components
    po_number = generate_po_number()
    bike_order = []
    for component in selected_components:
        bike_order.append({
            "PO Number": po_number,
            "Vendor": vendor,
            "Component": component[0],
            "Quantity": random.randint(1, 10),  # Random quantity between 1 and 10
            "Unit Price": component[1],
        })

    return bike_order

# Generate a single random purchase order
purchase_order = create_random_purchase_order(vendors)

# Writing the purchase order to a CSV file
po_file_path = "RENAME_WITH_DESIRED_FILEPATH"
with open(po_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["PO Number", "Vendor", "Component", "Quantity", "Unit Price"])
    # Write the header
    #writer.writeheader()
    # Write the data
    for order in purchase_order:
        writer.writerow(order)

############GENERATE GENERAL PO ###################

import csv
import random

# List of random names
names = ['Simon', 'Andrea', 'Efrain']

# Function to randomly apply a percentage increase for Simon
def apply_percentage_increase(name, total):
    if name == 'Simon' and random.randint(1, 50) == 1:  # 1 in 50 chance
        increase_percentage = random.randint(5, 10)  # Random increase between 5% and 10%
        total += total * (increase_percentage / 100)
    return total

# Read the original purchase order CSV file
input_file_path = po_file_path  # Your input CSV file name
output_file_path = "po_file_path = "RENAME_WITH_DESIRED_FILEPATH""  # Output CSV file name

# Initialize total sum
total_sum = 0

# Open and process the original CSV file
with open(input_file_path, mode='r') as infile:
    reader = csv.reader(infile)

    # Read all lines and sum the totals
    for row in reader:
        if len(row) < 3:
            continue  # Skip empty or incomplete lines
        po_number = row[0]  # PO Number (assumed to be the same for all lines)
        quantity = int(row[-2])  # Quantity (second-to-last field)
        unit_price = float(row[-1])  # Unit price (last field)
        # Calculate the total for this line (quantity * unit price)
        total_sum += quantity * unit_price

# Pick a random name
name = random.choice(names)

# Apply percentage increase for Simon (if chosen)
total_sum = apply_percentage_increase(name, total_sum)

# Write the final output to a new CSV file with the total sum and name
with open(output_file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Write the single row with the PO number, total, and name
    writer.writerow([po_number, round(total_sum, 2), name])

print(f"Final purchase order with total has been saved to {output_file_path}")
###########Rename fiels
#Renaming the PO file to add a timestamp
dt = str(datetime.datetime.now())
t = os.path.getctime(po_file_path)
t_str = time.ctime(t)
t_obj = time.strptime(t_str)
form_t = time.strftime("%Y-%m-%dT%H-%M-%S", t_obj)
os.rename(
    po_file_path, os.path.split(po_file_path)[0] + '/' + form_t + 'purchase_detail.csv')

#Renaming the global PO as well
dt = str(datetime.datetime.now())
t = os.path.getctime(output_file_path)
t_str = time.ctime(t)
t_obj = time.strptime(t_str)
form_t = time.strftime("%Y-%m-%dT%H-%M-%S", t_obj)
os.rename(
    output_file_path, os.path.split(output_file_path)[0] + '/' + form_t + 'purchase_detail.csv')
