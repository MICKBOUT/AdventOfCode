input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [tuple(map(int, line.strip().split(','))) for line in file]

# for line in arrey:
# 	print(line)

from math import sqrt
import time

def day08_pt1(arrey):
	lst = []
	len_arrey = len(arrey)
	gp = [x for x in range(len_arrey)] #groups of the points i
	
	groups = {x:[x] for x in range(len_arrey)}
	
	#print(gp, groups)
	for i in range(len_arrey - 1):
		x1, y1, z1 = arrey[i]
		for j in range(i + 1, len_arrey):
			x2, y2, z2 = arrey[j]
			ell = (sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), i, j) #dst, i, j
			lst.append(ell)

	lst.sort(key= lambda x:x[0])

	for i in range(len_arrey):
		_, p1, p2 = lst[i]
		#take all the points in the gp of p2:

		gp_p1, gp_p2 = gp[p1], gp[p2] #groups of the p1 and p2
		if gp_p2 == gp_p1:
			continue
		
		to_add = groups[gp_p2]
		for point in to_add:
			gp[point] = gp_p1
			groups[gp_p1].append(point)
		del groups[gp_p2]
	
	m1, m2, m3 = 0, 0, 0
	for key, value in groups.items():
		l = len(value)
		if l > m1:
			m1, m2, m3 = l, m1, m2
		elif l > m2:
			m2, m3 = l, m2
		elif l > m3:
			m3 = l
	
	return(m1 * m2 * m3)
	
def day08_pt2(arrey):
	lst = []
	len_arrey = len(arrey)
	gp = [x for x in range(len_arrey)] #groups of the points i
	
	groups = {x:[x] for x in range(len_arrey)}
	
	#print(gp, groups)
	for i in range(len_arrey - 1):
		x1, y1, z1 = arrey[i]
		for j in range(i + 1, len_arrey):
			x2, y2, z2 = arrey[j]
			ell = (sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2), i, j) #dst, i, j
			lst.append(ell)

	lst.sort(key= lambda x:x[0])
	
	for dst, p1, p2 in lst:
		#take all the points in the gp of p2:

		gp_p1, gp_p2 = gp[p1], gp[p2] #groups of the p1 and p2
		if gp_p1 == gp_p2:
			continue
		res = [p1, p2]
		to_add = groups[gp_p2]
		for point in to_add:
			gp[point] = gp_p1
			groups[gp_p1].append(point)
		del groups[gp_p2]
	
	return(arrey[res[0]][0] * arrey[res[1]][0])

print(day08_pt1(arrey))
print(day08_pt2(arrey))