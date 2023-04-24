#! python3
# deleteUnwantedFiles.py - Find and delete large, unwanted files of more than 100MB.


import pyinputplus as pyip
import os


def get_folder():
    """Gets folder from user to process for large, unwanted files."""
    folder = pyip.inputFilepath('Enter a filepath for folder to copy: ', mustExist=True)

    if not os.path.exists(folder):
        print('Filepath is invalid.')
        return get_folder()
    
    return os.path.abspath(folder)


def compare_file_size(file):
    """Gets size of file and returns file name if less than 100MB."""
    file_size = get_file_size_in_MB(file)
    
    if file_size <= 100:
        return
    return file


def get_file_size_in_MB(file):
    """Gets size of file in bytes and converts to MB."""
    file_size = os.path.getsize(file)
    file_size_MB = file_size/(1024 * 1024)
    return file_size_MB


def main():
    folder = get_folder()
    pass


if __name__ == "__main__":
    main()