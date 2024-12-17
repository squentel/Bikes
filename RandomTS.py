import random
from datetime import datetime, timedelta

def generate_random_timestamp():
    """Generate a random timestamp in the past 7 days, between 8 AM and 6 PM."""
    # Get the current time
    current_time = datetime.now()
    
    # Generate a random number of days in the past 7 days
    days_ago = random.randint(0, 6)  # 0 to 6 days ago
    
    # Generate a random time between 8:00 AM and 6:00 PM
    random_hour = random.randint(8, 17)  # Hours between 8 AM and 5 PM (last hour starts at 17)
    random_minute = random.randint(0, 59)  # Minutes: 0-59
    random_second = random.randint(0, 59)  # Seconds: 0-59
    
    # Create the random timestamp
    random_date = current_time - timedelta(days=days_ago)
    random_timestamp = random_date.replace(hour=random_hour, minute=random_minute, second=random_second)
    
    # Format the timestamp as '%Y-%m-%dT%H-%M-%S'
    formatted_timestamp = random_timestamp.strftime("%Y-%m-%dT%H-%M-%S")
    return formatted_timestamp

def main():
    # Generate and print the random timestamp
    random_timestamp = generate_random_timestamp()
    print(f"Random Timestamp: {random_timestamp}")

if __name__ == "__main__":
    main()
