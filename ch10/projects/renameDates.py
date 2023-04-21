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


# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart  = mo.group(1)
    monthPart   = mo.group(2)
    dayPart     = mo.group(4)
    yearPart    = mo.group(6)
    afterPart   = mo.group(8)


# TODO: Form the European-style filename


# TODO: Get the full, absolute file paths


# TODO: Rename the files