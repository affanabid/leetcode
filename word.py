def word_order(words):
    order = []
    for i in range(len(words)):
        count = 0
        word = words[i]
        for j in range(len(words)):
            if word != -1 and word == words[j]:
                count += 1
                words[j] = -1
        if word != -1:
            order.append(count)
    data = ''
    for o in order:
        data += (str(o))
        data += ' '
    STDOUT = f"{len(order)}\n{data}"
    return STDOUT
    # print(len(order))
print(word_order(['bcdef', 'abcdefg', 'bcde', 'bcdef']))
