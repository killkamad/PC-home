def lower_upper(s):
    change = []

    for char in s:
        if char.islower():
            change.append(char.upper())
        elif char.isupper():
            change.append(char.lower())
        else:
            change.append(char)

    return ''.join(change)


if __name__ == '__main__':
    print(lower_upper("AliK"))