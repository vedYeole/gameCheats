accents = ""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# with open("dictionaries/spanishFullCopy.txt", 'r', encoding='utf-8') as spanish:
#     with open("dictionaries/spanishFull.txt", 'w', encoding='utf-8') as new:
#         wordList = []
#         for word in spanish:
#             if word not in wordList:
#                 new.write(word)
#                 wordList.append(word)
# with open("dictionaries/spanishFull.txt", 'r', encoding='utf-8') as spanish:
#     with open("dictionaries/spanishSmall.txt", 'w', encoding='utf-8') as new:
#         for word in spanish:
#             if len(word.strip()) <= 6:
#                 new.write(word)
import json
with open("dictionaries/englishFull.txt", 'r', encoding="utf-8") as textFile:
    wordList = []
    for word in textFile:
        wordList.append(word.strip())
    with open("dictionaries/listEnglishFull.json", 'w', encoding="utf-8") as jsonFile:
        json.dump(wordList, jsonFile, indent = 4)
