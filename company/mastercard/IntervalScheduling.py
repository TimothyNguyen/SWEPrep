def interval_scheduling(R, O):
    R.sort(key =lambda x: x[1])
    finish = 0
    for r in R:
        if finish <= r[0]:
            finish = r[1]
            O.append(r)
    return O
# [1, 5, 8]
# [2, 8, 10]