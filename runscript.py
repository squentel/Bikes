import subprocess
import os

# Script to run (replace with the actual name of your script in the same folder)
script_full_path="YOUR_SCRIPT_PATH"


# Number of times to run the script
iterations = 5

# Check if the script exists before running
if not os.path.isfile(script_full_path):
    print(f"Error: The script '{script_to_run}' does not exist in the current directory.")
else:
    for i in range(1, iterations + 1):
        print(f"Running iteration {i}...")
        try:
            # Run the script and wait for it to finish
            subprocess.run(["python3", script_full_path], check=True)
            print(f"Iteration {i} completed successfully.\n")
        except subprocess.CalledProcessError as e:
            print(f"Error during iteration {i}: {e}")
            break  # Stop the loop if the script fails
        except FileNotFoundError:
            print(f"Error: Python interpreter not found or script missing.")
            break
