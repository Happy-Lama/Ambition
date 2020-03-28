#CHALLENGE
""" Some people are standing in a row in a particular park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in non-descending order without moving the trees
Example:
a = [-1,150,190,170,-1,-1,160,180] and your nswer should be = [-1,150,160,170,-1,-1,180,190]"""


def heights_ascending(arrangement,tree):
	""" This function takes in a list of the arrangement of trees and people(denoted by heights) and a character denoting a tree.
	The logic behind this solution is that since we are only arranging people by their heights is non-descending order,then we 
	first separate the people from the trees and handle them alone, and then place them back respectively between the trees similar
	to the first arrangement they were in."""
	heights = []
	tree_indices = []
	for tree_index ,i in enumerate(arrangement):
		tree_indices.append(tree_index) if (i is tree) else heights.append(i)
	heights_sorted = sorted(heights)
	for i in tree_indices:
		heights_sorted.append(tree) if len(heights_sorted)<i else heights_sorted.insert(i,tree)
	return heights_sorted
arrangement =  [-1,150,190,170,-1,-1,160,180]
print(heights_ascending(arrangement,-1))
