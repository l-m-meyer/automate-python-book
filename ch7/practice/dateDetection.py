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

    # validate special case date ranges
    # April, June, September, and November have 30 days
    if month in [4, 6, 9, 11] and day == 31:
        return

    # February has 28 days, 29 days if a leap year
    if month == 2 and day > 28:
        # check if year is not a leap year
        if day == 29 \
            and (year % 4 != 0 \
            and year % 100 == 0) \
            or year % 400 != 0:
                print(False, date)
                return
        
        return

    
    print(f'{str(day).zfill(2)}/{month}/{year}')


# TEST CASES
# passing
detect_date('03/11/1999')
detect_date('21/11/1999')
detect_date('01/04/2023')
detect_date('01/06/2023')
detect_date('01/09/2023')
detect_date('01/11/2023')
detect_date('29/02/2000')
detect_date('28/02/2001')

# failing
detect_date('3/3/1000')
detect_date('03/33/1000')
detect_date('03/12/3000')
detect_date('31/04/2023')
detect_date('31/06/2023')
detect_date('31/09/2023')
detect_date('31/11/2023')
detect_date('29/02/1900')
detect_date('29/02/1901')
detect_date('31/02/1901')