import sqlite3
from datetime import datetime
from urllib.parse import quote
import json
import requests
import csv

#
# PATHS
#

#VocabDB
VocabDB = "/home/teclas/Documents/Japanese/Kindle/vocab.db"

#CSV file
CSVOutput = "/home/teclas/Documents/Japanese/Kindle/vocab.csv"


#
# Get JAP words
#

def query_Kindle(vocab_db, _since=0):

    if isinstance(_since, datetime):
        since = int(_since.strftime('%s')) * 1000
    else:
        since = _since * 1000

    db = sqlite3.connect(vocab_db)
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    sql = '''
        select WORDS.stem, WORDS.word, LOOKUPS.usage, BOOK_INFO.title, LOOKUPS.timestamp
        from LOOKUPS left join WORDS
        on WORDS.id = LOOKUPS.word_key
        left join BOOK_INFO
        on BOOK_INFO.id = LOOKUPS.book_key
        where LOOKUPS.timestamp > ? AND WORDS.lang = "ja"
        order by WORDS.stem, LOOKUPS.timestamp
    '''

    rows = cur.execute(sql, (since,)).fetchall()
    return rows

def getvocab(search):
    kanjioriginal = search
    kanji = quote("*" + kanjioriginal + "*")
    url = str("http://jisho.org/api/v1/search/words?keyword=" + kanji)
    #site = urllib.request.urlopen(url)
    page = requests.get(url).text
    print(page)
    #with page as data_file:
    data = json.loads(page)
    #print(len(data))
    data = data["data"][0]

    word = ""
    reading = ""
    definitions = ""

    #### Just in case it doesn't find the word
    try:
        word = data["japanese"][0]["word"]
        reading = data["japanese"][0]["reading"]
        definitions = ", ".join(data["senses"][0]["english_definitions"])
        print("word", word)
        print("reading", reading)
        print("definitions", definitions)
    except:
        pass

    return [word, reading, definitions]

vocab = query_Kindle(VocabDB, _since=0)


with open(CSVOutput, "w", encoding="utf-8") as outputfile:
    outputwriter = csv.writer(outputfile, delimiter=",")
    for lookup in vocab:
        #print stem, lookup and source sentence
        print(lookup[0], lookup[1], lookup[2])
        definitions = getvocab(lookup[0])
        outputwriter.writerow(list(lookup) + definitions)
