def problem_b(s):
    a = list(map(len, s.split()))
    b = " ".join(map(str, a))
    return b


if __name__ == '__main__':
    print(problem_b("Alik Ayana Dias Elvira"))
    print(problem_b(
        "plpq cqhtemxzrjinbfigrexj fsoagndkuilweidftbost ikidxpahiadibcokkvweeeuklgbowgmenefjksyrvkdiuypl ajcupke diugljkbkuptwdtcghnuttupgbcanguwgpl gzxfhiethqqsfstrxq"))
