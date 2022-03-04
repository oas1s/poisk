from functools import partial
from operator import is_not
from urllib.request import Request, urlopen
import requests
import uuid

from bs4 import BeautifulSoup


def remove_punc(string):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    return string


def link_has_more_than_1000_words(source_link):
    try:
        html = requests.get(source_link)
    except Exception:
        print('cant ger page')
        return False
    soup = BeautifulSoup(html.text, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()
    words = text.split()
    print(len(words))
    return len(words) >= 100


def take_links_from_page(page):
    html = requests.get(page)

    soup = BeautifulSoup(html.text, "lxml")
    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    # unique values
    links = list(set(links))
    # remove none objects
    links = filter(partial(is_not, None), links)
    # remove phones etc
    links = [link for link in links if link.startswith('http')]
    links = [link for link in links if link_has_more_than_1000_words(link)]
    return links


def take_html_pure_text_from_page(page, logfile):
    html = requests.get(page)
    # html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = remove_punc(text)
    text = text.replace("&nbsp", " ")

    uuidd = str(uuid.uuid4())
    outF = open('pages/' + uuidd + '.txt', "w", encoding="utf-8")
    outF.write(text)
    logfile.write(page + ' ' + uuidd + '\n')
    outF.close()


outFi = open('index.txt', "w")
base_url = 'https://kpfu.ru'
links = take_links_from_page(base_url)
index = 0
while len(links) < 10:
    links = links + take_links_from_page(links[index])
    links = list(set(links))
    index += 1
print(len(links))
for link in links:
    take_html_pure_text_from_page(link, outFi)
outFi.close()
