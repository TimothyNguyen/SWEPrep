class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_p = len(p)
        len_s = len(s)

        if len_p > len_s:
            return result

        # Count occurrences of each character in p
        p_count = Counter(p)
        # Initialize the window with the first len_p characters in s
        window_count = Counter(s[:len_p - 1])

        for i in range(len_p - 1, len_s):
            # Add the new character to the current window
            window_count[s[i]] += 1

            # If the window matches the frequency count of p, we found an anagram
            if window_count == p_count:
                result.append(i - len_p + 1)

            # Move the window: remove the leftmost character of the window
            window_count[s[i - len_p + 1]] -= 1
            if window_count[s[i - len_p + 1]] == 0:
                del window_count[s[i - len_p + 1]]

        return result
