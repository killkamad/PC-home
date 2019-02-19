def merge_lists(a, b):

    result = []
    i = 0
    j = 0

    for k in range(len(a) + len(b)):
        if a[i] <= b[j]:
            result.append(a[i])
            if i < len(a) - 1:
                i += 1
            else:
                result += b[j:]
                print(b[j:])
                break
        else:
            result.append(b[j])
            if j < len(b) - 1:
                j += 1
            else:
                result += a[i:]
                print(a[i:])
                break
    return result

a = [1, 3, 5, 6, 8, 8, 9]
b = [2, 4, 6, 8, 9, 10, 12]
print(merge_lists(a, b))

x=[5,6,7]
l=[7,8,9,10]
g=x+l[2:]
print(g)
