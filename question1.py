import functions
import os
import concurrent.futures
from constants import *

english_df = functions.read_jsonl_file(english_dataset_path)
def setup():

    functions.create_directory_if_not_exist(processed_dataset_directory)

def process_file(file:str) -> None:
    """
    Processes the provided file name and exports to an excel file containing the english and language translation
    """

    dataset_path = os.path.join(dataset_directory,file)
    df = functions.read_jsonl_file(dataset_path)
    language_short_text = functions.get_language_short_text(file)
    df = functions.perform_merge_on_english(english_df,df)
    export_df_path = os.path.join(processed_dataset_directory,f"en-{language_short_text}.xlsx")
    df.to_excel(export_df_path)

def question1():
    setup()

    files = os.listdir(dataset_directory)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_file,files)
