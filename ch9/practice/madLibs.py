#! python3
# madLibs.py - Reads in text files and lets the user add their own text anywhere the word
# ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.


import pyinputplus as pyip
import re


def mad_libs():
    ml = open('./madlib.txt')
    text = ml.read()
    parts_of_speech = find_parts_of_speech(text)
    text = replace_pos(parts_of_speech, text)


def find_parts_of_speech(text):
    pos_pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    found_pos = pos_pattern.findall(text)
    return found_pos


def replace_pos(pos, text):
    for word in pos:
        prompt = f'Enter {"an" if word.lower()[0] == "a" else "a"} {word.lower()}\n'
        response = pyip.inputStr(prompt)
        
        text = re.sub(word, response, text, 1)
    return text
    

if __name__ == '__main__':
    mad_libs()