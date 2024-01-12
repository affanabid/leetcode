def common_prefix(strs):
    common = []
    for i in range(len(strs)):
        word = strs[i]
        for j in range(len(word)):
            alphabet = word[j]
            if alphabet 

strs = ['name', 'nail', 'naive']
common_prefix(strs)