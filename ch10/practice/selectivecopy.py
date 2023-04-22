#! python3
# selectivecopy.py - Copies all files in a folder tree with a certain file extension.


import pyinputplus as pyip
import shutil, os, re


# get folder to copy from user
def get_folder():
    folder = pyip.inputFilepath('Enter a filepath for folder to copy: ', mustExist=True)

    if not os.path.exists(folder):
        print('Filepath is invalid.')
        return get_folder()
    
    return os.path.abspath(folder)


# get file extension from user
def get_ext():
    ext = pyip.inputStr('Enter a file extension to target (ex: .pdf): ',
                        allowRegexes=[r'^\.([a-z]{2,3})$'],
                        blockRegexes=[r'\d+$'])
    
    if ext[0] != '.':
        print(f'"{ext}" is invalid. Must start with "."')
        return get_ext()
    
    return ext


# create regex pattern to identify file extension to copy
def find_ext(filename, ext):
    ext_regex = re.compile(f'{ext}')
    mo = ext_regex.search(filename)
    return mo


# walk the folder tree and copy matching file extensions to a new folder
def copy_files(folder, ext):
    new_folder = os.path.join(folder, f'{ext[1:]}_files')
    
    if not os.path.exists(new_folder):
        print(f'Creating new folder: {new_folder}...')
        make_folder = os.makedirs(new_folder)

    for foldername, subfolders, filenames in os.walk(folder):
        if foldername == new_folder:
            continue

        for filename in filenames:
            match = find_ext(filename, ext)
            if not match:
                continue
            to_copy = os.path.join(foldername, filename)
            shutil.copy(to_copy, new_folder)
    print('Done.')


def main():
    folder = get_folder()
    ext = get_ext()
    return copy_files(folder, ext)


if __name__ == '__main__':
    main()