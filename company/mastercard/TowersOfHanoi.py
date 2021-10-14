'''
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you 
have 3 towers and N disks of different sizes which can slide onto 
any tower. The puzzle starts with disks sorted in ascending order of 
size from top to bottom (i.e., each disk sits on top of an even larger one).
'''
def moveTowers(n, origin, buffer, destination):
    if n == 1:
        print("Move disc 1 from " + origin + " to " + destination)
        return
    if n > 0:
        moveTowers(n-1, origin, destination, buffer)
        print("Move disc " + n + " from " + origin + " to " + destination)
        moveTowers(n-1, buffer, origin, destination)
# Time Complexity: T(n) = 2T(n-1) + T(1)
