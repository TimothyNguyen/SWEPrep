def rand7From5(self):
    while True:
        r = rand5()
        c = rand5()
        idx = c + (r - 1) * 5
        if idx <= 20:
            break
    return 1 + (idx - 1) % 7