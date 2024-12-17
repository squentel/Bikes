import random
from datetime import datetime, timedelta

def generate_random_timestamp():
    """Generate a random timestamp in the past 7 days in the format '%Y-%m-%dT%H-%M-%S'."""
    # Get the current time
    current_time = datetime.now()
    
    # Generate a random number of days and seconds within the past 7 days
    days_ago = random.randint(0, 6)  # 0 to 6 days ago
    seconds_ago = random.randint(0, 86399)  # 0 to 86399 seconds in a day
    
    # Subtract the random time from the current time
    random_timestamp = current_time - timedelta(days=days_ago, seconds=seconds_ago)
    
    # Format the timestamp as '%Y-%m-%dT%H-%M-%S'
    formatted_timestamp = random_timestamp.strftime("%Y-%m-%dT%H-%M-%S")
    return formatted_timestamp
