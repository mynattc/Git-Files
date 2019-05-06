#!/usr/bin/python

import os
from datetime import datetime
from pathlib import Path

import requests


def file_array(path):
    data_dir = Path(path)
    text_files = [f for f in os.listdir(data_dir) if f.endswith('.xml')]
    return text_files


# Function to load into memory all file contents from an array of file names
def all_file_contents(path, file_name_arr):
    data = []
    for file_name in file_name_arr:
        with open(path + file_name, encoding="utf8") as file_input:
            data.append(file_input.read())
    print("All files read into memory.")
    return data


# Function to post content
def post_file_content(url, param, filename, data):
    payload = {param: data}
    r = requests.post(url, payload, verify=False)
    # Print response Code
    if r.status_code != 200:
        print("Failed to post " + filename + ": " + r.text)
    return r


def main():
    # Create timer to see execution time length
    start = datetime.now()

    # Values for where to post and config'd param name.
    url = 'localhost'
    param = 'param1'
    path = 'Some_Sample_Data/'

    # Get file list and file content of only .xml files
    names = file_array(path)
    files = all_file_contents(path, names)
    count = 0
    # Iterate over array and post to url.

    for x in range(len(names)):
        post_file_content(url, param, names[x], files[x])
        count += 1


# End timer and calculate execution time.
print('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now() - start))

if __name__ == "__main__":
    main()
