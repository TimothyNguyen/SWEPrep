# Given four points in the plane, how would you check if they are the 
# vertices of a rectangle?
import collections

Point = collections.namedtuple('Point', ('x', 'y'))

def is_rectangle(p1, p2, p3, p4):
    def is_orthogonal(a, b, c):
        return (b.x - a.x) * (b.x - c.x) + (b.y - a.y) * (b.y - c.y) == 0
    
    return is_orthogonal(p1, p2, p3) and is_orthogonal(p2, p3, p4) and is_orthogonal(p3, p4, p1)

# Time Complexity: O(1)