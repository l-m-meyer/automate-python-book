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

    # validate generic date ranges
    if not (1 <= day and day <= 31):
        return
    
    if not (1 <= month and month <= 12):
        return
    
    if not (1000 <= year and year <= 2999):
        return

    
    print(f'{str(day).zfill(2)}/{month}/{year}')


# TEST CASES
# passing
detect_date('03/11/1999')
detect_date('21/11/1999')
detect_date('01/04/2023')

# failing
detect_date('3/3/1000')
detect_date('03/33/1000')
detect_date('03/12/3000')