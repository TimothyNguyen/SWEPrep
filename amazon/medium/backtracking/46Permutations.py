from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            # Base case
            if i == len(nums):
                ans.append(list(nums))
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                print(nums)
        ans = []
        backtrack(0)
        return ans
# https://pythontutor.com/render.html#code=from%20typing%20import%20List%0A%0Aclass%20Solution%3A%0A%20%20%20%20def%20permute%28self,%20nums%3A%20List%5Bint%5D%29%20-%3E%20List%5BList%5Bint%5D%5D%3A%0A%20%20%20%20%20%20%20%20def%20backtrack%28i%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20Base%20case%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3D%3D%20len%28nums%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ans.append%28list%28nums%29%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%0A%20%20%20%20%20%20%20%20%20%20%20%20for%20j%20in%20range%28i,%20len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D,%20nums%5Bj%5D%20%3D%20nums%5Bj%5D,%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20backtrack%28i%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nums%5Bi%5D,%20nums%5Bj%5D%20%3D%20nums%5Bj%5D,%20nums%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28nums%29%0A%20%20%20%20%20%20%20%20ans%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20backtrack%280%29%0A%20%20%20%20%20%20%20%20return%20ans%0A%0Asolution%20%3D%20Solution%28%29%0Anums%20%3D%20%5B1,%202,%203%5D%0Aprint%28sorted%28solution.permute%28nums%29%29%29&cumulative=false&curInstr=52&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false