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
input_file_path = 'purchase_orders.csv'  # Your input CSV file name
output_file_path = 'final_purchase_order.csv'  # Output CSV file name

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
