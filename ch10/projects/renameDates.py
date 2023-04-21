#! python3
# renameDates.py - Rename files with American-style dates (MM-DD-YYYY)
# to European-style dates (DD-MM-YYYY).


import shutil, os, re


# create a regex that can identify the text pattern of American-style dates
datePattern = re.compile(r"""^(.*?)     # all text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3)?\d)-                     # one or two digits for the day
    ((19|20)\d\d)                       # four digits for the year
    (.*?)$                              # all text after the date
    """, re.VERBOSE)


# TODO: call os.listdir() to find all the files in the working directory


# TODO: Loop over each filename, using the regex to check whether it has a date


# TODO: If it has a date, rename the file with shutil.move()