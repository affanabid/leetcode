def logo(string):
    done = []
    data = []
    for i in range(len(string)):
        count = 0
        letter = string[i]
        if letter not in done:
            for j in range(len(string)):
                if letter == string[j]:
                    count += 1
                    w = string[j]
                    done.append(w)
            # print(f'{letter}: {count}')
            data.append(f'{letter} {count}')
    for i in range(len(data)):
        entry = data[i].split()
        letter = entry[0]
        count = entry[1]
        # print(letter, count)

logo('aaaabbbccddddd')

