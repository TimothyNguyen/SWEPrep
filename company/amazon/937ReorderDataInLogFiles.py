'''
You are given an array of logs. Each log is a space-delimited string of words, where the 
first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the 
same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []
        for log in logs:
            splitted_log = log.split(" ")
            content = " ".join(splitted_log[1:])
            if content[0].isalpha():
                letter_logs.append((content, splitted_log[0], log))
            else:
                digit_logs.append(log)

        letter_logs = sorted(letter_logs, key=lambda x: (x[0], x[1]))
        return [log[2] for log in letter_logs] + digit_logs        