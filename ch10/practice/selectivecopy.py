#! python3
# selectivecopy.py - Copies all files in a folder tree with a certain file extension.


import pyinputplus as pyip
import shutil, os, re


def main():
    folder = get_folder()
    ext = get_ext()
    print(f'FOLDER: {folder}\nEXTENSION: {ext}')
    return


# TODO: get folder to copy from and file extension from user
def get_folder():
    folder = pyip.inputFilepath('Enter a filepath for folder to copy: ', mustExist=True)

    return folder


def get_ext():
    ext = pyip.inputStr('Enter a file extension to target (ex: .pdf): ',
                        allowRegexes=[r'^\.([a-z]{2,3})$'],
                        blockRegexes=[r'\d+$'])

    if ext[0] != '.':
        print(f'"{ext}" is invalid. Must start with "."')
        return get_ext()

    return ext


# TODO: create regex pattern to identify file extension to copy


# TODO: walk the folder tree and copy matching file extensions to a new folder


if __name__ == '__main__':
    main()