#! python3
# regexPlay.py - Validating different types of input using regex.

import re


# Find website URLs that begin with http:// or https://
def validate_url(url):
    url_regex = re.compile(r'^(http|https)://\w*')

    valid_url = url_regex.search(url)

    if valid_url:
        print(f'${url} is a valid url')
    else:
        print(f'{url} is NOT a valid url')


# TEST CASES
# passing
validate_url('http://www.google.com')
validate_url('https://localhost:8081')
# failing
validate_url('htps://invalidurl.com')
validate_url('12344567')


# Clean up dates in different formats by replacing them with dates in a single, standard format.
def format_date(date):
    date_regex = re.compile(r'''(
        (\d{1,4}|[A-Z]{3})      # month or year
        (/|-|\s|.)              # separator
        (\d{1,2}|[A-Z]{3})      # day or month
        (/|-|\s|.)              # separator
        (\d{1,4})               # day or year
    )''', re.VERBOSE)

    valid_date = date_regex.findall(date)

    day = ''
    month = ''
    year = ''

    for groups in valid_date:
        if len(groups[1]) == 4:
            year = groups[1]
        
        # checks that length of group is less than 3 or year is null
        if len(groups[1]) <= 3 or not year:
            month = groups[1]

        # set month if month is null, else set day
        if not month:
            month = groups[3]
        else:
            day = groups[3]

        # set year if year is null, else set day
        if not year:
            year = groups[5]
        else:
            day = groups[5]

    # if any value is null, the date is not printed
    if not day or not month or not year:
        return
    print(f'DD_MM_YYYY: {day}_{month}_{year}')


# TEST CASES
# passing
format_date('3/14/2023')
format_date('3-14-2023')
format_date('3 14 2023')
format_date('3.14.2023')
format_date('MAR 14 2023')
format_date('MAR-14-2023')
format_date('MAR/14/2023')
format_date('MAR.14.2023')
format_date('2023/3/14')
format_date('2023-3-14')
format_date('2023.3.14')
format_date('2023 3 14')
# failing
format_date('*********')
format_date('abcdefgh')
format_date('12345-6789-111213')    # should fail, but prints 3_11_6789


# Remove sensitive information such as Social Security or credit card numbers.
def censor_info(data):
    data_CC = re.compile(r'(\d{15,16})|(\d{4}\s\d{4}\s\d{4}\s\d{4})|(\d{5}\s\d{5}\s\d{5})')
    data_SIN = re.compile(r'\d{3}\-\d{3}\-\d{3}')
    data_SSN = re.compile(r'\d{9}')

    # censors matched regex via substitution
    valid_CC = data_CC.sub('**** **** **** ****', data)
    valid_SIN = data_SIN.sub('***-***-***', data)
    valid_SSN = data_SSN.sub('*** *** ***', data)

    # determines the type of data input and returns if true
    if '*' in valid_CC:
        print(f'CC: {valid_CC}')
        return
    if '*' in valid_SIN:
        print(f'SIN: {valid_SIN}')
        return
    if '*' in valid_SSN:
        print(f'SSN: {valid_SSN}')
        return
    print(f'INVALID INPUT: {data}')


# TEST CASES
# passing
censor_info("123456789")            # SSN
censor_info("123-456-789")          # SIN
censor_info("1234567890123456")     # CC
censor_info("1234 5678 9012 3456")  # CC
censor_info("123456789012345")      # CC
censor_info("12345 67890 12345")    # CC
# failing
censor_info("abcdefghi")
censor_info("m23mwswe3")
censor_info("123.456.789")


# Find common typos such as:
#   - multiple spaces between words
#   - accidentally repeated words
#   - multiple exclaimation marks at the end of sentences
def fix_typos(text):
    result = find_multiple_spaces(text)
    
    # if result is not None, function consumes result with removed spaces
    # else function consumes original text
    if result:
        result = find_repeated_words(result)
    else:
        result = find_repeated_words(text)

    print(f'BEFORE: {text}\nAFTER: {result}')
    print()


def find_multiple_spaces(text):
    # substitutes extra spaces with a single space in text
    return re.sub(' +', ' ', text)


def find_repeated_words(text):
    # \b: matches word boundary
    # \1: matches text in group 1
    # pattern to find repeated words
    repeated_words_regex = re.compile(r'\b(\w+)( \1\b)+')
    
    # substitutes matches of repeated words with just the first match group
    # returns a string of non-repeated words
    return re.sub(repeated_words_regex, r'\1', text)


# TEST CASES
fix_typos('I  have  too  many  spaces.')
fix_typos('hello hello')
fix_typos('hello     hello')
fix_typos('space spaces  spacess   spacesss    space ')
fix_typos('text text text text hi')
fix_typos('text text hi text text hi')