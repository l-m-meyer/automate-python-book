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
    before  = mo.group(1)
    month   = mo.group(2)
    day     = mo.group(4)
    year    = mo.group(6)
    after   = mo.group(8)

    # Form the European-style filename
    euroFilename = f'{before}{day}-{month}-{year}{after}'

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    # shutil.move(amerFilename, euroFilename)         # uncomment after testing