import numpy as np

def calculate_dot_product(vec1, vec2):
	n1 = vec1
	n2 =vec2

	mult = n1*n2
	res = mult.sum()

	return res