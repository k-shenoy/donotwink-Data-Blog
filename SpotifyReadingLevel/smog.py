import pandas as pd
from PyLyrics import *

def num_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        if (len(word) != 2):
            count -= 1
    if count == 0:
        count += 1
    return count


df = pd.read_excel("spotifysongs.xlsx")

file1 = open("smogScores.csv","w")

for index, row in df.iterrows():
    try:
        songlyr = PyLyrics.getLyrics(row["artist"],row["song"][1:len(row["song"])-1])
    except:
        print(row["artist"], row["song"][1:len(row["song"])-1])

    all = songlyr.split()

    numpolysyl = 0

    for el in all:
        if (syllable_count(el) >= 3):
            numpolysyl+=1

    numLines = songlyr.count('\n') + 1


    file1.write(str(numpolysyl * 30 / numLines) + "," + row["song"] + "," + row["artist"] + "\n")

file1.close()
