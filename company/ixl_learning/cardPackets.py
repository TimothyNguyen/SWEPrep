def cardPackets(cardTypes):
    ans = len(cardTypes)
    max_num = max(cardTypes)

    cnt = [0] * (max_num + 1)
    for i in range(len(cardTypes)):
        cnt[cardTypes[i]] += 1

    for digit in range(2, max_num + 1):
        temp_ans = 0
        i = 0
        while i <= max_num and temp_ans < ans:
            temp_ans += cnt[i] * ((digit - (i % digit)) % digit)
            i += 1
        ans = min(ans, temp_ans)
    return ans