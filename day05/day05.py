import time

with open("input.txt", "r") as file:
	data = [line.strip() for line in file]

def day05_v1(data):
	res = 0
	ranges = sorted([tuple(map(int, line.split('-'))) for line in data[:data.index("")]], key= lambda x: x[0])
	for nb in tuple(map(int, data[data.index("") + 1:])):
		for n in ranges:
			if n[0] > nb:
				break 
			if n[1] >= nb:
				res += 1
				break
	return (res)

def day05_v2(data):
	res = 0
	ranges = sorted([tuple(map(int, line.split('-'))) for line in data[:data.index("")]], key= lambda x: x[0])
	start, end = ranges[0]
	for s, e in ranges:
		if s > end:
			res += end - start + 1
			start, end = s, e
		elif e > end:
			end = e
	return res + end - start + 1

s = time.time()
print(f"{day05_v1(data)} in {time.time() - s}s")
s = time.time()
print(f"{day05_v2(data)} in {time.time() - s}s")
