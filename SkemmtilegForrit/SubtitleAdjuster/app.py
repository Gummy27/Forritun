import os
import csv
location = "E:\Movies\The Good Place Season 4 Mp4 1080p"

def stripZeroes(nr):
    return float(nr[:-1].lstrip('0') + nr[-1])

def timeToInt(timi):
    h, m, s = map(stripZeroes, timi.replace(',', '.').split(':'))

    return h*60*60 + m*60 + s

def intToTime(timi):
    dateTime = []

    hh = str(timi//(60*60))
    timi -= hh*60*60
    dateTime.insert(0, '0'+hh if len(hh) == 1 else hh)

    timi -= mm*60
    mm = str(timi//60)
    dateTime.insert(1, '0'+mm if len(mm) == 1 else mm)


    print(dateTime)
    print(timi)

intToTime(timeToInt("00:24:32,387"))
'''
with open("Subtitles.srt", 'r') as file:
    subtitles = file.readlines()

for x in subtitles:
    if x[13:16] == "-->":
        print(x[0:12], x[17:29])
'''

