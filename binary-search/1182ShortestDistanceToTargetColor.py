'''
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two 
integers i and c, return the shortest distance between the 
given index i and the target color c. If there is no solution return -1.

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.

Time Complexity : O(QlogN+N), where Q is the length of queries and N
is the length of colors.

Going through the input array colors and storing each color - 
index pair take O(N) time. When iterating queries and generating 
results, we apply binary search once for each query, and each binary
search takes O(logN), which results in O(QlogN). Putting them together 
and ignoring constants for Big O notation, we have O(QlogN+N).

Space Complexity : O(N). This is because we store the indexes 
of each color - index pair in a hashmap.
'''
import collections

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(int)
        for i, c in enumerate(colors):
            hashmap[c].append(i)
        
        query_results = []
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                query_results.append(-1)
                continue
        
            index_list = hashmap[color]
            # use bisect from Python standard library
            # more details: https://docs.python.org/3/library/bisect.html
            insert = bisect.bisect_left(index_list, target)

            # compare the index on the left and right of insert
            # make sure it will not fall out of the index_list
            left_nearest = abs(index_list[max(insert - 1, 0)] - target)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - target)
            query_results.append(min(left_nearest, right_nearest))

        return query_results
'''
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # initializations
        n = len(colors)
        rightmost = [0, 0, 0]
        leftmost = [n - 1, n - 1, n - 1]

        distance = [[-1] * n for _ in range(3)]

        # looking forward
        for i in range(n):
            color = colors[i] - 1
            for j in range(rightmost[color], i + 1):
                distance[color][j] = i - j
            rightmost[color] = i + 1

        # looking backward
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(leftmost[color], i - 1, -1):
                # if the we did not find a target color on its right
                # or we find out that a target color on its left is
                # closer to the one on its right
                if distance[color][j] == -1 or distance[color][j] > j - i:
                    distance[color][j] = j - i
            leftmost[color] = i - 1

        return [distance[color - 1][index] for index,color in queries]
'''