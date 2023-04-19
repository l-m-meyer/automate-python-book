#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import pyinputplus as pyip
import re


def mad_libs():
    ml = open('./madlib.txt', 'r')
    text = ml.read()
    parts_of_speech = find_parts_of_speech(text)
    replace_pos(parts_of_speech, text)
    ml.close()
    

def find_parts_of_speech(text):
    pos_pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    found_pos = pos_pattern.findall(text)
    return found_pos


def replace_pos(pos, text):
    for word in pos:
        prompt = f'Enter {"an" if word.lower()[0] == "a" else "a"} {word.lower()}\n'
        response = pyip.inputStr(prompt)
        
        text = re.sub(word, response, text, 1)
    write_mad_lib(text)


def write_mad_lib(text):
    ml = open('./madlib_result.txt', 'w')
    ml.write(text)
    ml.close()


if __name__ == '__main__':
    mad_libs()