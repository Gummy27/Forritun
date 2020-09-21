import os
import csv
location = "E:\Movies\The Good Place Season 4 Mp4 1080p"

def stripZeroes(nr):
    return float(nr[:-1].lstrip('0') + nr[-1])

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
    
    listi = listi[stop+1:]

    return(float(str(nr).split('.')[0]+'.'+''.join(map(str, listi[::-1]))))

def timeToInt(timi):
    h, m, s = map(stripZeroes, timi.replace(',', '.').split(':'))

    return h*60*60 + m*60 + s

def intToTime(timi):
    formattedTime = []

    hh = str(int(timi//(60*60)))
    timi -= float(hh)*60*60
    formattedTime.insert(0, '0'+hh if len(hh) == 1 else hh)

    mm = str(int(timi//60))
    timi -= float(mm)*60
    formattedTime.insert(1, '0'+mm if len(mm) == 1 else mm)

    if len(str(timi).split('.')[1]) > 3:
        timi = roundFloat(timi, 3)
    
    s, ms = str(timi).split('.')
    if len(s) == 1:
        s = '0'+s
    if len(ms) < 3:
        ms = ms + ('0'*(3-len(ms)))
        
    formattedTime.insert(2, ','.join([s, ms]))

    return ':'.join(formattedTime)

def addToTime(formattedTime, seconds=0):
    return intToTime(timeToInt(formattedTime)+seconds)

with open("Subtitles.srt", 'r') as file:
    subtitles = file.readlines()

timeToAdd = float(input("Hvað viltu breyta um mikið? : "))

with open("Subtitles_copy.srt", 'w') as file:
    for x in subtitles:
        if x[13:16] == "-->":
            newTime = f"{addToTime(x[0:12], timeToAdd)} --> {addToTime(x[17:29], timeToAdd)}\n"
            file.write(newTime)
        else:
            file.write(x)
        
