import os
import csv
location = "E:\Movies\The Good Place Season 4 Mp4 1080p"

def stripZeroes(nr):
    return float(nr[:-1].lstrip('0') + nr[-1])

def timeToInt(timi):
    h, m, s = map(stripZeroes, timi.replace(',', '.').split(':'))

    return h*60*60 + m*60 + s

def roundFloat(nr, rounding):
    stop = len(str(nr).split('.')[1]) - rounding - 1

    listi = list(map(int, list(str(nr).split('.')[1][::-1])))
    for index, value in enumerate(listi):
        if index > stop:
            if value >= 10:
                listi[index+1] += 1
                listi[index] = 0
        else:
            if value > 5:
                listi[index+1] += 1
    
    listi = listi[rounding-1:]
    print(float(str(nr).split('.')[0]+'.'+''.join(map(str, listi[::-1]))))

def intToTime(timi):
    dateTime = []

    hh = str(timi//(60*60))
    timi -= float(hh)*60*60
    dateTime.insert(0, '0'+hh if len(hh) == 1 else hh)

    mm = str(timi//60)
    timi -= round(float(mm)*60, 2)
    dateTime.insert(1, '0'+mm if len(mm) == 1 else mm)

    roundFloat(timi, 3)

    dateTime.insert(2, '0'+str(timi) if len(str(timi).split('.')[0]) == 1 else str(timi))
    dateTime[2]
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

