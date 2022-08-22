class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        word_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = []
            word_dict[sorted_word].append(word)
        
        ans = []
        for word in word_dict:
            ans.append(word_dict[word])
        return ans
        