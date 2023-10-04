import functions
import os
import concurrent.futures
from constants import english_dataset_path,dataset_directory

english_df = functions.read_jsonl_file(english_dataset_path)
processed_directory = None


def setup(processed_dataset_dir):
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

def question1(dataset_directory_path: str, destination_directory_path: str):
    setup(destination_directory_path)
    files = os.listdir(dataset_directory_path)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_file, files)

    # zip_file = functions.zip_directory(destination_directory_path,'processed')
    # functions.upload_to_drive(zip_file,zip_file)

