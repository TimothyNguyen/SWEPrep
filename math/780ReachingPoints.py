class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if sx == tx and sy == ty:
                return True
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


'''
Approach #4: Work Backwards (Modulo Variant) [Accepted]
Intuition

As in Approach #3, we work backwards to find the answer, trying to transform the target point to the starting point via applying the parent operation (x, y) -> (x-y, y) or (x, y-x) [depending on which one doesn't have negative coordinates.]

We can speed up this transformation by bundling together parent operations.

Algorithm

Say tx > ty. We know that the next parent operations will be to subtract ty from tx, until such time that tx = tx % ty. When both tx > ty and ty > sy, we can perform all these parent operations in one step, replacing while tx > ty: tx -= ty with tx %= ty.

Otherwise, if say tx > ty and ty <= sy, then we know ty will not be changing (it can only decrease). Thus, only tx will change, and it can only change by subtracting by ty. Hence, (tx - sx) % ty == 0 is a necessary and sufficient condition for the problem's answer to be True.

The analysis above was for the case tx > ty, but the case ty > tx is similar. When tx == ty, no more moves can be made.
'''