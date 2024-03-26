import subprocess
import random
import time
import os

def run_randomly():
    # Path to the .py program
    program_path = "GenerateCoordinate.py"
    
    # Generate a random time delay between 1 to 10 seconds
    delay = random.randint(1, 10)
    
    print(f"Waiting for {delay} seconds before running the program...")
    time.sleep(delay)
    
    # Check if the file exists
    if os.path.exists(program_path):
        # Run the program
        subprocess.run(["python", program_path])
    else:
        print("Error: The specified program path does not exist.")

if __name__ == "__main__":
    run_randomly()
