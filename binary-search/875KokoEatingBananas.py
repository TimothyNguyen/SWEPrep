'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards 
have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and 
eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and 
will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        '''
        speed = 1
        while True:
            hour_spent = 0
            for pile in piles:
                hour_spent += math.ceil(pile/speed)
            
            if hour_spent <= h:
                return speed
            else:
                speed += 1
        '''
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)

        if h == len(piles):
            return right
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right