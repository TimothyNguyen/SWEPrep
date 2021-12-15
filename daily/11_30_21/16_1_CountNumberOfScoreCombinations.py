'''
In an American football Bame, a play can lead to 2 points (safety), 3 points (field goal), or 7 points
(touchdown, assuming the extra point). Many different combinations of 2,3, and 7 point plays can
make up a final score. For example, four combinations of plays yield a score of 12:
    - 6 safeties (2x6=12),
    - 3 safeties and 2 field goals (2 x 3 + 3 x2 = 72),
    - 1 safety, 1 field goal and 1 touchdown (2 x 1+ 3 x 1 +7 x1= 12), and
    - 4 field goals(3x4=12).

Write a program that takes a final score and scores for individual plays, and returns the number of
combinations of plays that result in the final score.
Hint: Count the number of combinations in which there are 0 w0 plays, then w1 plays, etc.

Time/Space: O(ns)
'''

class Solution:
    def count_combination(self, final_score: int, individual_scores: int):
        num_combinations = [[1] + [0] * final_score for _ in individual_scores]
        for i in range(len(individual_scores)):
            for j in range(1, final_score):
                without_play = (num_combinations[i-1][j] if i >= 1 else 0)
                with_play = (num_combinations[i-1][j - individual_scores[i]] if j >= num_combinations[i] else 0)
                num_combinations[i][j] = without_play + with_play
        return num_combinations[-1][-1]