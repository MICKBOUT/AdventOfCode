import time

def add_mirror(start, end):
	res = 0
	left = str(start)
	if (len(start) % 2) == 0:
		left = left[:len(str)//2]
	start = int(left)
	for nb in range(start, end + 1):
		s = str(nb)
		m = len(s) >> 1
		if s[:m] == s[m:]:
			res += nb
	return res

def add_mirror_v2(start, end):
	res = 0
	for nb in range(start, end + 1):
		s = str(nb)
		l = len(s)
		m = l >> 1
		while m > 0:
			if (l % m == 0):
				j = 0
				while (s[j*m:(j+1)*m] == s[(j+1)*m : (j+2)*m]):
					j += 1
				if j + 1 == (l // m):
					res += nb
					break
			m -= 1
	return res

def day02(s, part):
	res = 0
	range_nb = s.split(',')
	for r in range_nb:
		start, end = r.split('-')
		res += add_mirror(int(start), int(end)) if part == 0 else add_mirror_v2(int(start), int(end))
	return res

input_file = "input.txt"
with open(input_file, "r") as file:
	s1 = file.read()

for i in range(2):
	s = time.time()
	print(f"day02 pt{i} : res = {day02(s1, i)} in {round(time.time() - s, 3)}s")
