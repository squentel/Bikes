import subprocess

# Script to run (replace 'target_script.py' with your actual script name)
script_to_run = "target_script.py"

# Number of times to run the script
iterations = 500

for i in range(1, iterations + 1):
    print(f"Running iteration {i}...")
    try:
        # Run the script and wait for it to finish
        subprocess.run(["python", script_to_run], check=True)
        print(f"Iteration {i} completed successfully.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error during iteration {i}: {e}")
        break  # Optionally stop if an error occurs
    except FileNotFoundError:
        print(f"Error: Script '{script_to_run}' not found.")
        break
