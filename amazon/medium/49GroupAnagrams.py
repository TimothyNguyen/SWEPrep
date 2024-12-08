import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = collections.defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)

        ans = []
        for vals in anagram_dict.values():
            ans.append(vals)
        return ans