#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import re


def mad_libs():
    ml = open('./madlib.txt')
    content = ml.read()
    parts_of_speech = find_parts_of_speech(content)


def find_parts_of_speech(text):
    pos_pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    found_pos = pos_pattern.findall(text)
    return found_pos


def get_adjective():
    return


def get_noun():
    return


def get_verb():
    return


def get_adverb():
    return



if __name__ == '__main__':
    mad_libs()