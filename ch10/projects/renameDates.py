#! python3
# renameDates.py - Rename files with American-style dates (MM-DD-YYYY)
# to European-style dates (DD-MM-YYYY).


import shutil, os, re


# TODO: create a regex that can identify the text pattern of American-style dates


# TODO: call os.listdir() to find all the files in the working directory


# TODO: Loop over each filename, using the regex to check whether it has a date


# TODO: If it has a date, rename the file with shutil.move()