def removeDuplicate(str):
    str = list(str)
    n = len(str)
    index = 0
    count = 0
    for i in range(0, n):
        for j in range(0, i + 1):
            if (str[i] == str[j]):

                break
        if (j == i):
            str[index] = str[i]
            count += 1
            index += 1
    res = "".join(str[:index])
    print(res)
    print(count)


removeDuplicate("abcabc")
