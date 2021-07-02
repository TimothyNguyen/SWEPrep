class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        temp = []
        heights.append(float('-inf'))
        for i, h in enumerate(heights):
            cpos = i
            while stack and h < stack[-1][0]:
                ch, cpos = stack.pop()
                temp.append(ch*(i - cpos))
            stack.append([h, cpos])
        return max(temp) if temp else 0