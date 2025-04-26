def uncommon_from_sentences(s1, s2):
    count_s1 = {}
    count_s2 = {}
    result = []


    for word1 in s1.split():
        count_s1[word1] = True

    for word2 in s2.split():
        count_s2[word2] = True

    for word in s1.split():
        if word not in count_s2:
            result.append(word)

    for word in s2.split():
        if word not in count_s1:
            result.append(word)

    return result


print(uncommon_from_sentences("the cat sleeps", "the dog sleeps"))
