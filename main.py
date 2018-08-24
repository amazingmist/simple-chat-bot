import re
import os
import json
from difflib import SequenceMatcher

# return the similar ratio between two string.
def getSimilarRatio(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

# read data from data.json to program
filePath = os.path.dirname(__file__) + os.sep + "data.json"
with open(filePath) as data_file:    
    data = json.load(data_file)

# get input question from user
question = input("Question: ")
maxRatio = 0
index = -1

# find index of the most similar question with the user's question 
for i in range(len(data)):
    currentRatio = getSimilarRatio(data[i]["question"], question)
    if currentRatio > maxRatio:
        maxRatio = currentRatio
        index = i

# show the answer
print("Answer: ", data[index]["answer"])
