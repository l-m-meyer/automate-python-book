#! python3
# dateDetection.py - Detects dates in the DD/MM/YYYY format.


import re


def detect_date(date):
    date_regex = re.compile(r'''(
        (\d{2})    # day
        (/)          # separator
        (\d{2})    # month
        (/)          # separator
        (\d{4})      # year
    )''', re.VERBOSE)

    valid_date = date_regex.findall(date)

    if not valid_date:
        return

    # assign date values and convert to integers
    day = int(valid_date[0][1])
    month = int(valid_date[0][3])
    year = int(valid_date[0][5])