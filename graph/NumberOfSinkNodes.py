def num_sink_nodes(n, m, edgeFrom, edgeTo):
    mark = [0] * (n + 1)
    for i in range(m):
        mark[edgeFrom[i]] = 1
    count = 0
    for i in range(1, n+1):
        if mark[i] == 0:
            count += 1
    return count