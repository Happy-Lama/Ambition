arrangement = [-1,150,190,170,-1,-1,160,180]
heights = []
tree_indices = []
for tree_index, i in enumerate(arrangement):
	tree_indices.append(tree_index) if (i is -1) else heights.append(i)
heights_sorted = sorted(heights)
for i in tree_indices:
	heights_sorted.append(-1) if len(heights_sorted)<i else heights_sorted.insert(i,-1)
print(heights_sorted)