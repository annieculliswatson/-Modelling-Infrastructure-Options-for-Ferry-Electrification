import yaml,os
import pandas as pd

# Function to Load User Configuration File
def load_config(file_path):

    with open(file_path, 'r') as file:
        configs = yaml.safe_load(file)
    return configs