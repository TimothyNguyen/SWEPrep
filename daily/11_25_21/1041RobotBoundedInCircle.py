# On an infinite plane, a robot initially stands at (0, 0) and faces north. 
# The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the 
# robot never leaves the circle.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3 
        dir_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        idx = 0
        for letter in instructions:
            if letter == 'L':
                idx = (idx + 3) % 4
            elif letter == 'R':
                idx = (idx + 1) % 4
            else:
                x += dir_arr[idx][0]
                y += dir_arr[idx][1]
        return (x == 0 and y == 0) or idx != 0