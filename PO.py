import csv
import random

# Data for vendors and their components with three versions of each component
vendors = {
    "Trek Bikes": [
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

# Create a purchase order for components with different versions
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

# Writing the purchase order to a new CSV file
po_file_path = "purchase_order_with_component_versions.csv"
with open(po_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["PO Number", "Vendor", "Component", "Quantity", "Unit Price"])
    # Write the header
    writer.writeheader()
    # Write the data
    for order in purchase_orders:
        writer.writerow(order)

print(f"Purchase order file created: {po_file_path}")
