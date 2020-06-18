def problem_a(a):
    b = []
    count = 0
    run = True
    while run:
        for i in range(len(a)):
            if (a.index(a[i]) % 2) == 0:
                if a[i] % 2 == 0:
                    b.append((a[i]))
                    count += 1
        if count == 0:
            return 0
        else:
            s = sum(b) / count
            return round(s, 6)


if __name__ == '__main__':
    print(problem_a([1, 2, 3, 4, 5, 6, 7]))
    print(problem_a([62, 94, 92, 96, 10, 43, 63, 80]))
