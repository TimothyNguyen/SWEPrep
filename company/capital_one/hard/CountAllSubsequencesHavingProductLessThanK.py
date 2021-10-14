'''
Given a positive array, find the number of subsequences having product smaller than K.
'''

def productSubSeqCount(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n+1)] for j in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            # Number of sequences using j - 1 terms
            dp[i][j] = dp[i][j-1]

            # if arr[j - 1] > i, it will make product greater
            if arr[j-1] <= i and arr[j-1] > 0:
                dp[i][j] += dp[i // arr[j-1]][j-1] + 1
    return dp[k][n]