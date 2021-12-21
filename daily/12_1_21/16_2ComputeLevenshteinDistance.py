'''
Write a Program that takes two strings and computes the minimum number of edits needed to
transform the first string into the second string.
Hint: Consider the same problem for prefixes of the two strings.
'''

class Solution:
    def levenhshtein_distance(self, word1: str, word2: str):
        m, n = len(word1), len(word2)
        # if one of the strings is empty
        if n * m == 0:
            return n + m
        
        # array to store the convertion history
        dp = [ [0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                topleft = dp[i-1][j-1]
                left = dp[i][j-1] + 1
                top = dp[i-1][j] + 1
                if word1[i - 1] != word2[j - 1]:
                    topleft += 1
                dp[i][j] = min(left, topleft, top)
        return dp[m][n]


# A Space efficient Dynamic Programming
# based Python3 program to find minimum
# number operations to convert str1 to str2
def EditDistDP(str1, str2):
      
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0 for i in range(len1 + 1)] for j in range(2)]

    for i in range(len1 + 1):
        dp[0][i] = i
    
    # Start filling the DP
    # This loop run for every
    # character in second String
    for i in range(1, len2 + 1):
        # This loop compares the char from
        # second String with first String
        # characters
        for j in range(len1 + 1):
            # If first String is empty then
            # we have to perform add character
            # operation to get second String
            if j == 0:
                dp[i % 2][j] = i
            # If character from both strings are the same, 
            # we don't perform any operations. Here i % 2 is for
            # bound the row number
            elif str1[j-1] == str[i-1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]

            # If character from both String is
            # not same then we take the minimum
            # from three specified operation
            else:
                dp[i % 2][j] = (1 + min(dp[(i-1) % 2][j], dp[i % 2][j - 1], dp[(i-1) % 2][j-1]))

        return dp[len2 % 2][len1]