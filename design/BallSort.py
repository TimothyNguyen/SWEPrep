'''
Ball sort is a game where you start with test tubes with 4 balls each, except for 2 empty test tubes. 
The goal is to place all balls of the same color in the same test tube. 

There are 3 simple rules to this game: 

You cannot place a ball of a different color on top of another ball (ex. no red balls 
can be put on top of orange balls). 

Test tubes can contain a max of 4 balls. 

A ball of any color can be moved to an empty test tube. 
'''
# bound: 5 (3 <= x <= y)
# 3 colors
# starting state - 3 full and 2 empty
# Color distribution can be whatever
# Test tubes 
# colors are ints
def ball_sort(test_tubes: List[List[int]]):
	# First identify the empty tubes (For loop)
	tubes_dict = {idx: 'color'}
	empty_tube_set = set()
	for tube in tubes: 
		if len(tube) == 0:
			empty_tube_set.add(tube)
	arr = [False] * len(empty_tubes)
	color_tube = []
	for idx of empty_tube_set:
		send the ball initial empty tube
		while color is the same from the first tube that's non empty:
			tubes_dict[index of the tube] += 1
			color_tube[index of the tube] = color
	if tube is full and 


[[B Y Y Y],
 [Y],
 [],
 [B B B],
 [R R R R]