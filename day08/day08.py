import time
from math import sqrt, dist

input_file = "input.txt"

with open(input_file, "r") as file:
	arrey = [tuple(map(int, line.strip().split(','))) for line in file]

def ft_creat_lst(arrey, len_arrey):
	lst = []
	for i in range(len_arrey - 1):
		x1, y1, z1 = arrey[i]
		for j in range(i + 1, len_arrey):
			x2, y2, z2 = arrey[j]
			ell = (dist((x1, y1, z1), (x2, y2, z2)), i, j)
			lst.append(ell)
	lst.sort(key= lambda x:x[0])
	return (lst)

def day08_pt1(arrey):
	len_arrey = len(arrey)
	groups_index = [x for x in range(len_arrey)]
	groups = {x:[x] for x in range(len_arrey)}
	lst = ft_creat_lst(arrey, len_arrey)

	for _, index_p1, index_p2 in lst[:1000]:
		gp_p1, gp_p2 = groups_index[index_p1], groups_index[index_p2]
		if gp_p1 == gp_p2:
			continue
		res = [index_p1, index_p2]
		to_add = groups[gp_p2]
		for point in to_add:
			groups_index[point] = gp_p1
			groups[gp_p1].append(point)
		del groups[gp_p2]
	
	m1, m2, m3 = 0, 0, 0
	for key, value in groups.items():
		l = len(value)
		if l > m1: m1, m2, m3 = l, m1, m2
		elif l > m2: m2, m3 = l, m2
		elif l > m3: m3 = l
	return(m1 * m2 * m3)
	
def day08_pt2(arrey):
	lst = []
	len_arrey = len(arrey)
	groups_index = [x for x in range(len_arrey)]
	groups = {x:[x] for x in range(len_arrey)}
	lst = ft_creat_lst(arrey, len_arrey)
	
	for _, index_p1, index_p2 in lst:
		gp_p1, gp_p2 = groups_index[index_p1], groups_index[index_p2]
		if gp_p1 == gp_p2:
			continue
		res = [index_p1, index_p2]
		to_add = groups[gp_p2]
		for point in to_add:
			groups_index[point] = gp_p1
			groups[gp_p1].append(point)
		del groups[gp_p2]
	
	return(arrey[res[0]][0] * arrey[res[1]][0])

s = time.time()
print(f"{day08_pt1(arrey)} in {round(time.time() - s, 5)}s")
s = time.time()
print(f"{day08_pt2(arrey)} in {round(time.time() - s, 5)}s")