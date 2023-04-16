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