import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	res=[]
	for i in a:
		val = np.dot(i,b)
		res.append(val)
	return res
	
	