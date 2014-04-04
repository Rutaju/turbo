from collections import Counter
import re
import sys
import os


def reading(x):
    f = open(x, 'r+')
    text = f.read()
    f.close()
    return text


def counting(x):
    data_string = str(Counter(x))
    words = re.findall(r'\w+', x)
    data_words = str(Counter(words))
    return "symbols " + data_string + "words " + data_words + "\n" 

def writing(x):
    file = open('results.txt', 'a')
    file.write(x)
    file.close()

#print('please specify the directory')#
path = "/home/ruteles/Desktop/"
dirs = os.listdir(path)
all_text = ''
for file in dirs:
    writing("In file " + str(file) + ' ')
    text = reading(path + file)
    all_text = all_text + text
    writing(counting(text))
writing("In all files " + counting(all_text) + "\n" )
