import json
import re


def list_intersection(list1, list2):
    l3 = list(set(list1) & set(list2))
    return l3


def indexes_of_char(chrrr, strrrr):
    lst = []
    for pos, char in enumerate(strrrr):
        if (char == chrrr):
            lst.append(pos)
    return lst

def find_word(words,word_name):
    for word in words:
        if word['name'] == word_name:
            return word
    return

file = open('index.json', mode="r", encoding='utf-8')
data = file.read()
index = json.loads(data)

delimiters = " & ", " | "
example = "проект | кабинет & сотруднику"
regexPattern = '|'.join(map(re.escape, delimiters))
request_words = re.split(regexPattern, example)

indexes_of_and = indexes_of_char("&", example)
indexes_of_or = indexes_of_char("|", example)

print(index[0]['files'])
if len(indexes_of_and) == 2:
    word1 = find_word(index,request_words[0])
    word2 = find_word(index,request_words[1])
    word3 = find_word(index,request_words[2])
    intr1 = list_intersection(word1['files'],word2['files'])
    intr2 = list_intersection(intr1,word3['files'])
    print(intr2)

if len(indexes_of_or) == 2:
    word1 = find_word(index,request_words[0])
    word2 = find_word(index,request_words[1])
    word3 = find_word(index,request_words[2])
    unionn = list(set(word1['files'] + word2['files'] + word3['files']))
    print(unionn)

if indexes_of_and[0] < indexes_of_or[0]:
    word1 = find_word(index, request_words[0])
    word2 = find_word(index, request_words[1])
    word3 = find_word(index, request_words[2])
    intersection = list_intersection(word1['files'],word2['files'])
    unionnn = list(set(intersection + word3['files']))
    print(unionnn)

if indexes_of_and[0] > indexes_of_or[0]:
    word1 = find_word(index, request_words[0])
    word2 = find_word(index, request_words[1])
    word3 = find_word(index, request_words[2])
    intersection = list_intersection(word2['files'],word3['files'])
    unionnn = list(set(intersection + word1['files']))
    print(unionnn)