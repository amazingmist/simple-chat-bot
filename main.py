import re
import os
import json
from pprint import pprint


from difflib import SequenceMatcher

def getSimilarityRatio(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

filePath = os.path.dirname(__file__) + os.sep + "data.json"
with open(filePath) as data_file:    
    data = json.load(data_file)


question = input("Question: ")
ratio = 0
index = -1
for i in range(len(data)):
    if getSimilarityRatio(data[i]["question"], question) > ratio:
        ratio = getSimilarityRatio(data[i]["question"], question)
        index = i
    
print("Answer: ", data[index]["answer"])
