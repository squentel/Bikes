import csv
import random

# Data for vendors and their components
vendors = {
    "Trek Bikes": [
        ("Road Bike Wheelset", 450),
        ("Carbon Brake Pads", 30),
        ("Handlebar Tape", 20),
        ("Chainring Set", 150),
        ("Saddle", 90),
        ("Derailleur", 120),
        ("Cassette", 80),
        ("Crankset", 250),
        ("Pedals", 60),
        ("Brake Levers", 100),
    ],
    "Specialized Bikes": [
        ("Road Bike Wheelset", 500),
        ("Disc Brake Pads", 40),
        ("Handlebar Tape", 25),
        ("Chainring Set", 170),
        ("Saddle", 95),
        ("Derailleur", 130),
        ("Cassette", 85),
        ("Crankset", 270),
        ("Pedals", 65),
        ("Brake Levers", 110),
    ],
    "Giant Bicycles": [
        ("Road Bike Wheelset", 420),
        ("Hydraulic Brake Pads", 35),
        ("Handlebar Tape", 22),
        ("Chainring Set", 160),
        ("Saddle", 88),
        ("Derailleur", 115),
        ("Cassette", 75),
        ("Crankset", 260),
        ("Pedals", 55),
        ("Brake Levers", 105),
    ]
}

# Generate a random purchase order number
def generate_po_number():
    return f"PO-{random.randint(10000, 99999)}"

# Create a purchase order for one bike assembly
def create_purchase_order(vendor, components):
    po_number = generate_po_number()
    bike_order = [
        {"PO Number": po_number, "Vendor": vendor, "Component": component[0], "Quantity": 1, "Unit Price": component[1]}
        for component in components
    ]
    return bike_order

# Combine purchase orders for all vendors
purchase_orders = []
for vendor, components in vendors.items():
    purchase_orders.extend(create_purchase_order(vendor, components))

# Writing the purchase order to a CSV file
po_file_path = "purchase_order.csv"
with open(po_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["PO Number", "Vendor", "Component", "Quantity", "Unit Price"])
    # Write the header
    writer.writeheader()
    # Write the data
    for order in purchase_orders:
        writer.writerow(order)

print(f"Purchase order file created: {po_file_path}")
