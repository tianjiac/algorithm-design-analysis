# Random Contraction Algorithm.
# Tianjia Chen


import random
import copy


def random_contraction_algorithm(adj_list_original, number):
	""" It retuns minimum cut of an undirected graph.

		Input: 
			adj_list_original: A dictionary-formated adjacent list. 
			The keys represent vertices, and the values represent adjacent
			vertices for that specific vertex in key.
			number: nunmber of iterations.
	"""

	# Get number of vertices in the graph.
	n = len(adj_list_original.keys())

	# Create a list storing min cuts in each iteration.
	num_list = []

	# Iteration begins.
	for i in range(0, number):

		# Deepcopy the original dictionary each time.
		adj_list = copy.deepcopy(adj_list_original)

		# Contract the graph until there are only 2 vertices.
		while (len(adj_list.keys()) > 2):

			# Randomly pick a remaining edge.
			u = random.choice(list(adj_list.keys()))
			v = random.choice(adj_list[u])

			# Merge edge(u,v). Rule: u --> v. 
			# Add edges for u to v.
			adj_list[u] = [x for x in adj_list[u] if x != v]
			adj_list[v] = adj_list[v] + adj_list[u]

			# Delete self-loop.
			del adj_list[u]

			# Delete edges like (v, v).
			adj_list[v] = [x for x in adj_list[v] if x != u]

			# Update u --> v for other vertices.
			for key, item in adj_list.items():
				if u in item:
					for k in item:
						if k == u:
							item[item.index(k)] = v

		# Get min-cut within this iteration.
		result = max([len(x) for x in adj_list.values()])

		# Put min-cut into list.
		num_list.append(result)

	# Return min of "min-cuts" in all iterations.
	return min(num_list)

# Test with simple graph.
# adj_list = {1: [2,3,4],
#  			 2: [1,3,4],
# 			 3: [1,2,4],
#			 4: [1,2,3]}

# result = random_contraction_algorithm(adj_list, 100)
# print(result)


# Do data.txt

# Read file.
lines = [line.rstrip('\t\n') for line in open('/Users/Tianjia.Chen/Desktop/algorithms/algorithm-design-analysis/week3/data.txt')]

# Create input adjacent list dictionary.
adj_list_original = {}
for line in lines:
	tmp = [int(x) for x in line.split('\t')]
	adj_list_original[tmp[0]] = tmp[1:]

result = random_contraction_algorithm(adj_list_original, 100)
print(result)

# Result is 17.


