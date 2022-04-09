import os
import json
import csv
import math


def find_word_index_by_name(name):
    for word in index:
        if word['name'] == name:
            return word


def count_tf_from_file(filename, word):
    file = open('lemm/' + filename, mode="rt", encoding='utf-8')
    data = file.read()
    words = data.split()
    print(words.count(word))
    tf = words.count(word) / len(words)
    return tf


def count_idf(word):
    indx = find_word_index_by_name(word)
    idf = math.log(len(documents) / len(indx['files']))
    return idf


documents = os.listdir('lemm')
file = open('index.json', mode="r", encoding='utf-8')
data = file.read()
index = json.loads(data)
# index = index[]
headers = []
words = []
headers.append('documentId')
for ii in index:
    headers.append(ii['name'])
    words.append(ii['name'])

f = open('tables/tf.csv', 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(headers)

for document in documents:
    row = []
    row.append(document)
    for word in words:
        row.append(count_tf_from_file(document, word))
    writer.writerow(row)
f.close()

f2 = open('tables/idf.csv', 'w', encoding='utf-8')
writer2 = csv.writer(f2)
writer2.writerow(words)

rrow = []
for word in words:
    rrow.append(count_idf(word))
writer2.writerow(rrow)
f2.close()

f3 = open('tables/tf-idf.csv', 'w', encoding='utf-8')
writer3 = csv.writer(f3)
writer3.writerow(headers)

tf = open('tables/tf.csv', 'r', encoding='utf-8')
heading = next(tf)
print(heading)
tf_reader_obj = csv.reader(tf)

idf = open('tables/idf.csv', 'r', encoding='utf-8')
heading = next(idf)
idf_reader_obj = csv.reader(idf)

skipline2 = next(idf_reader_obj)
idf_line = next(idf_reader_obj)
for document in documents:
    row = []
    row.append(document)
    skipline1 = next(tf_reader_obj)
    tf_line = next(tf_reader_obj)
    tf_line_conv = tf_line[1:]
    tf_line_conv = list(map(float, tf_line_conv))
    idf_line = list(map(float, idf_line))
    multiply = [a * b for a, b in zip(tf_line_conv, idf_line)]
    row.extend(multiply)
    writer3.writerow(row)
f3.close()
