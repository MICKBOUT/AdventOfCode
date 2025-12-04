import time

data = "5959566378-5959623425,946263-1041590,7777713106-7777870316,35289387-35394603,400-605,9398763-9592164,74280544-74442206,85684682-85865536,90493-179243,202820-342465,872920-935940,76905692-76973065,822774704-822842541,642605-677786,3759067960-3759239836,1284-3164,755464-833196,52-128,3-14,30481-55388,844722790-844967944,83826709-83860070,9595933151-9595993435,4216-9667,529939-579900,1077949-1151438,394508-486310,794-1154,10159-17642,5471119-5683923,16-36,17797-29079,187-382"

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
