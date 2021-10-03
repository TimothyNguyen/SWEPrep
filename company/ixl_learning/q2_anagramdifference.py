'''
We define an anagram to be a word whose characters can be 
rearranged to create another word. Given two strings, we want 
to know the minimum number of characters that we must modify 
to make two strings anagrams. If its not possible to make 
two strings anagrams, we consider this number to be -1.

For example,

- tea and ate are anagrams, so we would need to modify 0 characters.
- tea and toe are not anagrams, but we can modify 1 
  character in either string (o -> a or a-> o) to make them anagrams.
- act and acts are not anagrams and cannot be converted 
  to anagrams because they contain different numbers of characters.

Complete the function getMinimumDifference in the editor below. 
The function must return an array of integers which denote the
minimum number of characters in either string that need to be 
modified to make the two strings anagrams. If its not possible, 
return -1.
'''


'''
Iterate over each word in the array, then iterate over each 
character in the first word.

For each character, if its in the first word and the second word, then
increment the counter by the difference between the number of times the
character appears in the first word and the number of times it appears in the
second. If the character in the first word does not appear at all in the
second word, then increment the counter by the number of times the letter
appeared in the first word.
Algorithm runs in O(N) time where N is the length of the word.
'''
import collections

def getMinimumDifference(a: str, b: str):
    differences_array = []
    for array_index, word in enumerate(a):
        
        if len(word) != len(b[array_index]):
            differences_array.append(-1)
            continue

        word_difference = 0

        word_1_freq = dict(collections.Counter(a[array_index]))
        word_2_freq = dict(collections.Counter(b[array_index]))
        
        for letter, value in word_1_freq.items():
            if letter in word_2_freq:
                word_difference += abs(word_1_freq[letter] - word_2_freq[letter])

            else:
                word_difference += value

        differences_array.append(word_difference)

    return differences_array

a = ['a', 'jk', 'abb', 'mn', 'abc']
b = ['bb', 'kj', 'bbc', 'op', 'def']
print(getMinimumDifference(a, b))
