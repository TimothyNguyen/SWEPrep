'''
You are given an integer n, which indicates that there are n courses 
labeled from 1 to n. You are also given an array relations where 
relations[i] = [prevCoursei, nextCoursei], representing a prerequisite 
relationship between course prevCoursei and course nextCoursei: course 
prevCoursei has to be taken before course nextCoursei. Also, you are 
given the integer k.

In one semester, you can take at most k courses as long as you have taken 
all the prerequisites in the previous semesters for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The 
testcases will be generated such that it is possible to take every course.

 

Example 1:

Input: n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
Output: 3
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 2 and 3.
In the second semester, you can take course 1.
In the third semester, you can take course 4.

Example 2:

Input: n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4
Explanation: The figure above represents the given graph.
In the first semester, you can only take courses 2 and 3 since you cannot 
take more than two per semester.

In the second semester, you can take course 4.
In the third semester, you can take course 1.
In the fourth semester, you can take course 5.
'''
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        pre = [0] * n
        shortest = [n + 1] * (1 << (n)) # remember shortest steps for each state
        TARGET = (1 << n) - 1  # zero-based index
        for dep in dependencies: # u -> v
            u, v = dep[0] - 1, dep[1] - 1
            pre[v] += 1 << u  
        queue = deque([[0, 0]])  # (state, step count)
        while queue:
            [state, step] = queue.popleft()
            potential_new_courses = []  # new courses to study
            for i in range(n):
                if pre[i] & state != pre[i]: # not enough prereq
                    continue
                if (1<<i) & state != 0: # already studies this course
                    continue
                potential_new_courses.append(i)     

            if len(potential_new_courses) <= k:  # study all in this semester
                for course in potential_new_courses: 
                    state += 1 << course
                if state == TARGET: 
                    return step+1
                if shortest[state] > step+1: 
                    queue.append([state,step+1])
                    shortest[state] = step+1
            else: # can only take part of courses this semester
                for seq in list(combinations(potential_new_courses,k)):
                    new_state = state
                    for course in list(seq): 
                        new_state += 1 << course
                    if shortest[new_state] > step + 1:
                        queue.append([new_state, step + 1])
                        shortest[new_state] = step + 1