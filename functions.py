import pandas as pd
import numpy as np
import json
import os


def read_jsonl_file(file_path: str) -> pd.DataFrame:
    """
    Reads a jsonl file and returns a pandas dataframe
    """
    df = pd.read_json(file_path, lines=True)
    return df


def get_language_short_text(file_name: str) -> str:
    """
    Returns the language short text from the file name
    """
    return file_name.split("-")[1].split(".")[0]


def create_directory_if_not_exist(directory_name: str):
    """

    Returns the file path of the file in the directory.
    If the directory does not exist its created.
    """

    if os.path.exists(directory_name):
        pass
    else:
        os.mkdir(directory_name)


def perform_merge_on_english(
    english_df: pd.DataFrame, other_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Performs the merge operation, Returning a combined dataframes with the utterance translations and sources.
    """
    df = other_df.merge(english_df, on='id')
    df = df.rename(
        {
            "utt_x": "utterance_translation",
            "annot_utt_x": "annotation_utterance_translation",
            "utt_y": "utterance",
            "annot_utt_y": "annot_utt",
            "partition_y": "partition",
        },
        axis=1,
    )
    return df[
        [
            "utterance_translation",
            "annotation_utterance_translation",
            "utterance",
            "annot_utt",
            "id",
            "partition",
        ]
    ]


def partition_dfs(df: pd.DataFrame, key: str) -> pd.DataFrame:
    """
    Partitions the dataframe based on the key
    """
    return df[df["partition"] == key]


def df_to_jsonl(df: pd.DataFrame, file_path: str):
    """
    Writes the dataframe to a jsonl file
    """
    df.to_json(file_path, orient="records", lines=True)


def export_list_as_json(datalist: list, file_path):
    """
    Exports a list as json file
    """
    with open(file_path, "w") as f:
        json.dump(datalist, f)
