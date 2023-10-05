'''

This module answers question 2 of the task
'''


import functions
import pandas as pd
import os
from constants import (
    partitioned_dataset_directory,
    processed_dataset_directory,
    english_dataset_path,
    kiswahili_dataset_path,
    german_dataset_path,
)
import pprint
from logging import Logger


def setup():
    functions.create_directory_if_not_exist(partitioned_dataset_directory)


def partition_datasets(dfs: list[pd.DataFrame], df_names: list["str"]):
    """
    Partitions the datasets into dev, train and test
    """

    partitions = ["dev", "train", "test"]

    for df, name in zip(dfs, df_names):
        for partition in partitions:
            partitioned_df = functions.partition_dfs(df, partition)
            export_path = os.path.join(
                partitioned_dataset_directory, f"{name}-{partition}.jsonl"
            )
            functions.df_to_jsonl(partitioned_df, export_path)


def create_processed_json():
    """
    Partitions the dataset by train and exports as a pretty printed JSON file.
    """

    files_english = os.listdir(processed_dataset_directory)

    result = []
    for file in files_english:
        file_path = os.path.join(processed_dataset_directory, file)
        try:
            df = pd.read_excel(file_path)
            df = functions.partition_dfs(df, "train")
            df = df[
                [
                    "id",
                    "utterance_translation",
                ]
            ]
            result.extend(list(df.to_dict(orient="index").values()))
        except:
            Logger().warning(f"Could not parse the file at: {file_path}")

    functions.export_list_as_json(result,'combined')


def question2():
    """
    Performs the question 2 operations
    """
    setup()
    english_df = functions.read_jsonl_file(english_dataset_path)
    kiswahili_df = functions.read_jsonl_file(kiswahili_dataset_path)
    german_df = functions.read_jsonl_file(german_dataset_path)
    dfs = [english_df, kiswahili_df, german_df]
    df_names = ["english", "kiswahili", "german"]
    partition_datasets(dfs, df_names)

    zipped_dir = functions.zip_directory(partitioned_dataset_directory, "partitioned")
    functions.upload_to_drive(zipped_dir,'partitioned')

    create_processed_json()
