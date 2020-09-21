def stafrof(word):
    if len(word) == 1:
        return word
    else:
        for letter in word:
            try:
                if ord(letter) < ord(lowest):
                    lowest = letter 
            except:
                lowest = letter

        return lowest + stafrof(word.replace(lowest, '', 1))

print(stafrof("1dsnajk321"))