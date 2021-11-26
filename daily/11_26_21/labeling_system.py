# https://leetcode.com/discuss/interview-question/1331455/amazon-oa-june-2021-labeling-system-multiprocessor-system
'''
Labeling System
Amazon is looking to develop a new labeling system in the fulfilment centers. 
New labels will be devised from the original string labels. Given the original 
string label, construct a new string by rearranging the original string and deleting 
characters as needed. Return the alphabetically-largest string that can be constructed 
respecting the limit as to how many consecutive characters can be the same (represented by k).

"Alphabetically-largest" is defined in reverse alphabetical order (e.g., b is 
"larger" than a, c is "larger" than b, etc.) from left to right (e.g., "ba" is larger than "ab").

Write an algorithm to return the alphabetically-largest string that can be 
constructed respecting the above limits.

Input
The input to the function/method consists of two arguments:
originalLabel, a string representing the original string label;
charLimit, an integer representing the maximum number of identical consecutive 
characters the new string can have (k).

Output
Return a string representing the alphabetically largest string that can be 
constructed that has no more than k identical consecutive characters.
'''
def largest_str(originalLabel: str, charLimit: int) -> str:
    new_label = ''
    old_label = sorted(originalLabel, reverse=True)
    map_count = dict()
    for letter in old_label:
        if letter not in map_count:
            map_count[letter] = 0
        if map_count[letter] < charLimit:
            map_count[letter] += 1
            new_label += letter
    return new_label

print(largest_str('ajaawiasdkffddxxyynnmf', 2))

