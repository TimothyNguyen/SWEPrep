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

