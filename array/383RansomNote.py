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