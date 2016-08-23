def sort_and_count(A, n):
	# if n is 1, no pairs.
	if n == 1:
		return (A, 0)
	
	(B, x) = sort_and_count(A[0:n/2], n/2)
	(C, y) = sort_and_count(A[n/2:], n-n/2)
	
	i = 0
	j = 0
	z = 0
	D = []

	for k in range(1,n+1):
		if B[i] < C[j]:
			D.append(B[i])
			i += 1
			if (i == len(B)):
				D += C[j:]
				break;
			
		elif B[i] > C[j]:
			D.append(C[j])
			j += 1
			z += len(B)-i
			if (j == len(C)):
				D += B[i:]
				break;
				
	return (D, x+y+z)


# testing.
f = open('/Users/Tianjia.Chen/Desktop/algorithms/week1.txt','r')
data = [int(l) for l in f]

[sort, x] = sort_and_count(data, len(data))
print x

	


