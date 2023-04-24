#! python3
# deleteUnwantedFiles.py - Find and delete large, unwanted files of more than 100MB.


import pyinputplus as pyip
import os


def get_folder():
    """Gets folder from user to process for large, unwanted files."""
    folder = pyip.inputFilepath('Enter a filepath for folder to search for large files: ', mustExist=True)

    if not os.path.exists(folder):
        print('Filepath is invalid.')
        return get_folder()
    
    return os.path.abspath(folder)


def get_large_files(folder):
    """Returns a list of files over 100MB in size."""
    large_files = []

    for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            fpath = os.path.join(foldername, file)

            file_size_over_100MB = compare_file_size(fpath)
            if file_size_over_100MB:
                large_files.append(fpath)
    return large_files


def compare_file_size(file):
    """Gets size of file and returns True if file size is less than 100MB, False otherwise."""
    file_size = get_file_size_in_MB(file)
    
    if file_size <= 100:
        return False
    return True


def get_file_size_in_MB(file):
    """Gets size of file in bytes and returns file size in MB."""
    file_size = os.path.getsize(file)
    file_size_MB = file_size/(1024 * 1024)
    return file_size_MB


def print_large_files(files):
    """Prints the absolute path of each file found, or prints that no files were found."""
    if not files:
        print('No files larger than 100MB found in folder tree.')
        return
    
    print('Files over 100MB in size:')
    for file in files:
        print(f'- {file}\n')


def main():
    folder = get_folder()
    large_files = get_large_files(folder) 
    print_large_files(large_files)


if __name__ == "__main__":
    main()