'''
There's a school that has classes of students and each class has a final exam
You ahve classes[i] = [pass_i, total_i]
You are given an integer extraStudents. There are another extraStudents brilliant
students that are guaranteed to pass the exam of any class they are assigned to.
You want to assign each of the extra students to a class in a way that maximizes the
average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class 
that will pass the exam divided by the total number of students of the class.
The average pass ratio is the sum of pass ratios of all the classes divided
by the number of the classes.

Return the max possible average pass ratio after assigning the 
extraStudents students.
'''
     
from heapq import *
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        computeGain = lambda p, t: (1 - (p/t)) / (t + 1)
        R = [(-computeGain(p, t), p, t) for p, t in classes]
        heapify(R)

        for x in range(extraStudents):
            _, p, t = heappop(R)
            p += 1
            t += 1
            heappush(R, (-computeGain(p, t), p, t))
        
        ans = 0
        for x in R:
            ans += x[1] / x[2]
        return ans / len(classes)