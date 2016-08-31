# Quick Sort algorithm. Return #comparisons during the sorting process.
# Tianjia Chen.

import random
import statistics

def quick_sort(A, n, method):
	# number of comparisons.
	num = 0

	if n == 0:
		return [A, 0]
	if n == 1:
		return [A, 0]

	# choose pivot. should return position of pivot as "l".
	[p, l] = choose_pivot(A, n, method)

	# partition A around p.
	[l, a] = partition(A, l, n)

	# recursively sort 1st part of A.
	[B, b] = quick_sort(A[:l], l, method)

	# recursively sort 2nd part of A.
	[C, c] = quick_sort(A[(l+1):], n-1-l, method)

	final = B + [int(p)] + C
	num = b + c + a

	return [final, num]


def partition(A, l, r):
	# Sort A based on pivot, and return the position of pivot in A, as well as number of comparisons.
	i = l + 1
	# pivot: p
	p = A[l]
	for j in range(l+1, r):
		# if A[j] < pivot, swap A[i] and A[j].
		if A[j] < p:
			inter = A[j]
			A[j] = A[i]
			A[i] = inter

			# swap pivot and A[i-1]
			i = i + 1
			inter = A[l]
			A[l] = A[i-1]
			A[i-1] = inter
			l = i-1

	return [A.index(p), r-1]


def choose_pivot(A, n, method):
	# always choose the first one as pivot
	if method == 'first':
		return [A[0],0]

	# always choose the last one as pivot
	if method == 'last':
		inter = A[n-1]
		A[n-1] = A[0]
		A[0] = inter

	## randomly choose pivot.
	if method == 'random':
		random_number = random.randint(0, n-1)
		inter = A[random_number]
		A[random_number] = A[0]
		A[0] = inter

	# "median-of-three"
	if method == 'median':
		if n%2 == 1:
			three_number = [A[0], A[n-1], A[n/2]]
		else:
			three_number = [A[0], A[n-1], A[(n/2)-1]]

		md = statistics.median(three_number)
		position = A.index(md)
		inter = A[position]
		A[position] = A[0]
		A[0] = inter

	return [A[0], 0]



[A, num] = quick_sort([2,5,7,8,3,6,4,1,0,10],10, 'median')
print(A)
print(num)
