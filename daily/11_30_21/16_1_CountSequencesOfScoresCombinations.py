'''
Write a program that takes a final score and scores for individual plays, and retums the
number of sequences of plays that result in the final score. For example, 18 sequences of plays yield
a score of 12. Some examples are (2,2,2,3,3), <2,3,2,2,3>, <2,3,7), <7,3,2>.
'''
class Solution:
    def count_combination(self, final_score: int, individual_scores: int):
        res = []
        def backtrack(res, individual_scores, temp_list, remain, index):
            if remain < 0:
                return
            elif remain == 0:
                iter_list = []
                for elem in temp_list:
                    iter_list.append(elem)
                res.append(iter_list)
            else:
                for i in range(index, len(individual_scores)):
                    temp_list.append(individual_scores[i])
                    backtrack(res, individual_scores, temp_list, remain - individual_scores[i], index + 1)
                    temp_list.pop(-1)

        individual_scores.sort()
        backtrack(res, individual_scores, [], final_score, 0) 
        return len(res)
