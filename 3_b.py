import json
import re
import os


def remove_list(l1, l2):
    l3 = [x for x in l1 if x not in l2]
    return l3


def list_intersection(list1, list2):
    l3 = list(set(list1) & set(list2))
    return l3


def indexes_of_char(chrrr, strrrr):
    lst = []
    for pos, char in enumerate(strrrr):
        if (char == chrrr):
            lst.append(pos)
    return lst


def find_word(words, word_name):
    for word in words:
        if word['name'] == word_name:
            return word
    return


file = open('index.json', mode="r", encoding='utf-8')
data = file.read()
index = json.loads(data)
all_files = os.listdir('lemm')

delimiters = " & ", " | "
example = "!проект | кабинет & сотруднику"
regexPattern = '|'.join(map(re.escape, delimiters))
request_words = re.split(regexPattern, example)

indexes_of_and = indexes_of_char("&", example)
indexes_of_or = indexes_of_char("|", example)

print(request_words[0])
print(index[0]['files'])
if len(indexes_of_and) == 2:
    word1 = find_word(index, request_words[0])['files'] if not request_words[0].startswith('!') else remove_list(
        all_files, find_word(index, request_words[0][1:])['files'])
    word2 = find_word(index, request_words[1])['files'] if not request_words[1].startswith('!') else remove_list(
        all_files, find_word(index, request_words[1][1:])['files'])
    word3 = find_word(index, request_words[2])['files'] if not request_words[2].startswith('!') else remove_list(
        all_files, find_word(index, request_words[2][1:])['files'])
    intr1 = list_intersection(word1, word2)
    intr2 = list_intersection(intr1, word3)
    print(intr2)

if len(indexes_of_or) == 2:
    word1 = find_word(index, request_words[0])['files'] if not request_words[0].startswith('!') else remove_list(
        all_files, find_word(index, request_words[0][1:])['files'])
    word2 = find_word(index, request_words[1])['files'] if not request_words[1].startswith('!') else remove_list(
        all_files, find_word(index, request_words[1][1:])['files'])
    word3 = find_word(index, request_words[2])['files'] if not request_words[2].startswith('!') else remove_list(
        all_files, find_word(index, request_words[2][1:])['files'])
    unionn = list(set(word1 + word2 + word3))
    print(unionn)

if indexes_of_and[0] < indexes_of_or[0]:
    word1 = find_word(index, request_words[0])['files'] if not request_words[0].startswith('!') else remove_list(
        all_files, find_word(index, request_words[0][1:])['files'])
    word2 = find_word(index, request_words[1])['files'] if not request_words[1].startswith('!') else remove_list(
        all_files, find_word(index, request_words[1][1:])['files'])
    word3 = find_word(index, request_words[2])['files'] if not request_words[2].startswith('!') else remove_list(
        all_files, find_word(index, request_words[2][1:])['files'])
    intersection = list_intersection(word1, word2)
    unionnn = list(set(intersection + word3))
    print(unionnn)

if indexes_of_and[0] > indexes_of_or[0]:
    word1 = find_word(index, request_words[0])['files'] if not request_words[0].startswith('!') else remove_list(
        all_files, find_word(index, request_words[0][1:])['files'])
    word2 = find_word(index, request_words[1])['files'] if not request_words[1].startswith('!') else remove_list(
        all_files, find_word(index, request_words[1][1:])['files'])
    word3 = find_word(index, request_words[2])['files'] if not request_words[2].startswith('!') else remove_list(
        all_files, find_word(index, request_words[2][1:])['files'])
    intersection = list_intersection(word2, word3)
    unionnn = list(set(intersection + word1))
    print(unionnn)
