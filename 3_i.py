import json
from json import JSONEncoder
import os


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Word:
    def __init__(self, name):
        self.name = name
        self.files = []


lemmas = os.listdir('lemm')
words = []
wordnamesadded = []
print(lemmas)

for lemma in lemmas:
    file = open('lemm/' + lemma,mode='r',encoding='utf-8')
    flat_list = [word for line in file for word in line.split()]
    flat_list = list(set(flat_list))
    for foundword in flat_list:
        if (foundword not in wordnamesadded):
            new_word = Word(foundword)
            new_word.files.append(lemma)
            words.append(new_word)
            wordnamesadded.append(foundword)
        else:
            for word in words:
                if (word.name == foundword):
                    word.files.append(lemma)

file2 = open('index.json',encoding='utf-8',mode='w')
file2.write(MyEncoder().encode(words))