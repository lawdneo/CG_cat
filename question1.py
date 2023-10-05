"""
This module answers question 1 on the task provided
"""


import functions
import os
import concurrent.futures
from constants import english_dataset_path, dataset_directory
from zenlog import log

english_df = functions.read_jsonl_file(english_dataset_path)
processed_directory = None



def setup(processed_dataset_dir):
    """
    Create the specified temporary directory if it does not exist
    """

    global processed_directory
    functions.create_directory_if_not_exist(processed_dataset_dir)
    processed_directory = processed_dataset_dir


def process_file(file: str) -> None:
    """
    Processes the provided file name and exports to an excel file containing the english and language translation
    """

    dataset_path = os.path.join(dataset_directory, file)
    df = functions.read_jsonl_file(dataset_path)
    language_short_text = functions.get_language_short_text(file)
    df = functions.perform_merge_on_english(english_df, df)
    export_df_path = os.path.join(processed_directory, f"en-{language_short_text}.xlsx")
    df.to_excel(export_df_path)
    log.info(f"Finished processing the file {file}")


def question1(dataset_directory_path: str, destination_directory_path: str):
    """
    Answers question 1 task and uploads the files to google drive
    """
    setup(destination_directory_path)
    files = os.listdir(dataset_directory_path)
    log.info("File Processing Has Been Initialized")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_file, files)

    zip_file = functions.zip_directory(destination_directory_path, "processed")
    functions.upload_to_drive(zip_file)
