import time
from math import prod

input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = []
	matrix = []
	for line in file:
		arrey.append([ell for ell in line.strip().split(" ") if ell != '']) 
		matrix.append([])
		matrix[-1] = [c for c in line if c != '\n']
	for i in range(len(arrey) - 1):
		arrey[i] = list(map(int, arrey[i]))

def day06_pt2(matrix):
	m = len(matrix)
	n = len(matrix[0])
	i = 0
	res = 0
	while i < n:
		j = 1
		while i + j < n and matrix[-1][i + j] == ' ':
			j += 1
		if i + j < n:
			j -= 1
		arrey_nb = [0] * (j)
		for k in range(j):
			for l in range(m - 1):
				if matrix[l][i + k] != ' ':
					arrey_nb[k] *= 10					
					arrey_nb[k] += int(matrix[l][i + k])
		res += sum(arrey_nb) if matrix[-1][i] == '+' else prod(arrey_nb)
		i += j + 1
	return res

def day06_pt1(arrey): return sum([sum([arrey[x][i] for x in range(len(arrey) - 1)]) if arrey[-1][i] == '+' else prod([arrey[x][i] for x in range(len(arrey) - 1)]) for i in range(len(arrey[0]))])

s = time.time()
print(f"{day06_pt1(arrey)} in {round(time.time() - s, 5)}s")
s = time.time()
print(f"{day06_pt2(matrix)} in {round(time.time() - s, 5)}s")