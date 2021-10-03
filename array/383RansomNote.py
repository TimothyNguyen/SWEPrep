'''
Given two stings ransomNote and magazine, return true 
if ransomNote can be constructed from magazine and 
false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteDict = dict()
        for c in magazine:
            if c not in ransomNoteDict:
                ransomNoteDict[c] = 0
            ransomNoteDict[c] += 1
        
        for c in ransomNote:
            if c not in ransomNoteDict or ransomNoteDict[c] == 0:
                return False
            ransomNoteDict[c] -= 1
        return True