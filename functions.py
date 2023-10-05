'''
This functions module contains different functions to support the answering of the tasks provided
'''


import pandas as pd
import numpy as np
import json
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from shutil import make_archive

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/spreadsheets']



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
    df = other_df.merge(english_df, on="id")
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


def df_to_jsonl(df: pd.DataFrame, file_path: str) ->None:
    """
    Writes the dataframe to a jsonl file
    """
    df.to_json(file_path, orient="records", lines=True)


def export_list_as_json(datalist: list, file_path) ->None:
    """
    Exports a list as json file
    """
    with open(file_path, "w") as f:
        json.dump(datalist, f, indent=4)


def zip_directory(directory_name: str, zip_file_name: str) -> str:
    """
    Zips a directory
    """
    make_archive(zip_file_name, "zip", directory_name)
    return f"{zip_file_name}.zip"


def upload_to_drive(filename: str):
    """
    Uploads a file to google drive and returns the file id
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        file_metadata = {"name": filename}
        media = MediaFileUpload(filename, mimetype="application/zip")
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )
        print(f'File ID: {file.get("id")}')

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None
