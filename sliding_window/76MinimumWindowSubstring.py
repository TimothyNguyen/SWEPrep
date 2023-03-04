'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 
'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        1. Start with two pointers l & r
        2. Use right pointer r to expand window until we see all desired chars
        3. Then move the left pointer ahead one by one until we see only one occurrence
        4. Once window isn't desirable, we take the min window & we repeat step 2 
        5. Keep doing this until you get to the end of the string with right pointer "r"
        '''

        if not t or not s:
            return ""
        
        dict_t = collections.Counter(t)

        all_formed = 0
        required_char = len(dict_t)

        l, r = 0, 0

        min_len = float('inf')
        min_window_str = ""
        window_counter = collections.defaultdict(int)
        while r < len(s):
            # add to hashmap
            window_counter[s[r]] += 1

            if s[r] in dict_t and window_counter[s[r]] == dict_t[s[r]]:
                all_formed += 1
            
            while l <= r and all_formed == required_char:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window_str = s[l:r+1]
                window_counter[s[l]] -= 1

                if window_counter[s[l]] < dict_t[s[l]]:
                    all_formed -= 1
                l += 1
            r += 1
        return min_window_str

class Solution2:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    

            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]