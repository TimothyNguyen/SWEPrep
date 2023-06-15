# /*
# class Solution:
#     def minCut(self, s: str) -> int:
#         self.ans = float('inf')
#         def isPalindrome(s):
#             for i in range(len(s) // 2):
#                 if s[i] != s[len(s) - i - 1]:
#                     return False
#             return True
                
#         def dfs(curr=[], index=1):
#             if index == len(s) + 1:
#                 self.ans = min(self.ans, len(curr) - 1)
#                 return
#             if self.ans <= len(curr):
#                 return
#             for i in range(index, len(s)+1):
#                 if isPalindrome(s[index-1:i]):
#                     curr.append(s[index-1:i])
#                     dfs(curr, i+1)
#                     curr.pop()
#         dfs()
#         return self.ans

# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1

# Time: O(N^2 * N)
# Space: O(N^2)

class Solution:
    def minCut(self, s: str) -> int:
        self.ans = float('inf')
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True
                
        def dfs(curr=[], index=1):
            if index == len(s) + 1:
                self.ans = min(self.ans, len(curr) - 1)
                return
            if self.ans <= len(curr):
                return
            for i in range(index, len(s)+1):
                if isPalindrome(s[index-1:i]):
                    curr.append(s[index-1:i])
                    dfs(curr, i+1)
                    curr.pop()
        dfs()
        return self.ans

# // class Solution {

# //     private Integer memoCuts[][];
# //     private Boolean memoPalindrome[][];

# //     public int minCut(String s) {
# //         memoCuts = new Integer[s.length()][s.length()];
# //         memoPalindrome = new Boolean[s.length()][s.length()];
# //         return findMinimumCut(s, 0, s.length() - 1, s.length() - 1);
# //     }

# //     private int findMinimumCut(String s, int start, int end, int minimumCut) {
# //         // base case
# //         if (start == end || isPalindrome(s, start, end)) {
# //             return 0;
# //         }
# //         // check for results in memoCuts
# //         if (memoCuts[start][end] != null) {
# //             return memoCuts[start][end];
# //         }
# //         for (int currentEndIndex = start; currentEndIndex <= end; currentEndIndex++) {
# //             if (isPalindrome(s, start, currentEndIndex)) {
# //                 minimumCut = Math
# //                     .min(minimumCut, 1 + findMinimumCut(s, currentEndIndex + 1, end, minimumCut));
# //             }
# //         }
# //         return memoCuts[start][end] = minimumCut;
# //     }

# //     private boolean isPalindrome(String s, int start, int end) {
# //         if (start >= end) {
# //             return true;
# //         }
# //         // check for results in memoPalindrome
# //         if (memoPalindrome[start][end] != null) {
# //             return memoPalindrome[start][end];
# //         }
# //         return memoPalindrome[start][end] = (s.charAt(start) == s.charAt(end))
# //             && isPalindrome(s, start + 1, end - 1);
# //     }
# // }