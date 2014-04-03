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
    data_string = Counter(x)
    words = re.findall(r'\w+', x)
    data_words = Counter(words)
    return data_string, data_words

#print('please specify the directory')#
path = "/home/ruteles/Desktop/"
dirs = os.listdir(path)
all_text = ''
for file in dirs:
    print file
    text = reading(path + file)
    all_text = all_text + text
    print (counting(text))
print ('statistics of all the files in directory', counting(all_text))
