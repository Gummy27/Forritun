def word_mixer(word_list):
    word_list.sort()
    new_words = []
    while len(words_list) > 5:
        new_words.append(words_list.pop(-5))
        new_words.append(words_list.pop(0))
        new_words.append(words_list.pop(-1))

    return new_words

words_list = input().split(' ')
lengd = len(words_list)

for x in range(lengd):
    if len(words_list[x]) >= 6:
        words_list[x] = words_list[x].upper()
    else:
        words_list[x] = words_list[x].lower()

print(' '.join(word_mixer(words_list)))

