import csv
from scipy import spatial


class DocSimilarity:
    def __init__(self, name, similarity_koeff):
        self.name = name
        self.similarity_koeff = similarity_koeff

    def __str__(self):
        return 'name: ' +  self.name + ' similarity koeff: ' + str(self.similarity_koeff)

def count_tf(word, words):
    print(words.count(word))
    tf = words.count(word) / len(words)
    return tf


def count_cos_similarity(data1, data2):
    return 1 - spatial.distance.cosine(data1, data2)


query = input()
query_words = query.split()

idf = open('tables/idf.csv', 'r', encoding='utf-8')
idf_reader = csv.reader(idf)
headers = next(idf_reader)
skip_line = next(idf_reader)
values = next(idf_reader)
print(headers)
search_query = []
for idx, header in enumerate(headers):
    if header in query_words:
        tf = float(count_tf(header, query_words))
        idff = float(values[idx])
        search_query.append(tf * idff)
    else:
        search_query.append(0)
print(search_query)
tf_idf = open('tables/tf-idf.csv', 'r', encoding='utf-8')
skip_headers = next(tf_idf)
tf_idf_reader = csv.reader(tf_idf)
skip = 0
similarities = []
for row in enumerate(tf_idf_reader):
    if skip == 0:
        skip = 1
        continue
    else:
        skip = 0
        name = row[1][0]
        vector = row[1][1:]
        vector = [float(i) for i in vector]
        similarity = count_cos_similarity(search_query,vector)
        similarities.append(DocSimilarity(name,similarity))

similarities = sorted(similarities, key=lambda x: x.similarity_koeff, reverse=True)

top5 = similarities[0:5]

for sim in top5:
    print(sim.__str__())
