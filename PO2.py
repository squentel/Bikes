import csv
import random

# Data for vendors and their components with multiple versions, now including bike frames
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

# Select a random vendor and create a single purchase order
def create_random_purchase_order(vendors):
    # Randomly select a vendor
    vendor = random.choice(list(vendors.keys()))
    components = vendors[vendor]

    # Create a purchase order with random quantities for each component
    po_number = generate_po_number()
    
    bike_order = []
    for component in components:
        bike_order.append({
            "PO Number": po_number,
            "Vendor": vendor,
            "Component": component[0],
            "Quantity": random.randint(1, 10),
            "Unit Price": component[1],
        })
    
    return bike_order

# Generate a single random purchase order
purchase_order = create_random_purchase_order(vendors)

# Writing the purchase order to a CSV file
po_file_path = "single_purchase_order_with_bike_frames.csv"
with open(po_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["PO Number", "Vendor", "Component", "Quantity", "Unit Price"])
    # Write the header
    writer.writeheader()
    # Write the data
    for order in purchase_order:
        writer.writerow(order)

print(f"Single purchase order file created: {po_file_path}")
