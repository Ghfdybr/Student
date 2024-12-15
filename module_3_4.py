def single_root_words(root_word, *other_words):
    same_words = []
    # Первый поиск, если корень (root_word) целиком входит в состав слова
    i = 1
    for i in range(len(other_words)):
        a = other_words[i]
        a = a.upper()
        b = root_word.upper()
        if a.find(b) == -1:
            i += 1
        else:
            same_words.append(other_words[i])
            i += 1
    # Второй поиск, если корень (root_word) частично входит в состав слова
    i = 1
    for i in range(len(other_words)):
        a = other_words[i]
        a = a.upper()
        b = root_word.upper()
        if b.find(a) == -1:
            i += 1
        else:
            same_words.append(other_words[i])
            i += 1

    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))