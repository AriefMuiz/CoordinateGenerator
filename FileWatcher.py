#version 2.0(WorkingCode)

import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import numpy as np
import os
import time  # Add this import for time module
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import pandas as pd

gis = GIS("https://www.arcgis.com", "username", "password")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith(".txt"):
            print(f"File '{event.src_path}' has been added.")
            # Read the text file and extract data
            file_path = event.src_path  # Full path to the newly added file
            print(f"File '{file_path}'")  # Correct indentation here
            x_array, y_array = read_text_file(file_path)
            print("X Array:", x_array)
            print("Y Array:", y_array)
            json_data = generate_json(x_array, y_array)
            print("Generated JSON:", json.dumps(json_data, indent=2))
            result = add_data_to_FeaturLayer(json_data)
            print(result)

def read_text_file(file_path):
    x_data = []
    y_data = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the first line
        for line in file:
            if line.strip():  # Check if the line is not empty
                x, y = map(float, line.split('\t'))
                x_data.append(x)
                y_data.append(y)
    return np.array(x_data), np.array(y_data)

def generate_json(x_array, y_array):
    json_data = []
    for x, y in zip(x_array, y_array):
        item = {
            "attributes": {
                "x": x,
                "y": y
            }
        }
        json_data = item
    return json_data

def add_data_to_FeaturLayer(json_data):
    Find_FeatureLayer= gis.content.search("TestingLayer", "Feature Layer")
    FeatureLayer_Item = Find_FeatureLayer[0]
    FeatureLayer = FeatureLayer_Item.layers[0]
    FeatureLayer_FeatureSet = FeatureLayer.query()
    Add_Result = FeatureLayer.edit_features(adds = [json_data])
    Update_Result = FeatureLayer.edit_features(updates=FeatureLayer_FeatureSet.features)
    print(Update_Result)
    return Update_Result
	

if __name__ == "__main__":
    path = r"FeatureData"  # Path to the directory to watch
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
