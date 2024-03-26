import random
import time
import uuid
import os


def generate_coordinates():
    # Define the latitude and longitude boundaries of Malaysia
    min_longitude = 1  # Southernmost point of Malaysia
    max_longitude = 6  # Northernmost point of Malaysia
    min_latitude = 100  # Westernmost point of Malaysia
    max_latitude = 105  # Easternmost point of Malaysia
    
    # Generate random latitude and longitude within the boundaries
    latitude = random.uniform(min_latitude, max_latitude)
    longitude = random.uniform(min_longitude, max_longitude)
    return latitude, longitude

def generate_unique_filename(directory):
    filename = str(uuid.uuid4()) + ".txt"
    return os.path.join(directory, filename)

def generate_txt_file(file_path):
    x, y = generate_coordinates()
    content = f"x\ty\n{x}\t{y}"
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    directory = "FeatureData"
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        print(f"Error creating directory: {e}")
        return
    
    while True:
        # Generate a unique filename
        file_path = generate_unique_filename(directory)
        
        # Generate and write to the text file
        generate_txt_file(file_path)
        print(f"File generated at path: {file_path}")
        
        # Generate a random time delay
        time_delay = random.randint(1, 10)
        print(f"Waiting for {time_delay} seconds...")
        
        # Sleep for the random time delay
        time.sleep(time_delay)

        # At this point, the sleep is finished, so the loop will iterate again

if __name__ == "__main__":
    main()
