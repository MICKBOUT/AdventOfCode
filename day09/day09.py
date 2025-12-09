import time
from shapely.geometry import Point, Polygon

input_file = "input.txt"
with open(input_file, "r") as file:
	arrey = [tuple(map(int, line.strip().split(','))) for line in file]

def ft_creat_lst(arrey, len_arrey):
	lst = []
	for i in range(len_arrey - 1):
		y1, x1 = arrey[i]
		for j in range(i + 1, len_arrey):
			y2, x2 = arrey[j]
			ell = (y1, x1, y2, x2)
			lst.append(ell)
		lst.sort(key=lambda x: abs(x[0] - x[2]) * abs(x[1] - x[3]), reverse=True)
	return (lst)

def day09_pt2(arrey):
	l_arrey = len(arrey)
	polygon = Polygon([(x, y) for (y, x) in arrey])
	gp_sqrt = ft_creat_lst(arrey, l_arrey)

	max_area = 0

	for y1, x1, y2, x2 in gp_sqrt:
		sqrt_pt = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
		rectangle = Polygon(sqrt_pt)
		if polygon.covers(rectangle):
			return (abs(sqrt_pt[0][0] - sqrt_pt[1][0]) + 1) * (abs(sqrt_pt[0][1] - sqrt_pt[2][1]) + 1)

s = time.time()
print(f"{day09_pt2(arrey)} in {time.time() - s}s")
