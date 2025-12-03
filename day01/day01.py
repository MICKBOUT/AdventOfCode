import time

with open("input.txt", "r") as file:
	arrey = [line.strip() for line in file]

def count_v1(data):
	clock = 50
	res = 0
	for d in data:
		if (d[0] == 'L'):
			step = -int(d[1:])
		else:
			step = int(d[1:])
		clock += step
		if (clock == 0):
			res += 1
	return (res)

def count_v2(data):
	clock = 50
	res = 0
	for d in data:
		if (d[0] == 'L'):
			step = -int(d[1:])
			if clock == 0:
				res -= 1
		else:
			step = int(d[1:])
			if clock == 100:
				res -= 1
		clock += step
		if (clock <= 0):
			res += (abs(clock) // 100) + 1
			if clock != 0:
				clock %= 100
		if (clock >= 100):
			res += clock // 100
			if clock != 100:
				clock %= 100
	return res	

s = time.time()
print(f"pt1 = {count_v1(arrey)} in {round(time.time() - s, 5)}s")
s = time.time()
print(f"pt2 = {count_v2(arrey)} in {round(time.time() - s, 5)}s")