# Kindle2CSV
Queries Kindle's vocab.db to create a CSV with definitions from Jisho (JMdict, Kanjidic2, JMnedict and Radkfile dictionary files)

Change VocabDB and CSVOutput variables and run. Tested with python 3.7, but should work with any version of python 3.

Columns order:
* Stem (what kindle used to lookup in the dictionary)
* Original word
* Sentence where the lookup was taken from
* Book where it was taken from
* Timestamp (so you can exclude entries already imported)
* Word queried in Jisho (might differ for kana words like the one below)
* Reading from Jisho
* English definitions

Example:

Stem | Original Word | Sentence where the lookup was taken from | Book | Timestamp | Jisho word | Reading Jisho | Definitions
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | -------------
かなしい | 哀しい | するとその男は、嬉しそうな哀しそうな、そして泣き出しそうな顔をして、キノとエルメスに訊ねた。 | キノの旅　the Beautiful World | 1535195449083 | 悲しい | かなしい | sad, sorrowful
