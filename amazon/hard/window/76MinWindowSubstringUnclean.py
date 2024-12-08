class Solution:
    def minWindow(self, s: str, t: str) -> str:
        word_dict = defaultdict(int)
        remaining_chars = len(t)
        for letter in t:
            word_dict[letter] += 1
        l, r = 0, 0
        saved_l, saved_r = -float('inf'), float('inf')
        while r < len(s):
            curr_char = s[r]
            if curr_char in word_dict:
                if word_dict[curr_char] > 0:
                    remaining_chars -= 1
                word_dict[curr_char] -= 1
            while remaining_chars == 0:
                if r - l < saved_r - saved_l:
                    saved_l, saved_r = l, r
                if s[l] in word_dict:
                    word_dict[s[l]] += 1
                    if word_dict[s[l]] > 0:
                        remaining_chars += 1
                l += 1
            if r < len(s):
                r += 1
        return s[saved_l:saved_r+1] if saved_r != float('inf') else ""
