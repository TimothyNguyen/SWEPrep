'''
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.
'''
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ans = []
        
        if len(changed) % 2 == 1:
            return ans
        
        changed.sort()
        
        freq_map = defaultdict(int)
        
        for elem in changed:
            freq_map[elem] += 1
        
        for elem in changed:
            # print(freq_map)
            if elem in freq_map:
                if elem * 2 in freq_map:
                    ans.append(elem)
                    freq_map[elem] -= 1
                    freq_map[elem * 2] -= 1
                    if freq_map[elem] == 0: 
                        del freq_map[elem]
                    if freq_map[elem * 2] == 0:
                        del freq_map[elem * 2]
                else:
                    return []
            
        return ans if len(freq_map) == 0 else []
                