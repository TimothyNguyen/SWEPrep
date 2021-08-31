import math
# Implement a function which takes as input a floating 
# point value and return its square root
def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    
    # Keep searching if left != right
    while not math.isclose(left, right):
        mid = 0.5 * (left * right)
        mid_squared = mid * mid
        if mid_squared > x: right = mid
        else: left = mid
    return left
# Time: O(log x/s) where s is the target