'''
This module contains a list of default paths to use within the project
'''
import os
dataset_directory = "./massive-dataset/1.1/data"
partitioned_dataset_directory = "./partitioned-datasets"
processed_dataset_directory = "./processed-dataset"
english_dataset_path = os.path.join(dataset_directory, "en-US.jsonl")
kiswahili_dataset_path = os.path.join(dataset_directory, "sw-KE.jsonl")
german_dataset_path = os.path.join(dataset_directory, "de-DE.jsonl")
