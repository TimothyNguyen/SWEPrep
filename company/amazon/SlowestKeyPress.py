'''
Amazon engineers have redesigned a keypad used by delivery drivers in urban areas. 
In order to determine which key takes the longest time to press, the keypad is tested by a driver.
Given the results of that test which contains encoded key pressed and the time at which 
it was pressed, write an algorithm to determine which key takes the longest to press.

Input
The input to the function/method consists of two arguments:
num, an integer representing the number of keys;
keyTimes, a list of pairs of integers where the first element representing the encoded 
key pressed and the second element representing the time at which it was pressed.

Output
Return a character representing the key that took the longest time to press.

Note
There will only be one key with the longest time.
keyTimes is sorted in ascending order of keyTimes[i][1].
Encoded key characters in the range ascii[a-z] where a = 0, b = 1, ..., Z = 25.
The starting time of the test is 0.

Constraints
1 <= num <= 10^5
0 <= keyTimes[i][0] <= 25, where keyTimes[i][0] represents the first element of keyTimes.
1 <= keyTimes[i][1] <= 10^8, where keyTimes[i][1] represents the second element of keyTimes.
0 <= i < num

Example
Input:
num= 4
keyTimes = [(0, 2), (1,5), (0.9), (2, 15)]

Output:
c

Explanation:
Elements in keyTimes[i][0] represent encoded characters in the range ASCII[a-z] 
where a = 0, b = 1,..., z = 25. The second element, key Times (1) represents the time 
the key is pressed since the start of the test. The elements will be given in ascending 
time order. In the example, keys pressed, in order are 0102 and encoded as = abac at 
times 2,5,9, 15. From the start time, it took 2 - 0 = 2 to press the first key, 5 - 2 = 3 
to press the second, and so on. The longest time it took to press a key was key 2, or 'c', 
at 15 - 9 = 6.

Helper Description
The following class is used to represent a Pair of integers which is already implemented 
in the default code (Do not write this definition again in your code):
'''
"""
Examples:
              0123
keyPressed = "cbcd"
                0   1   2   3
releaseTimes = [9, 29, 49, 50]
                           i

durations = {
    c: 20,
    b: 20
    d: 1
}

Time: O(n)
Space: O(n)
"""
from collections import defaultdict
import sys
def slowest_key(keys_pressed, release_times):
    if len(keys_pressed) != len(release_times): return None
    durations = defaultdict(lambda: 0)
    durations[keys_pressed[0]] = release_times[0]

    for i in range(1, len(release_times)):
        durations[keys_pressed[i]] = max(durations[keys_pressed[i]], release_times[i] - release_times[i - 1])

    max_time = -sys.maxsize
    max_key = ""
    for k in durations:
        if durations[k] > max_time: 
            max_time = durations[k]
            max_key = k
    
    for k in durations:
        if durations[k] == max_time and ord(k) - ord('a') > ord(max_key) - ord('a'): 
            max_key = k
    
    return max_key

import unittest
class TestSlowestKeys(unittest.TestCase):
    def test_generic(self):
        self.assertEqual("c", slowest_key("cbcd", [9, 29, 49, 50]))
        self.assertEqual("a", slowest_key("spuda", [12, 23, 36, 46, 62]))

if __name__ == "__main__": unittest.main()