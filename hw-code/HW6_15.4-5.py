def LIS(A):
	n = len(A)
	d = [ 0  for _ in range(n) ]
	b = [ -1 for _ in range(n) ]
	m = 0

	for i in range(n):
		for j in range(i):
			if A[j] < A[i] and d[j] >= d[i]:
				d[i] = d[j] + 1
				b[i] = j
				if d[i] > d[m]:
					m = i

	r = []
	while m != -1:
		r = [A[m]] + r
		m = b[m]

	return r


print LIS([4,2,6,1,9,0,11,7,12])
